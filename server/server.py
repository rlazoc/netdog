import socket
import logging

def start_server(host, port):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen(1)
            logging.info(f"Listening on {host}:{port}")

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
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    start_server('0.0.0.0', 9999)