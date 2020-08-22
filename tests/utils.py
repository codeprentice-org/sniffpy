from sniffpy.mimetype import MIMEType

def mimetype_is_equal(first_mime: MIMEType, second_mime: MIMEType) -> None:
    """ Verifies that both MIMEType objects are equal for purposes of testing"""
    assert first_mime.type == second_mime.type
    assert first_mime.subtype == second_mime.subtype

    for key in  first_mime.parameters.keys():
        assert key in second_mime.parameters
        assert first_mime.parameters[key] == second_mime.parameters[key]

    for key in  second_mime.parameters.keys():
        assert key in second_mime.parameters
        assert first_mime.parameters[key] == second_mime.parameters[key]
