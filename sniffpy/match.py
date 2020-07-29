def match_pattern(resource: bytes, pattern: bytes, mask: bytes, ignored: bytes):
    """
    Implementation of algorithm in:
    https://mimesniff.spec.whatwg.org/#matching-a-mime-type-pattern
    True if pattern matches the resource. False otherwise.
    """
    resource = bytearray(resource)
    pattern = bytearray(pattern)
    mask = bytearray(mask)

    if len(pattern) != len(mask):
        return False
    if len(resource) < len(pattern):
        return False

    start = 0
    for byte in resource:
        if byte in ignored:
            start += 1
        else:
            break

    iteration_tuples = zip(resource[start:], pattern, mask)
    for resource_byte, pattern_byte, mask_byte in iteration_tuples:
        masked_byte = resource_byte & mask_byte
        if masked_byte != pattern_byte:
            return False

    return True
