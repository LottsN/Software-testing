import socket
import psycopg2
from IP_Address_to_Number import IP_Address_to_Number_Solution

class HostError(Exception):
    """HostError: host is not found"""
    pass

class DatabaseError(Exception):
    """DatabaseError: database is not found"""
    pass

class DataProviderError(Exception):
    """DataProviderError: data provider is not exist"""
    pass

class MethodError(Exception):
    """MethodError: calling unexpected method"""
    pass

def send_user_request(funcName, data):

    # это функция, через которую будет оправлять введенные данные пользователя
    # здесь можно устанавливать нужные параметры отправки запроса
    # host = "site.ru"
    # database = "siteDB"
    # user = DataProvider.GetIdentity.Username
    # password = DataProvider.GetIdentity.Password

    host = "localhost"
    database = "softwareTestingDB"
    user = "user"
    password = "password"

    try:
        test_connection_to_database(host, database, user, password)
    except Exception as e:
        return f"There is error in connecting to database: + {str(e)}"
    else:
        iptn = IP_Address_to_Number_Solution(
            host,
            database,
            user,
            password
        )

    if funcName == "ipToNum":
        try:
            return iptn.ipToNum(data)
        except Exception as e:
            return f"There is error in converting from ip to num: + {str(e)}"
    elif funcName == "numToIp":
        try:
            return iptn.numToIp(int(data))
        except Exception as e:
            return f"There is error in converting from num to ip: + {str(e)}"
    else:
        return f"There is no such method"


def test_connection_to_database(host, database, user, password):
    # check if host exist
    if (not test_host_existing(host)):
        raise HostError

    # check if database exist
    if (not test_database_existing(host, database)):
        raise DatabaseError

    # check if user exist
    if (not test_data_provider_existing(host, database, user, password)):
        raise DataProviderError

    return 0


def test_host_existing(hostname):
    try:
        socket.gethostbyname(hostname)
        return 1
    except socket.error:
        return 0


def test_database_existing(host, database):
    try:
        conn = psycopg2.connect(
            host=host,
            database=database,
            user="test",
            password="test")
        conn.close()
        return 1
    except psycopg2.OperationalError:
        return 0


def test_data_provider_existing(host, database, user, password):
    try:
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password)
        conn.close()
        return 1
    except psycopg2.OperationalError:
        return 0