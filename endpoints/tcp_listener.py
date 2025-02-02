import socket

# Server configuration
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 500  # Port number to listen on

def run_tcp_listener():
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)  # Allow 1 client connection

        print(f"Server listening on {HOST}:{PORT}...")

        while True:
            # Accept a client connection
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Connected by {client_address}")
                while True:
                    # Receive data from the client
                    data = client_socket.recv(1024)  # Buffer size of 1024 bytes
                    if not data:
                        break
                    # Decode and display the received data
                    print(f"Received: {data.decode().strip()}")
