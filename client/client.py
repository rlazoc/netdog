import socket
import logging


def start_tcp_client(host, port):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            logging.info(f"Connected to TCP server at {host}:{port}")

            while True:
                message = input("Enter message: ")
                if message.lower() == 'exit':
                    break
                client_socket.sendall(message.encode('utf-8'))
                data = client_socket.recv(1024)
                logging.info(f"Received: {data.decode('utf-8')}")
    except Exception as e:
        logging.error(f"An error occurred in TCP client: {e}")


def start_udp_client(host, port):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
            logging.info(f"Connected to UDP server at {host}:{port}")

            while True:
                message = input("Enter message: ")
                if message.lower() == 'exit':
                    break
                client_socket.sendto(message.encode('utf-8'), (host, port))
                data, _ = client_socket.recvfrom(1024)
                logging.info(f"Received: {data.decode('utf-8')}")
    except Exception as e:
        logging.error(f"An error occurred in UDP client: {e}")


if __name__ == "__main__":
    host, port = '127.0.0.1', 9999
    protocol = input("Choose protocol (TCP/UDP): ").strip().upper()
    if protocol == 'TCP':
        start_tcp_client(host, port)
    elif protocol == 'UDP':
        start_udp_client(host, port)
    else:
        print("Invalid protocol. Please choose either TCP or UDP.")