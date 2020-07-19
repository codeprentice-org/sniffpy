from .mimetype import MIMEType

def match_image_type_pattern(resource: bytes) -> MIMEType:
	raise NotImplementedError

def match_video_audio_type_pattern(resource: bytes) -> MIMEType:
	raise NotImplementedError
