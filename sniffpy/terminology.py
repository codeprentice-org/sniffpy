import re


def check_http_quoted_string_token_code_points(str_input: str) -> bool:

    for char in str_input:
        inRange1 = u'\u0009' <= char <= u'\u007e'
        inRange2 = u'\u0080' <= char <= u'\u00ff'
        if not (char == u'\u0009' or inRange1 or inRange2):
            return False

    return True


def check_http_token_code_points(str_input: str) -> bool:
    reg = re.compile(r'^[a-zA-Z0-9\!#\$%&\'\*\+-\.\^_`\|~]+$')
    return reg.search(str_input)
