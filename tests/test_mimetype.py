"""This module implements tests pertaining to the mimetype module"""

import sniffpy.mimetype as mimetype

def test_parse_mime_type_basic():
    """Tests whether basic parsing works"""
    
    test_string = "text/html"
    mimetype_obj = mimetype.parse_mime_type(test_string)
    
    assert mimetype_obj.type == "text"
    assert mimetype_obj.type == "html"
