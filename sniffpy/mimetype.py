"""
Implementation of section 4 in the specification:
https://mimesniff.spec.whatwg.org/#understanding-mime-types

Contains the MIMEType class definition and an implementation
of MIME type parsing.
"""

from . import ref
from . import terminology

class MIMEType:
    """
    This class defines a MIME type and has as its methods
    and properties, definitions and algorithms from
    section 4 of the specification.
    """

    def __init__(self, _type: str, _subtype: str,
                 parameters: dict = None) -> None:
        """
        This initializes a MIME type.

        * type: the general category into which a resource falls under,
        for example, "text"
        * subtype: the exact category of the specific type, for example,
        "plain"
        * parameters: a string to string mapping containing
        further information of the MIME type, for example, {"charset": "UTF-8"}
        """

        self.type = _type
        self.subtype = _subtype
        if parameters is None:
            self.parameters = dict()
        else:
            self.parameters = parameters

    def essence(self) -> str:
        return self.type + "/" + self.subtype

    def __str__(self) -> str: #TODO: Should be an implementation of 4.5
        return self.type + "/" + self.subtype

    def is_xml(self) -> bool:
        if len(self.subtype) > 3 and self.subtype[-4:] == "+xml":
            return True
        if (self.type == "text" or self.type ==
                "application") and self.subtype == "xml":
            return True
        return False

    def is_unknown(self) -> bool:
        return self.essence() == "unknown/unknown" or self.essence(
        ) == "application/unknown" or self.essence() == "*/*"

    def is_image(self) -> bool:
        return self.type == "image"

    def is_video_audio(self) -> bool:
        return self.type == "audio" or self.type == "video" or self.essence() == "application/ogg"

    def __eq__(self, obj):
        value = self.type == obj.type and self.subtype == obj.subtype
        value = value and self.parameters == obj.parameters
        return value

def parse_mime_type(str_input: str) -> MIMEType:
    """
    Implementation of algorithm in:
    https://mimesniff.spec.whatwg.org/#parsing-a-mime-type

    Given a string representation of a MIME type this function
    parses it and returns its representation as an instance of MIMEType
    """

    str_input = str_input.strip()  # might have to specify HTTP whitespace characters
    pos = 0
    _type, pos = ref.collect_code_points(str_input, ['/'], pos)

    if _type == "" or not terminology.check_http_token_code_points(_type):
        return None
    if len(str_input) <= pos:
        return None

    pos += 1
    _subtype, pos = ref.collect_code_points(str_input, [';'], pos)
    _subtype = _subtype.rstrip()

    if _subtype == "" or not terminology.check_http_token_code_points(
            _subtype):
        return None

    _parameters = dict()
    while pos < len(str_input):
        pos += 1
        _, pos = ref.collect_code_points(
            str_input, ['\u000A', '\u000D', '\u0009', '\u0020'], pos, exclusion=False)
        _parameter_name, pos = ref.collect_code_points(
            str_input, [';', '='], pos)
        _parameter_name = _parameter_name.lower()
        if len(str_input) <= pos:
            break
        if str_input[pos] == ';':
            continue

        pos += 1
        if str_input[pos] == '"':
            _parameter_value, pos = ref.collect_http_quoted_string(
                str_input, pos, exact_value=True)
            _, pos = ref.collect_code_points(str_input, [';'], pos)
        else:
            _parameter_value, pos = ref.collect_code_points(
                str_input, [';'], pos)
            _parameter_value = _parameter_value.rstrip()
            if _parameter_value == '':
                continue

        if (_parameter_name != '' and terminology.check_http_token_code_points(_parameter_name)
                and terminology.check_http_quoted_string_token_code_points(_parameter_value)
                and _parameter_name not in _parameters):
            _parameters[_parameter_name] = _parameter_value

    return MIMEType(_type.lower(), _subtype.lower(), parameters=_parameters)
