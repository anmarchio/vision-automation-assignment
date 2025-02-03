import unittest
from unittest.mock import patch, MagicMock

from endpoints.tcp_listener import run_tcp_listener


class TestTcpListener(unittest.TestCase):

    @patch("endpoints.tcp_listener.socket.socket")
    def test_tcp_listener_receives_data(self, mock_socket_class):
        # Mock socket instance
        mock_socket_instance = MagicMock()
        mock_socket_class.return_value = mock_socket_instance

        mock_conn = MagicMock()
        mock_socket_instance.accept.return_value = (mock_conn, ("127.0.0.1", 5000))

        mock_conn.recv.return_value = b'Test data'

        with patch("endpoints.tcp_listener.fi_confidence") as mock_process_data:
            mock_process_data.return_value = "Data processed"

            run_tcp_listener("127.0.0.1", 550)

            # Assert that the connection was accepted and data was received
            mock_socket_instance.bind.assert_called_with(("127.0.0.1", 550))
            mock_socket_instance.listen.assert_called_once()
            mock_conn.recv.assert_called_once()

            # Check if data processing function was called
            mock_process_data.assert_called_with(b'Test data')

    @patch("endpoints.tcp_listener.socket.socket")
    def test_tcp_listener_no_data_received(self, mock_socket_class):
        # Mock socket instance
        mock_socket_instance = MagicMock()
        mock_socket_class.return_value = mock_socket_instance

        # Simulate incoming connection
        mock_conn = MagicMock()
        mock_socket_instance.accept.return_value = (mock_conn, ("127.0.0.1", 550))

        # Simulate no data received
        mock_conn.recv.return_value = b''

        with patch("endpoints.tcp_listener.fi_confidence") as mock_process_data:
            run_tcp_listener("127.0.0.1", 550)

            mock_process_data.assert_not_called()


if __name__ == "__main__":
    unittest.main()
