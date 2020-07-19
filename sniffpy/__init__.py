import re

class MIMEType:

	def __init__(self, _type: str, _subtype: str, parameters: dict = None) -> None:
		self.type = _type
		self.subtype = _subtype
		if _parameters is None:
			self.parameters = dict()
		else:
			self.parameters = _parameters

	def essence(self) -> str:
		return self.type + "/" + self.subtype

	def __str__(self) -> str:
		return self.type + "/" + self.subtype #TODO: Implement parameter

	def is_xml(self) -> bool:
		if len(self.subtype) > 3 and self.subtype[-4:] == "+xml":
			return True
		if (self.type == "text" or self.type == "application") and self.subtype == "xml":
			return True
		return False

	def is_unknown(self) -> bool:
		return self.essence() == "unknown/unknown" or self.essence() == "application/unknown" or self.essence() == "*/*"

	def is_image(self) -> bool:
		return self.type == "image"

	def is_video_audio(self) -> bool:
		return self.type == "audio" or self.type == "video" or self.essence() == "application/ogg"

def sniff_unknown(resource: bytes, sniff_scriptable: bool = False): #might need more arguments
	raise NotImplementedError

def sniff_mislabeled_binary(resource: bytes) -> MIMEType:
	raise NotImplementedError

def sniff_mislabeled_feed(resource: bytes) -> MIMEType:
	raise NotImplementedError

def match_image_type_pattern(resource: bytes) -> MIMEType:
	raise NotImplementedError

def match_video_audio_type_pattern(resource: bytes) -> MIMEType:
	raise NotImplementedError

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
	return result.join(''), pos

def collect_http_quoted_string(str_input: str, pos: int, exact_value: bool = False) -> str, int:
	raise NotImplementedError

def check_http_token_code_points(str_input: str) -> bool:
	reg = re.compile('^[a-zA-Z0-9\!#\$%&\'\*\+-\.\^_`\|~]+$')
	return reg.search(str_input)

def parse_mime_type(str_input: str) -> MIMEType:
	str_input = str_input.strip() #might have to specify HTTP whitespace characters
	pos = 0
	_type, pos = collect_code_points(str_input, ['/'], pos)

	if _type == "" or not check_http_token_code_points(_type):
		return None
	if len(str_input) <= pos:
		return None

	pos += 1
	_subtype, pos = collect_code_points(str_input, [';'], pos)
	_subtype = _subtype.rstrip()	

	if _subtype == "" or not check_http_token_code_points(_subtype):
		return None

	_parameters = dict()

	while pos < len(str_len):
		pos += 1
		_, pos = collect_code_points(str_input, ['\u000A', '\u000D', '\u0009', '\u0020'], pos)
		_parameterName, pos = collect_code_point(str_input, [';', '='], pos)
		_parameterName = _parameterName.lower()
		
		if len(str_len) <= pos:
			break
		if  str_input[pos] == ';':
			continue
		
		pos += 1
		if str_input[pos] == '"':
			_parameterValue, pos = collect_http_quoted_string(str_input, pos, expected_value=True)
			_, pos = collect(str_input, [';'], pos)
		else:
			_parameterValue, pos = collect_code_point(str_input, [';'], pos)
			_parameterValue = _parameterValue.rstrip()
			if _parameter == '':
				continue
		
		if (not _parameterName == '' and check_http_token_code_points(_parameterName) 
				and check_http_quoted_string_token_code_points(_parameterValue) and not _parameterName in _parameters):
			_parameters[_parameterName] = _parameterValue

	mimeType = MIMEType(_type.lower(), _subtype.lower(), parameters=_parameters)


def sniff(resource: bytes, mime_type_string: str = "unknown/unknown", no_sniff: bool = False, check_for_apache_bug: bool = False) -> str:
	mime_type = parse_mime_type(mime_type_string)
	if mime_type.is_unknown():
		return sniff_unknown(resource, sniff_scriptable=not no_sniff)
	if no_sniff:
		return mime_type
	if check_for_apache_bug:
		return sniff_mislabeled_binary(resource)
	if mime_type.is_xml():
		return mime_type
	if mime_type.essence() == "text/html":
		sniff_mislabeled_feed(resource)
	if mime_type.is_image(): #TODO: implement checking suppported image by user agent
		match_type = match_image_type_pattern(resource)
		if not match_type is None:
			return match_type
	if mime_type.is_video_audio(): #TODO: implement checking suppported image by user agent
		match_type = match_image_type_pattern(resource)
		if not match_type is None:
			return match_type
	return mime_type
