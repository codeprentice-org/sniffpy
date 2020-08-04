""" Moudule with functions or utilities"""


def parse_vint(sequence: bytes, index: int) -> (int, int):
    """ Implementation of https://mimesniff.spec.whatwg.org/#parse-a-vint"""
    mask = 128
    max_len = 8
    number_size = 1
    zero = b'x00'

    while number_size < max_len and number_size < len(sequence):
        if sequence[index] & mask != zero:
            break
        mask = mask >> 1
        number_size += 1

    index = 0
    parsed_number = sequence[index] & ~ mask
    index += 1
    bytes_remaining = number_size

    while bytes_remaining != 0:
        parsed_number = parsed_number << 8
        parsed_number = parsed_number | sequence[index]
        index += 1
        if index >= len(sequence):
            break
        bytes_remaining -= 1

    return (parsed_number, number_size)


def parse_mp3_frame(resource: bytes, offset: int, parsed_values: dict) -> int:
    raise NotImplementedError


def match_mp3_header(
        resource: bytes,
        offset: int,
        parsed_values: dict) -> bool:
    raise NotImplementedError


def compute_mp3_frame_size(
        version: int,
        bit_rate: int,
        freq: int,
        pad: int) -> int:
    raise NotImplementedError
