import re


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
