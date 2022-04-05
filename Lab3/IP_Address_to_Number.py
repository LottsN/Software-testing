import psycopg2

class TypeErrorInt(Exception):
    """TypeErrorInt: type is not integer"""
    pass

class ValueLessThanZeroError(Exception):
    """ValueLessThanZeroError: IPv4 cannot be less then zero"""
    pass

class ValueMoreThanLimitError(Exception):
    """ValueMoreThanLimitError: IPv4 cannot be more then 4294967295"""
    pass

class TypeErrorStr(Exception):
    """TypeErrorStr: type is not integer"""
    pass

class LengthErrorMin(Exception):
    """LengthErrorMin: min string length is 7 symbols"""
    pass

class LengthErrorMax(Exception):
    """LengthErrorMax: max string length is 15 symbols"""
    pass

class NotIPv4Error(Exception):
    """NotIPv4Error: you inputed not IPv4"""
    pass

class NoDigitSymbolError(Exception):
    """NoDigitSymbolError: Some octet has no digit symbol"""
    pass

class TooBigOctetsError(Exception):
    """TooBigOctetsError: Some octets' values is very big"""
    pass



class IP_Address_to_Number_Solution:
    def __init__(self, host, database, user, password):
        self.conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password)
        self.cur = self.conn.cursor()

    def ipToNum(self, str_ip):
        if not isinstance(str_ip, str):
            return TypeErrorStr
        if len(str_ip) > 15:
            return LengthErrorMax
        if len(str_ip) < 7:
            return LengthErrorMin
        # check if value in database
        self.cur.execute(f"SELECT * FROM ipn_results WHERE value='{str_ip}' ")
        if (self.cur.rowcount == 1):
            return (self.cur.fetchone()[1])
        value = str_ip[:]
        str_ip = str_ip.split('.')
        if len(str_ip) != 4:
            return NotIPv4Error
        if ( not str_ip[0].isdecimal() or not str_ip[1].isdecimal() or not str_ip[2].isdecimal() or not str_ip[3].isdecimal()):
            return NoDigitSymbolError
        if ( int(str_ip[0]) > 255 or int(str_ip[1]) > 255 or int(str_ip[2]) > 255 or int(str_ip[3]) > 255 ):
            return TooBigOctetsError
        bin_line = bin( int(str_ip[0]) )[2:].zfill(8) + bin( int(str_ip[1]) )[2:].zfill(8) + bin( int(str_ip[2]) )[2:].zfill(8) + bin( int(str_ip[3]) )[2:].zfill(8)
        result = int(bin_line, 2)

        # insert value if it is not in database
        if (self.cur.rowcount != 1 and self.cur.rowcount < 2):
            sql = "INSERT INTO ipn_results (value, result) VALUES (%s, %s)"
            val = (value, result)
            self.cur.execute(sql, val)
            self.conn.commit()

        return (result)

    def numToIp(self, int_ip):
        if not isinstance(int_ip, int):
            return TypeErrorInt
        if int_ip < 0:
            return ValueLessThanZeroError
        if int_ip > 4294967295:
            return ValueMoreThanLimitError
        # check if value in database
        self.cur.execute(f"SELECT * FROM nip_results WHERE value='{int_ip}' ")
        if (self.cur.rowcount == 1):
            return (self.cur.fetchone()[1])
        bin_line = bin(int_ip)[2:].zfill(32)
        octet4 = bin_line[-8:]
        octet3 = bin_line[-16:-8]
        octet2 = bin_line[-24:-16]
        octet1 = bin_line[-32:-24]
        ip_address = ".".join([ str(int(octet1, 2)), str(int(octet2, 2)), str(int(octet3, 2)), str(int(octet4, 2)), ])

        # insert value if it is not in database
        if (self.cur.rowcount != 1 and self.cur.rowcount < 2):
            sql = "INSERT INTO nip_results (value, result) VALUES (%s, %s)"
            val = (int_ip, ip_address)
            self.cur.execute(sql, val)
            self.conn.commit()

        return (ip_address)

