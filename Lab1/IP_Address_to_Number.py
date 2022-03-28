class IP_Address_to_Number_Solution:
    def __init__(self):
        pass

    def ipToNum(self, str_ip):

        if not isinstance(str_ip, str):
            return "TypeError: type is not string"
        if len(str_ip) > 15:
            return "LengthError: max string length is 15 symbols"
        if len(str_ip) < 7:
            return "LengthError: min string length is 7 symbols"
        str_ip = str_ip.split('.')
        if len(str_ip) != 4:
            return "ValueError: you inputed not IPv4"
        if ( not str_ip[0].isdecimal() or not str_ip[1].isdecimal() or not str_ip[2].isdecimal() or not str_ip[3].isdecimal()):
            return "ValueError: Some octet has no digit symbol"
        if ( int(str_ip[0]) > 255 or int(str_ip[1]) > 255 or int(str_ip[2]) > 255 or int(str_ip[3]) > 255 ):
            return "ValueError: Some octets' values is very big"
        bin_line = bin( int(str_ip[0]) )[2:].zfill(8) + bin( int(str_ip[1]) )[2:].zfill(8) + bin( int(str_ip[2]) )[2:].zfill(8) + bin( int(str_ip[3]) )[2:].zfill(8)
        return (int(bin_line, 2))

    def numToIp(self, int_ip):
        if not isinstance(int_ip, int):
            return "TypeError: type is not integer"
        if int_ip < 0:
            return "ValueError: IPv4 cannot be less then zero"
        if int_ip > 4294967295:
            return "ValueError: IPv4 cannot be more then 4294967295"
        bin_line = bin(int_ip)[2:].zfill(32)
        octet4 = bin_line[-8:]
        octet3 = bin_line[-16:-8]
        octet2 = bin_line[-24:-16]
        octet1 = bin_line[-32:-24]
        ip_address = ".".join([ str(int(octet1, 2)), str(int(octet2, 2)), str(int(octet3, 2)), str(int(octet4, 2)), ])
        return (ip_address)
