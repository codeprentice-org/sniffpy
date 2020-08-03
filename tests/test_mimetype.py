"""This module implements tests pertaining to the mimetype module"""

import sniffpy.mimetype as mimetype

def test_parse_mime_type_basic():
    """Tests whether basic parsing works"""
    
    test_string = "text/html"
    mimetype_obj = mimetype.parse_mime_type(test_string)

    assert mimetype_obj.type == "text"
    assert mimetype_obj.subtype == "html"

def test_parse_mime_type_single_unquoted_parameter():
    """Tests whether parsing works with a single unquoted parameter"""
    
    test_string = "text/html;charset=ISO-8859-1"
    mimetype_obj = mimetype.parse_mime_type(test_string)

    assert mimetype_obj.type == "text"
    assert mimetype_obj.subtype == "html"
    assert len(mimetype_obj.parameters) == 1 
    assert "charset" in mimetype_obj.parameters
    assert mimetype_obj.parameters['charset'] == "ISO-8859-1"

