import unittest
import socket
import threading
from netdog.server.server import start_tcp_server, start_udp_server
from netdog.client.client import start_tcp_client, start_udp_client


class TestTCPClient(unittest.TestCase):
    def setUp(self):
        self.host = '127.0.0.1'
        self.port = 9999
        self.server_thread = threading.Thread(target=start_tcp_server, args=(self.host, self.port))
        self.server_thread.daemon = True
        self.server_thread.start()
    def test_tcp_client_connection(self):
        client_thread = threading.Thread(target=start_tcp_client, args=(self.host, self.port))
        client_thread.start()
        client_thread.join()


class TestUDPClient(unittest.TestCase):
    def setUp(self):
        self.host = '127.0.0.1'
        self.port = 9999
        self.server_thread = threading.Thread(target=start_udp_server, args=(self.host, self.port))
        self.server_thread.daemon = True
        self.server_thread.start()
    def test_udp_client_connection(self):
        client_thread = threading.Thread(target=start_udp_client, args=(self.host, self.port))
        client_thread.start()
        client_thread.join()


if __name__ == '__main__':
    unittest.main()