def check_condition(code_point: str, condition: List[str]) -> bool:
	for char in condition:
		if code_point == char:
			return True
	return False

def collect_code_points(str_input: str, condition: List[str], pos: int) -> (str, int): #Implements: https://infra.spec.whatwg.org/#collect-a-sequence-of-code-points
	result = []
	while not check_condition(str_input[pos], condition):
		result.append(str_input[pos])
		pos += 1
	return ''.join(result), pos

def collect_http_quoted_string(str_input: str, pos: int, exact_value: bool = False) -> (str, int):
	raise NotImplementedError
