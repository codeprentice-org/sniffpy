""" This module implements matching algorithms as described in
https://mimesniff.spec.whatwg.org/#matching-a-mime-type-pattern"""

from typing import List
from sniffpy.mimetype import MIMEType, parse_mime_type
from sniffpy.utils import match_mp3_header, compute_mp3_frame_size, parse_mp3_frame

import sniffpy.utils as utils

from . import constants as const


def match_pattern(
        resource: bytes,
        pattern: bytes,
        mask: bytes,
        ignored: bytes):
    """
    Implementation of algorithm in:x
    https://mimesniff.spec.whatwg.org/#matching-a-mime-type-pattern
    True if pattern matches the resource. False otherwise.
    """

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

def match_pattern_from_table(resource: bytes, table: List[List[bytes]]):
    """
    Utility function for looping through a table of patterns
    to return matching pattern

    Returns: MIME Type of the row if some pattern matches
    the corresponding resource or UNDEFINED otherwise.
    """
    for row in table:
        pattern = row[0]
        mask = row[1]
        mime_type = parse_mime_type(row[3])
        ignored = row[2]
        pattern_found = match_pattern(resource=resource,
                                      pattern=pattern,
                                      mask=mask,
                                      ignored=ignored
                                      )

        if pattern_found:
            return mime_type

    return const.UNDEFINED

def match_image_type_pattern(resource: bytes) -> bool:
    """
    Implementation of algorithm in:
    https://mimesniff.spec.whatwg.org/#matching-an-image-type-pattern

    Returns: Image MIME Type if some image pattern matches the resource
    or UNDEFINED otherwise.

    """
    return match_pattern_from_table(resource, const.IMAGE_PATTERNS)

def match_video_audio_type_pattern(resource: bytes) -> MIMEType:
    raise NotImplementedError

def match_font_type_pattern(resource: bytes) -> MIMEType:
    raise NotImplementedError

def match_archive_type_pattern(resource: bytes) -> MIMEType:
    raise NotImplementedError

def is_mp4_pattern(resource: bytes) -> bool:
    """ Determines whether a byte sequence (resource) mathces the
    signature for MP4"""
    if len(resource) < 4:
        return False

    box_size = int.from_bytes(resource[:4], 'big')
    if len(resource) < box_size or box_size % 4 != 0:
        return False
    if resource[4:8] != b'ftyp':
        return False
    if resource[8:11] == b'mp4':
        return True

    bytes_read = 16
    while bytes_read < box_size:
        if resource[bytes_read: bytes_read + 3] == b'mp4':
            return True
        bytes_read += 4

    return False


def is_mp3_pattern(resource: bytes) -> bool:
    """Determines whether a byte sequence matches the signature for mp3 wihtout ID3"""
    # TO DO TEST THIS Function
    offset = 0
    parsed_values = {}

    if not match_mp3_header(resource, offset, parsed_values):
        return False
    offset = parse_mp3_frame(resource, offset, parsed_values)
    skipped_bytes = compute_mp3_frame_size(parsed_values['version'],
                                           parsed_values['bit_rate'],
                                           parsed_values['freq'],
                                           parsed_values['pad'])
    if skipped_bytes < 4 or skipped_bytes > offset - len(resource):
        return False

    offset += offset

    return  match_mp3_header(resource, offset, parsed_values)


def is_webm_pattern(resource: bytes) -> bool:
    """Determines whether a byte sequence mateches the signature for WebM"""
    if len(resource) < 4:
        return False
    if resource[:4] != b'\x1a\x45\xdf\xa3':
        return False
    print(resource[:40])
    
    i = 4
    while i < len(resource) and i < 38:
        
        if resource[i:i+2] == b'\x42\x82':
            i += 2
            if i >= len(resource):
                break
            parsed_number, number_size = utils.parse_vint(resource, i)
            i += number_size
            if i > len(resource) - 4:
                break
            print(i)
            match = utils.match_padded_sequence(b'webm', resource, i, end=-float('inf'))
            if match:
                return True
        i += 1 

    return False    

