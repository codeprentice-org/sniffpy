""" This module implements matching algorithms as described in
https://mimesniff.spec.whatwg.org/#matching-a-mime-type-pattern"""

from sniffpy.mimetype import MIMEType, parse_mime_type
import sniffpy.constants as const

def match_video_audio_type_pattern(resource: bytes) -> MIMEType:
    raise NotImplementedError

def match_pattern(resource: bytes, pattern: bytes, mask: bytes, ignored: bytes):
    """
    Implementation of algorithm in:x
    https://mimesniff.spec.whatwg.org/#matching-a-mime-type-pattern
    True if pattern matches the resource. False otherwise.
    """
    resource = bytearray(resource)
    pattern = bytearray(pattern)
    mask = bytearray(mask)

    if len(pattern) != len(mask):
        return False
    if len(resource) < len(pattern):
        return False

    start = 0
    for byte in resource:
        if byte in ignored:
            start += 1
        else:
            break

    iteration_tuples = zip(resource[start:], pattern, mask)
    for resource_byte, pattern_byte, mask_byte in iteration_tuples:
        masked_byte = resource_byte & mask_byte
        if masked_byte != pattern_byte:
            return False
    return True


def match_image_type_pattern(resource: bytes) -> bool :
    """
    Implementation of algorithm in:
    https://mimesniff.spec.whatwg.org/#matching-an-image-type-pattern

    Returns: Image MIME Type if some image pattern matches the resource
    or UNDEFINED otherwise. 

    """
    for row in const.IMAGE_PATTERNS:
        pattern = row[0]
        mask =row[1] 
        mime_type = parse_mime_type(row[3])
        string_to_ignore =row[2]
        ignored = [] if "None" in string_to_ignore else WHITESPACE
        pattern_found = match_pattern( resource = resource, 
                                       pattern = pattern,
                                       mask = mask,
                                       ignored = ignored
        )

        if pattern_found:
            return MIMEType

        return const.UNDEFINED
