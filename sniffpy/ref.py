from typing import List

def check_condition(code_point: str, condition: List[str]) -> bool:
    for char in condition:
        if code_point == char:
            return True
    return False

def collect_code_points(str_input: str, condition: List[str], pos: int, exclusion: bool = True) -> (str, int): #Implements: https://infra.spec.whatwg.org/#collect-a-sequence-of-code-points
    result = []
    while pos != len(str_input) and check_condition(str_input[pos], condition) ^ exclusion:
        result.append(str_input[pos])
        pos += 1
    return ''.join(result), pos

def collect_http_quoted_string(str_input: str, pos: int, exact_value: bool = False) -> (str, int):
    position_start = pos
    value = ""
    assert str_input[pos] == '"'
    pos += 1

    while True:
        append_value, pos = collect_code_points(str_input, ['"', '\\'], pos)
        value += append_value
        
        if len(str_input) <= pos:
            break

        quote_or_backslash = str_input[pos]
        pos += 1

        if quote_or_backslash == '\\':
            if len(str_input) <= pos:
                val += "\\"
                break
            value += str_input[pos]
            pos += 1
        else:
            assert quote_or_backslash == '"'
            break

    if exact_value:
        return value, pos

    return str_input[position_start:pos+1], pos
