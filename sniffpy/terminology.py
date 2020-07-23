import re

def check_http_quoted_string_token_code_points(str_input: str) -> bool:
    raise NotImplementedError

def check_http_token_code_points(str_input: str) -> bool:
    reg = re.compile(r'^[a-zA-Z0-9\!#\$%&\'\*\+-\.\^_`\|~]+$')
    return reg.search(str_input)
