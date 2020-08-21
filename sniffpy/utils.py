""" Moudule with functions or utilities"""
import sniffpy.constants as const


def parse_vint(sequence: bytes, index: int) -> (int,int):
    """ Implementation of https://mimesniff.spec.whatwg.org/#parse-a-vint"""
    mask = 128
    max_len = 8
    number_size = 1

    
    while number_size < max_len and number_size <len(sequence):
        if sequence[index] & mask != 0:
            break
        mask = mask >> 1
        number_size += 1

    index = 0
    parsed_number = sequence[index] & ~ mask
    index += 1
    bytes_remaining = number_size

    while bytes_remaining != 0:
        parsed_number = parsed_number << 8
        parsed_number = parsed_number | sequence[index]
        index += 1
        if index >= len(sequence):
            break
        bytes_remaining -= 1

    return (parsed_number, number_size)


def match_mp3_header(resource: bytes, offset: int, parsed_values: dict) -> bool:
    """ Implements the aglorithm in specification and modifies the  parsed_vaues dictionary to add relevant information of the file.
Solution is not cleanbut is the most consistent with the specification"""

    #We use b'\x02'[0] to extract unsigned int from byte (2 in this case)
    if len(resource) < 4:
        return False
    if resource[offset] != b'\xff' and resource[offset + 1] & b'\xe0'[0] != b'\xe0'[0]:
        return False

    layer = resource[offset + 1]  & b'\x06'[0]
    parsed_values['layer'] = layer[0] >> 1
    if parsed_values['layer'] == 0: 
        return False

    bit_rate = resource[offset + 2] & b'\x0c'[0]
    parsed_values['bit_rate'] = bit_rate[0] >> 4
    if parsed_values['bit_rate'] == 15:
        return False

    sample_rate = resource[offset + 2] & b'\x0c'[0]
    parsed_values['sample_rate'] = sample_rate >> 2
    if parsed_values['sample_rate'] == 3:
        return False

    parsed_values['freq'] = const.SAMLE_RATES[sample_rate]
    parsed_values['final_layer'] = 4 - resource[offset + 1]
    if final_layer & b'\x06'[0] != 3:
        return False

    return True

def compute_mp3_frame_size(version: int, bit_rate: int, freq: int, pad: int) -> int:
    scale = 72 if version == 1 else 144
    size = bit_rate * scale / freq
    size = size + 1 if pad != 0 else size
    return size

def parse_mp3_frame(resource: bytes, offset: int, parsed_values: dict) -> int:
    """Parses and mp3 frame and adds criteria to the parsed_value dict
    Returns offset after operations.
    Solution is not clean but is consistent with specification
    """
    s = offset
    parsed_values['version'] = (resource[s+1] & b'\x18'[0]) >> 3
    bit_rate_index = (resource[s+2] & b'\xf0'[0]) >> 4
    if version & 1 != 0:
        bit_rate = const.MP25_RATES[bit_rate_index]
    else:
        bit_rate = const.MP3_RATES[bit_rate_index]
    parsed_values['bit_rate'] = bit_rate

    sample_rate_index = (resource[s+2] & b'\x0c'[0]) >> 2
    parsed_values['sample_rate'] = const.SAMPLE_RATES[sample_rate_index]
    parsed_values['pad'] = (resource[s+2] & b'\x02') >> 1

    return s


def match_padded_sequence(pattern: bytes, sequence: bytes, offset: int, end: int)-> bytes:

    if len(sequence) <= end :
        return False

    i = 0
    print(len(sequence))
    while i + offset + len(pattern) < len(sequence):
        print(sequence[offset + i: offset + i + len(pattern)])
        if sequence[offset + i: offset + i + len(pattern)] == pattern:
            return True
        elif sequence[offset + i] != 0:
            return False

    return False
                        
        
    
    

    
    

    
        
            
        
    
