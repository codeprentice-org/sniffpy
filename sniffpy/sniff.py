from . import match
from . import mimetype
from .mimetype import MIMEType

def sniff_unknown(resource: bytes, sniff_scriptable: bool = False): #might need more arguments
	raise NotImplementedError

def sniff_mislabeled_binary(resource: bytes) -> MIMEType:
	raise NotImplementedError

def sniff_mislabeled_feed(resource: bytes) -> MIMEType:
	raise NotImplementedError

def sniff(resource: bytes, mime_type_string: str = "unknown/unknown", no_sniff: bool = False, check_for_apache_bug: bool = False) -> str:
	mime_type = mimetype.parse_mime_type(mime_type_string)
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
		match_type = match.match_image_type_pattern(resource)
		if not match_type is None:
			return match_type
	if mime_type.is_video_audio(): #TODO: implement checking suppported image by user agent
		match_type = match.match_image_type_pattern(resource)
		if not match_type is None:
			return match_type
	return mime_type
