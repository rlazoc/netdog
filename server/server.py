import socket
import logging
import threading

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
    host, port = '0.0.0.0', 9999
    tcp_thread = threading.Thread(target=start_tcp_server, args=(host, port))
    udp_thread = threading.Thread(target=start_udp_server, args=(host, port))
    tcp_thread.start()
    udp_thread.start()
    tcp_thread.join()
    udp_thread.join()