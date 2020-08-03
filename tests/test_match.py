""" This module should implement tests pertaining the match module in the package"""

import sniffpy.match as match
from sniffpy.mimetype import parse_mime_type
from tests.utils import mimetype_is_equal 
import pytest

def test_match_pattern():
    """Tests whether match_pattern implementation works"""
    ignore = b'\x01\x02'
    sequence = b'\x01\x02\xff'
    mask = b'\xdd'
    pattern = b'\xdd'
    true_value = match.match_pattern(
        resource=sequence,
        ignored=ignore,
        mask=mask,
        pattern=pattern
    )
    sequence = b'\x01\x00\x02\xff'
    false_value = match.match_pattern(
        resource=sequence,
        ignored=ignore,
        mask=mask,
        pattern=pattern
    )
    assert not false_value
    assert true_value


class TestImageMatching:
    mime_types = ['image/gif', 'image/png', 'image/jpeg','undefined/undefined']
    content = [
        b'\x47\x49\x46\x38\x39\x61\x32\xa4\x90',
        b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x43',
        b'\xff\xd8\xff\x78\x98\x23\x32\xfa\x89',
        b'\xfa\xd8\xff\x78\x98\x23\x32\xfa\x89'
    ]

    @pytest.mark.parametrize('mime, resource', list(zip(mime_types, content)))
    def test_match_image_pattern(self, mime, resource):
        """ Tests the most importnat image MIMEs with simulated content"""
        computed_type = match.match_image_type_pattern(resource)
        actual_type = parse_mime_type(mime)
        mimetype_is_equal(computed_type, actual_type)
        


