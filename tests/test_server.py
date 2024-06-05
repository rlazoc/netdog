import unittest
import socket
import threading
from netdog.server.server import start_tcp_server, start_udp_server


class TestTCPServer(unittest.TestCase):
    def setUp(self):
        self.host = '127.0.0.1'
        self.port = 9999
        self.server_thread = threading.Thread(target=start_tcp_server, args=(self.host, self.port))
        self.server_thread.daemon = True
        self.server_thread.start()
    def test_tcp_server_connection(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            client_socket.sendall(b'Hello, Server')
            data = client_socket.recv(1024)
            self.assertEqual(data, b'Hello, Server')


class TestUDPServer(unittest.TestCase):
    def setUp(self):
        self.host = '127.0.0.1'
        self.port = 9999
        self.server_thread = threading.Thread(target=start_udp_server, args=(self.host, self.port))
        self.server_thread.daemon = True
        self.server_thread.start()
    def test_udp_server_connection(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
            client_socket.sendto(b'Hello, Server', (self.host, self.port))
            data, _ = client_socket.recvfrom(1024)
            self.assertEqual(data, b'Hello, Server')


if __name__ == '__main__':
    unittest.main()