import unittest
from IP_Address_to_Number import  IP_Address_to_Number_Solution

class Test_IP_Address_to_Number_Solution(unittest.TestCase):
    def setUp(self):
        self.iptn = IP_Address_to_Number_Solution()

    #ipToNum tests
    def test_ip_to_num_normal_input(self):
        self.assertEqual(self.iptn.ipToNum('0.0.0.0'), 0, "Values are calculated incorrectly")
        self.assertEqual(self.iptn.ipToNum('255.255.255.255'), 2 ** 32 - 1, "Values are calculated incorrectly")
        self.assertEqual(self.iptn.ipToNum('192.168.1.1'), 3232235777, "Values are calculated incorrectly")

    def test_ip_to_num_incorrect_input_of_correct_data(self):
        self.assertEqual(self.iptn.ipToNum(' 1 . 1 . 1 . 1 '), "ValueError: Some byte has no digit symbol", "The program works with incorrectly entered values")
        self.assertEqual(self.iptn.ipToNum(' 10.10.10.10 '), "ValueError: Some byte has no digit symbol", "The program works with incorrectly entered values")
        self.assertEqual(self.iptn.ipToNum('1 . 1 . 1 . 1'), "ValueError: Some byte has no digit symbol", "The program works with incorrectly entered values")

    def test_ip_to_num_wrong_type_input(self):
        self.assertEqual(self.iptn.ipToNum(2 ** 32 - 1), "TypeError: type is not string", "The program is being used with <int> data type (instead of <string>)")
        self.assertEqual(self.iptn.ipToNum([255, 255, 255, 255]), "TypeError: type is not string", "The program is being used with <list> data type (instead of <string>)")
        self.assertEqual(self.iptn.ipToNum((10, 1, 4, 15)), "TypeError: type is not string", "The program is being used with <set> data type (instead of <string>)")

    def test_ip_to_num_wrong_string_length(self):
        self.assertEqual(self.iptn.ipToNum('.1.1.1'), "LengthError: min string length is 7 symbols", "The program works with a string less than the minimum possible length")
        self.assertEqual(self.iptn.ipToNum('255.255.255.255 '), "LengthError: max string length is 15 symbols", "The program works with a string larger than the maximum possible length")

    def test_ip_to_num_bytes_values_out_of_range_input(self):
        self.assertEqual(self.iptn.ipToNum('1000.0.0.0'), "ValueError: Some bytes' values is very big", "The program works with too large byte values")
        self.assertEqual(self.iptn.ipToNum('-55.56.-55.55'), "ValueError: Some byte has no digit symbol", "The program works with negative byte values")

    def test_ip_to_num_bytes_with_no_digit_symbols_input(self):
        self.assertEqual(self.iptn.ipToNum('1+1.1+1.1+1.1+1'), "ValueError: Some byte has no digit symbol", "The program works with bytes with non-numeric characters")
        self.assertEqual(self.iptn.ipToNum('(-0./20|.%0.^,1'), "ValueError: Some byte has no digit symbol", "The program works with bytes with non-numeric characters")
        self.assertEqual(self.iptn.ipToNum('abc.def.jhg.klm'), "ValueError: Some byte has no digit symbol", "The program works with literal byte values")

    def test_ip_to_num_with_dots_wrong_order(self):
        self.assertEqual(self.iptn.ipToNum('255255255255...'), "ValueError: Some byte has no digit symbol", "The program works with the wrong order of points")
        self.assertEqual(self.iptn.ipToNum('...1010'), "ValueError: Some byte has no digit symbol", "The program works with the wrong order of points")
        self.assertEqual(self.iptn.ipToNum('..111.1'), "ValueError: Some byte has no digit symbol", "The program works with the wrong order of points")
        self.assertEqual(self.iptn.ipToNum('.111.1.'), "ValueError: Some byte has no digit symbol", "The program works with the wrong order of points")

    def test_ip_to_num_wrong_dots_amount_input(self):
        self.assertEqual(self.iptn.ipToNum('255255255255'), "ValueError: you inputed not IPv4", "The program works with incorrect IP address partitioning (received 1 bytes instead of 4)")
        self.assertEqual(self.iptn.ipToNum('255255.255255'), "ValueError: you inputed not IPv4", "The program works with incorrect IP address partitioning (received 2 bytes instead of 4)")
        self.assertEqual(self.iptn.ipToNum('255.255.255255'), "ValueError: you inputed not IPv4", "The program works with incorrect IP address partitioning (received 3 bytes instead of 4)")
        self.assertEqual(self.iptn.ipToNum('25.525.5.5.5'), "ValueError: you inputed not IPv4", "The program works with incorrect IP address partitioning (received more than 4 bytes)")


    #numToIp tests
    def test_num_to_ip_normal_input(self):
        self.assertEqual(self.iptn.numToIp(0), '0.0.0.0', "Values are calculated incorrectly")
        self.assertEqual(self.iptn.numToIp(2 ** 32 - 1), '255.255.255.255', "Values are calculated incorrectly")
        self.assertEqual(self.iptn.numToIp(3232235777), '192.168.1.1', "Values are calculated incorrectly")

    def test_num_to_ip_wrong_type_input(self):
        self.assertEqual(self.iptn.numToIp('3232235777'), "TypeError: type is not integer", "The program is being used with the wrong data type")
        self.assertEqual(self.iptn.numToIp(3232235777.0), "TypeError: type is not integer", "The program is being used with the wrong data type")
        self.assertEqual(self.iptn.numToIp([3232235777]), "TypeError: type is not integer", "The program is being used with the wrong data type")


    def test_num_to_ip_out_of_range_input(self):
        self.assertEqual(self.iptn.numToIp(2 ** 33), "ValueError: IPv4 cannot be more then 4294967295", "Using a program with a number greater than the maximum")
        self.assertEqual(self.iptn.numToIp(-1), "ValueError: IPv4 cannot be less then zero", "Using a program with a number less than the minimum")

if __name__ == "__main__":
  unittest.main()





