import socket


def run_tcp_listener(host='0.0.0.0', port=500):
    """
    Starts a tcp listener thread
    :param host: by default running on localhost
    :param port: by default listening to port 500
    :return:
    """
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)

        print(f"Server listening on {host}:{port}...")

        while True:
            # Accept a client connection
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Connected to {client_address}")
                while True:
                    # Set buffer size to 1024 bytes
                    data = client_socket.recv(1024)
                    if not data:
                        break

                    print(f"Incoming: {data.decode().strip()}")
