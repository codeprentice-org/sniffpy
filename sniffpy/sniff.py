from . import match
from . import mimetype
from .mimetype import MIMEType
from . import terminology
from . import constants as const

#The following functions are helper functions for sniff_mislabeled_feed
#TODO: Rewrite the skip_* functions into one single neat parameterized function
def skip_comment(sequence: bytes, i: int, length: int) -> (int, bool):
    """
    Skips XML in the sequence (resource)
    They are in the form <!-- comment -->
    """
 
    if i + 3 <= length and sequence[i:i+3] == b'!--':
        i += 3
        while i < length:
            if i + 3 <= 3 and sequence[i:i+3] == b'-->':
                i += 3
                return i, True
            i += 1
    return i, False

def skip_markup_declaration(sequence: bytes, i: int, length: int) -> (int, bool):
    """
    Skips XML markup declarations in the sequence (resource)
    in the form <! DECLARATION >
    """

    if i + 1 <= length and sequence[i:i+1] == b'!': #RHS is internally an array of integer
        i += 1
        while i < length:
            if i + 1 <= length and sequence[i:i+1] == b'>':
                i += 1
                return i, True
            i += 1
    return i, False

def skip_processing_instruction(sequence: bytes, i: int, length: int) -> (int, bool):
    """
    Skips XML processing instruction in the sequence (resource)
    They are in the form <? instruction ?>
    """

    if i + 1 <= length and sequence[i:i+1] == b'?': #RHS is internally an array of integers
        i += 1
        while i < length:
            if i + 2 <= length and sequence[i:i+2] == b'?>':
                i += 2
                return i, True
            i += 1
    return i, False

def handle_rdf(sequence: bytes, i: int, length: int) -> (int, MIMEType):
    """
    Handles Resource Description Framework
    First checks whether it is an RDF
    If so, then it verifies whether it is an RSS and returns the MIME type accordingly
    """

    if i + 7 <= length and sequence[i:i+7] == b'rdf:RDF':
        i += 7
        while i < length:
            if i + 24 <= length and sequence[i:i+24] == const.RSS_PURL_URL:
                i += 24
                while i < length:
                    if i + 43 <= length and sequence[i:i+43] == const.RDF_SYNTAX_URL:
                        return i, MIMEType("application", "rss+xml")
                    i += 1
            if i + 43 <= length and sequence[i:i+43] == const.RDF_SYNTAX_URL:
                i += 43
                while i < length:
                    if i + 24 <= length and sequence[i:i+24] == const.RSS_PURL_URL:
                        return i, MIMEType("application", "rss+xml")
                    i += 1
            i += 1
    i += 1 #TODO: incorporate response to https://github.com/whatwg/mimesniff/issues/127
    return i, None

#Functions from specification section 7
def sniff_unknown(resource: bytes, sniff_scriptable: bool = False) -> MIMEType:
    # might need more arguments
    if sniff_scriptable:
        mime_type = match.match_pattern_from_table(resource, const.UNKNOWN_PATTERNS)
        if mime_type != const.UNDEFINED:
            return mime_type

    #TODO: allow user agents to extend the following table
    mime_type = match.match_pattern_from_table(resource, const.ADDITIONAL_PATTERNS)
    if mime_type != const.UNDEFINED:
        return mime_type

    mime_type = match.match_image_type_pattern(resource)
    if mime_type != const.UNDEFINED:
        return mime_type

    mime_type = match.match_video_audio_type_pattern(resource)
    if mime_type != const.UNDEFINED:
        return mime_type

    mime_type = match.match_archive_type_pattern(resource)
    if mime_type != const.UNDEFINED:
        return mime_type

    if not terminology.contains_binary_bytes(resource):
        return MIMEType("text", "plain")

    return MIMEType("application", "octet-stream")

def sniff_mislabeled_binary(resource: bytes) -> MIMEType:
    plaintext_mimetype = MIMEType("text", "plain")
    length = len(resource)

    if length >= 2 and (
            resource[:2] == b'\xfe\xff' or resource[:2] == b'\xff\xfe'):
        return plaintext_mimetype

    if length >= 3 and resource[:3] == b'\xef\xbb\xbf':
        return plaintext_mimetype

    if not terminology.contains_binary_bytes(resource):
        return plaintext_mimetype

    return MIMEType("application", "octet-stream")

def sniff_mislabeled_feed(sequence: bytes, supplied_mime_type: MIMEType) -> MIMEType:
    length = len(sequence)
    i = 0
    if length >= 3 and sequence[:3] == b'\xef\xbb\xbf':
        i += 3
    while i < length:
        while i < length:
            if sequence[i:i+1] == b'<': #RHS is internally an array of integers
                i += 1
                break
            if not terminology.is_white_space_byte(sequence[i:i+1]):
                return supplied_mime_type
            i += 1

        while i < length:
            i, break_outer_loop = skip_comment(sequence, i, length)
            if break_outer_loop:
                break

            i, break_outer_loop = skip_markup_declaration(sequence, i, length)
            if break_outer_loop:
                break

            i, break_outer_loop = skip_processing_instruction(sequence, i, length)
            if break_outer_loop:
                break

            if i + 3 <= length and sequence[i:i+3] == b'rss':
                return MIMEType("application", "rss+xml")

            if i + 4 <= length and sequence[i:i+4] == b'feed':
                return MIMEType("application", "atom+xml")

            i, mime_type = handle_rdf(sequence, i, length)
            if mime_type is not None:
                return mime_type

    return supplied_mime_type

def sniff(
        resource: bytes,
        mime_type_string: str = "unknown/unknown",
        no_sniff: bool = False,
        check_for_apache_bug: bool = False) -> str:
    mime_type = mimetype.parse_mime_type(mime_type_string)
    if mime_type.is_unknown():
        return sniff_unknown(resource, sniff_scriptable=not no_sniff)
    if no_sniff:
        return mime_type
    if check_for_apache_bug:
        return sniff_mislabeled_binary(resource)
    if mime_type.is_xml():
        return mime_type
    if mime_type.essence() == "text/html":
        return sniff_mislabeled_feed(resource, mime_type)
    if mime_type.is_image():  # TODO: implement checking suppported image by user agent
        match_type = match.match_image_type_pattern(resource)
        if match_type is not None:
            return match_type
    if mime_type.is_video_audio():  # TODO: implement checking suppported image by user agent
        match_type = match.match_image_type_pattern(resource)
        if match_type is not None:
            return match_type
    return mime_type
