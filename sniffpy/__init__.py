class MIMEType:

	def __init__(self, _type: str, _subtype: str, _parameters: dict = None) -> None:
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

def parse_mime_type(mime_type_string: str) -> MIMEType:
	raise NotImplementedError

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
