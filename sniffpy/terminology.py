import re


def contains_binary_bytes(resource: bytes) -> bool:
    contains_binary = False
    for byte in resource:

        in_range1 = int.from_bytes(b'\x00', "little") <= byte <= int.from_bytes(b'\x08', "little")
        in_range2 = byte == int.from_bytes(b'\x0b', "little")
        in_range3 = int.from_bytes(b'\x0e', "little") <= byte <= int.from_bytes(b'\x1a', "little")
        in_range4 = int.from_bytes(b'\x1c', "little") <= byte <= int.from_bytes(b'\x1f', "little")
        if in_range1 or in_range2 or in_range3 or in_range4:
            contains_binary = True

    return contains_binary


def check_http_quoted_string_token_code_points(str_input: str) -> bool:

    for char in str_input:
        in_range1 = u'\u0009' <= char <= u'\u007e'
        in_range2 = u'\u0080' <= char <= u'\u00ff'
        if not (char == u'\u0009' or in_range1 or in_range2):
            return False

    return True


def check_http_token_code_points(str_input: str) -> bool:
    reg = re.compile(r'^[a-zA-Z0-9\!#\$%&\'\*\+-\.\^_`\|~]+$')
    return reg.search(str_input)
