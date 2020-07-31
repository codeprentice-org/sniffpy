""" This module should implement tests pertaining the match module in the package"""

import sniffpy.match as match

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
# def test_match_image_pattern()
#         """ Tests the most importnat image MIMEs with simulated content"""
#         mimes = ['image/gif', 'image/png', 'image/jpeg','undefined']
#         content = [
             #             b'\x47\x49\x46\x38\x39\x61\x32\xa4\x90',
#             b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x43',
#             b'\xff\xd8\xff\x43\x43\x89\x90\x40\x90',
#             b'\x22\xd8\xff\x43\x43\x89\x90\x40\x90'
#         ]
#         for mime, body in zip(mimes, content):
#             computed_type = sniff.match_image_pattern(body)
#             error_msg =  mime + " not equal to " + computed_type
#             self.assertEqual(computed_type, mime, error_msg)
