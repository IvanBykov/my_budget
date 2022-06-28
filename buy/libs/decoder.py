import quopri


def decode_str(str):
    str_byte = bytes(str, 'UTF-8')
    str_decode = quopri.decodestring(str_byte)
    return str_decode.decode('UTF-8')
