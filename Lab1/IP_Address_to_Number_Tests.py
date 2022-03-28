import unittest
from IP_Address_to_Number import  IP_Address_to_Number_Solution

class Test_IP_Address_to_Number_Solution(unittest.TestCase):
    def setUp(self):
        self.iptn = IP_Address_to_Number_Solution()

    #ipToNum tests
    def test_ip_to_num_normal_input(self):
        self.assertEqual(self.iptn.ipToNum('0.0.0.0'), 0, "Inputed value's ('0.0.0.0') result doesn't match with correct result ( 0 )")
        self.assertEqual(self.iptn.ipToNum('255.255.255.254'), 2 ** 32 - 2, "Inputed value's ('255.255.255.254') result doesn't match with correct result ( 4294967294 )")
        self.assertEqual(self.iptn.ipToNum('192.168.1.1'), 3232235777, "Inputed value's ('192.168.1.1') result doesn't match with correct result ( 3232235777 )")

    def test_ip_to_num_negative_octets_values(self):
        self.assertEqual(self.iptn.ipToNum('-10.255.255.255'), "ValueError: Some octet has no digit symbol", "The program works with negative first octet")
        self.assertEqual(self.iptn.ipToNum('255.-10.255.255'), "ValueError: Some octet has no digit symbol", "The program works with negative second octet")
        self.assertEqual(self.iptn.ipToNum('255.255.-10.255'), "ValueError: Some octet has no digit symbol", "The program works with negative third octet")
        self.assertEqual(self.iptn.ipToNum('255.255.255.-10'), "ValueError: Some octet has no digit symbol", "The program works with negative fourth octet")
        self.assertEqual(self.iptn.ipToNum('-10.-10.-10.-10'), "ValueError: Some octet has no digit symbol", "The program works with several negative octets")

    def test_ip_to_num_octets_values_more_than_limit(self):
        self.assertEqual(self.iptn.ipToNum('255.255.255.255'), 4294967295, "Inputed value's ('255.255.255.255') result doesn't match with correct result ( 4294967295 )")
        self.assertEqual(self.iptn.ipToNum('256.255.255.255'), "ValueError: Some octets' values is very big", "The program works with incorrect first octet's value which is more than limit(255)")
        self.assertEqual(self.iptn.ipToNum('255.256.255.255'), "ValueError: Some octets' values is very big", "The program works with incorrect second octet's value which is more than limit(255)")
        self.assertEqual(self.iptn.ipToNum('255.255.256.255'), "ValueError: Some octets' values is very big", "The program works with incorrect third octet's value which is more than limit(255)")
        self.assertEqual(self.iptn.ipToNum('255.255.255.256'), "ValueError: Some octets' values is very big", "The program works with incorrect fourth octet's value which is more than limit(255)")
        self.assertEqual(self.iptn.ipToNum('256.256.256.256'), "ValueError: Some octets' values is very big", "The program works with incorrect with several octets' values which is more than limit(255)")

    def test_ip_to_num_octets_values_less_than_limit(self):
        self.assertEqual(self.iptn.ipToNum('0.0.0.0'), 0, "Inputed value's ('0.0.0.0') result doesn't match with correct result ( 0 )")
        self.assertEqual(self.iptn.ipToNum('-1.0.0.0'), "ValueError: Some octet has no digit symbol", "The program works with incorrect first octet's value which is less than limit(0)")
        self.assertEqual(self.iptn.ipToNum('0.-1.0.0'), "ValueError: Some octet has no digit symbol", "The program works with incorrect second octet's value which is less than limit(0)")
        self.assertEqual(self.iptn.ipToNum('0.0.-1.0'), "ValueError: Some octet has no digit symbol", "The program works with incorrect third octet's value which is less than limit(0)")
        self.assertEqual(self.iptn.ipToNum('0.0.0.-1'), "ValueError: Some octet has no digit symbol", "The program works with incorrect fourth octet's value which is less than limit(0)")
        self.assertEqual(self.iptn.ipToNum('-1.-1.-1.-1'), "ValueError: Some octet has no digit symbol", "The program works with incorrect several octets' values which is less than limit(0)")

    def test_ip_to_num_incorrect_input_of_correct_data(self):
        self.assertEqual(self.iptn.ipToNum(' 1 . 1 . 1 . 1 '), "ValueError: Some octet has no digit symbol", "The program works with incorrectly entered values")
        self.assertEqual(self.iptn.ipToNum(' 10.10.10.10 '), "ValueError: Some octet has no digit symbol", "The program works with incorrectly entered values")
        self.assertEqual(self.iptn.ipToNum('1 . 1 . 1 . 1'), "ValueError: Some octet has no digit symbol", "The program works with incorrectly entered values")

    def test_ip_to_num_wrong_type_input(self):
        self.assertEqual(self.iptn.ipToNum(2 ** 32 - 1), "TypeError: type is not string", "The program is being used with <int> data type (instead of <string>)")
        self.assertEqual(self.iptn.ipToNum([255, 255, 255, 255]), "TypeError: type is not string", "The program is being used with <list> data type (instead of <string>)")
        self.assertEqual(self.iptn.ipToNum((10, 1, 4, 15)), "TypeError: type is not string", "The program is being used with <set> data type (instead of <string>)")

    def test_ip_to_num_wrong_string_length(self):
        self.assertEqual(self.iptn.ipToNum('.1.1.1'), "LengthError: min string length is 7 symbols", "The program works with a string less than the minimum possible length")
        self.assertEqual(self.iptn.ipToNum('255.255.255.255 '), "LengthError: max string length is 15 symbols", "The program works with a string larger than the maximum possible length")

    def test_ip_to_num_bytes_values_out_of_range_input(self):
        self.assertEqual(self.iptn.ipToNum('1000.0.0.0'), "ValueError: Some octets' values is very big", "The program works with too large octet values")
        self.assertEqual(self.iptn.ipToNum('-55.56.-55.55'), "ValueError: Some octet has no digit symbol", "The program works with negative octet values")

    def test_ip_to_num_bytes_with_no_digit_symbols_input(self):
        self.assertEqual(self.iptn.ipToNum('1+1.1+1.1+1.1+1'), "ValueError: Some octet has no digit symbol", "The program works with octets with non-numeric characters")
        self.assertEqual(self.iptn.ipToNum('(-0./20|.%0.^,1'), "ValueError: Some octet has no digit symbol", "The program works with octets with non-numeric characters")
        self.assertEqual(self.iptn.ipToNum('abc.def.jhg.klm'), "ValueError: Some octet has no digit symbol", "The program works with literal octet values")

    def test_ip_to_num_with_dots_wrong_order(self):
        self.assertEqual(self.iptn.ipToNum('255255255255...'), "ValueError: Some octet has no digit symbol", "The program works with the wrong order of points")
        self.assertEqual(self.iptn.ipToNum('...1010'), "ValueError: Some octet has no digit symbol", "The program works with the wrong order of points")
        self.assertEqual(self.iptn.ipToNum('..111.1'), "ValueError: Some octet has no digit symbol", "The program works with the wrong order of points")
        self.assertEqual(self.iptn.ipToNum('.111.1.'), "ValueError: Some octet has no digit symbol", "The program works with the wrong order of points")

    def test_ip_to_num_wrong_dots_amount_input(self):
        self.assertEqual(self.iptn.ipToNum('255255255255'), "ValueError: you inputed not IPv4", "The program works with incorrect IP address partitioning (received 1 octets instead of 4)")
        self.assertEqual(self.iptn.ipToNum('255255.255255'), "ValueError: you inputed not IPv4", "The program works with incorrect IP address partitioning (received 2 octets instead of 4)")
        self.assertEqual(self.iptn.ipToNum('255.255.255255'), "ValueError: you inputed not IPv4", "The program works with incorrect IP address partitioning (received 3 octets instead of 4)")
        self.assertEqual(self.iptn.ipToNum('25.525.5.5.5'), "ValueError: you inputed not IPv4", "The program works with incorrect IP address partitioning (received more than 4 octets)")


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
