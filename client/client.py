import socket
import logging

def start_client(host, port):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            print(f"Connected to {host}:{port}")

            while True:
                message = input('Enter message: ')
                if message.lower() == 'exit':
                    break
                client_socket.sendall(message.encode('utf-8'))
                data = client_socket.recv(1024)
                print(f"Received: {data.decode('utf-8')}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    start_client('127.0.0.1', 9999)