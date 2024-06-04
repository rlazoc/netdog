import socket
import logging
import threading
import argparse


def start_tcp_server(host, port):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen(1)
            logging.info(f"TCP Server listening on {host}:{port}...")

            conn, addr = server_socket.accept()
            with conn:
                logging.info(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    logging.info(f"Received: {data.decode('utf-8')}")
                    conn.sendall(data)
    except Exception as e:
        logging.error(f"An error occurred in TCP server: {e}")


def start_udp_server(host, port):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
            server_socket.bind((host, port))
            logging.info(f"UDP Server listening on {host}:{port}...")

            while True:
                data, addr = server_socket.recvfrom(1024)
                logging.info(f"Received from {addr}: {data.decode('utf-8')}")
                server_socket.sendto(data, addr)
    except Exception as e:
        logging.error(f"An error occurred in UDP server: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Netdog Server')
    parser.add_argument('--host', type=str, default='0.0.0.0', help='Host to bind the server')
    parser.add_argument('--port', type=int, default=9999, help='Port to bind the server')
    parser.add_argument('--protocol', type=str, choices=['TCP', 'UDP', 'BOTH'], default='BOTH', help='Protocol to use (TCP, UDP, or BOTH)')
    args = parser.parse_args()

    if args.protocol in ['TCP', 'BOTH']:
        tcp_thread = threading.Thread(target=start_tcp_server, args=(args.host, args.port))
        tcp_thread.start()
    if args.protocol in ['UDP', 'BOTH']:
        udp_thread = threading.Thread(target=start_udp_server, args=(args.host, args.port))
        udp_thread.start()
    if args.protocol == 'BOTH':
        tcp_thread.join()
        udp_thread.join()
    elif args.protocol == 'TCP':
        tcp_thread.join()
    elif args.protocol == 'UDP':
        udp_thread.join()