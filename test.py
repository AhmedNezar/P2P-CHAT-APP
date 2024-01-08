import io
import itertools
import socket
import sys
import pytest
from peer import peerMain
from peer import PeerClient
import unittest
from unittest.mock import Mock, patch, MagicMock


class TestPeerMain(unittest.TestCase):
    @patch('pwinput.pwinput', side_effect=itertools.repeat('Password-1'))
    @patch('builtins.input', return_value='username1')
    def test_create_account_success(self, mock_input, mock_pwinput):
        # Arrange
        peer = peerMain()
        peer.tcpClientSocket = MagicMock()
        peer.tcpClientSocket.recv.return_value = b'join-success'
        capturedOutput = io.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput             # Redirect stdout.

        # Act
        peer.createAccount(username='username1', password='Password-1')

        # Assert
        sys.stdout = sys.__stdout__            # Reset redirect.
        self.assertTrue("Account created..." in capturedOutput.getvalue())

    @patch('pwinput.pwinput', side_effect=itertools.repeat('Password-1'))
    @patch('builtins.input', return_value='username1')
    def test_create_account_exist(self, mock_input, mock_pwinput):
        # Arrange
        peer = peerMain()
        peer.tcpClientSocket = MagicMock()
        peer.tcpClientSocket.recv.return_value = b'join-exist'
        capturedOutput = io.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput             # Redirect stdout.

        # Act
        peer.createAccount(username='username1', password='Password-1')

        # Assert
        sys.stdout = sys.__stdout__             # Reset redirect.
        # assert the printed output
        self.assertTrue(
            "choose another username or login..." in capturedOutput.getvalue())

    def setUp(self):
        self.peer = peerMain()
        self.mock_socket = MagicMock()
        self.peer.tcpClientSocket = self.mock_socket
        # self.peer.tcpClientSocket = MagicMock()

    def test_login_success(self):
        # Arrange
        self.peer.tcpClientSocket.recv.return_value = b'login-success'
        capturedOutput = io.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput             # Redirect stdout.

        # Act
        result = self.peer.login('username1', 'Password-1', 12345)

        # Assert
        sys.stdout = sys.__stdout__             # Reset redirect.
        self.assertEqual(result, 1)
        # assert the printed output
        self.assertTrue(
            "Logged in successfully..." in capturedOutput.getvalue())

    def test_login_account_not_exist(self):
        # Arrange
        self.peer.tcpClientSocket.recv.return_value = b'login-account-not-exist'
        capturedOutput = io.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput             # Redirect stdout.

        # Act
        result = self.peer.login('username1', 'Password-1', 12345)

        # Assert
        sys.stdout = sys.__stdout__             # Reset redirect.
        self.assertEqual(result, 0)
        # assert the printed output
        self.assertTrue(
            "Account does not exist..." in capturedOutput.getvalue())

    def test_logout_option_1(self):
        # Arrange
        self.peer.loginCredentials = ['username1', 'Password-1']
        self.peer.timer = MagicMock()
        # Create a second mock object for the new socket instance
        new_socket_instance = MagicMock()
        self.peer.tcpClientSocket.connect.side_effect = [
            None, new_socket_instance]  # Set the side effect of connect
        # Act
        self.peer.logout(1)

        # Print method calls
        # print(self.mock_socket.mock_calls)

        # Assert
        self.mock_socket.send.assert_called_once_with(
            "LOGOUT username1".encode())
        # self.assertEqual(self.peer.tcpClientSocket.send.call_count, 1)

    def test_logout_option_other(self):
        # Arrange
        self.peer.loginCredentials = ['username1', 'Password-1']
        # Create a second mock object for the new socket instance
        new_socket_instance = MagicMock()
        self.peer.tcpClientSocket.connect.side_effect = [
            None, new_socket_instance]  # Set the side effect of connect

        # Act
        self.peer.logout(0)

        # Assert
        self.mock_socket.send.assert_called_once_with("LOGOUT".encode())

    def test_user_search_not_found(self):
        with patch('builtins.input', return_value='username2') as mock_input:
            # Arrange
            self.peer.loginCredentials = ['username1', 'Password-1']
            self.mock_socket.recv.return_value = b'search-user-not-found'
            capturedOutput = io.StringIO()          # Create StringIO object
            sys.stdout = capturedOutput             # Redirect stdout.

            # Act
            self.peer.searchUser(username='username2')

            # Assert
            sys.stdout = sys.__stdout__             # Reset redirect.
            self.mock_socket.send.assert_called_once_with(
                "SEARCH username2".encode())
            self.assertTrue(
                "username2 is not found" in capturedOutput.getvalue())

    def test_user_search_not_online(self):
        with patch('builtins.input', return_value='username2') as mock_input:
            # Arrange
            self.peer.loginCredentials = ['username1', 'Password-1']
            self.mock_socket.recv.return_value = b'search-user-not-online'
            capturedOutput = io.StringIO()          # Create StringIO object
            sys.stdout = capturedOutput             # Redirect stdout.

            # Act
            self.peer.searchUser(username='username2')

            # Assert
            sys.stdout = sys.__stdout__             # Reset redirect.
            self.mock_socket.send.assert_called_once_with(
                "SEARCH username2".encode())
            self.assertTrue(
                "username2 is not online..." in capturedOutput.getvalue())

    def test_user_search_found(self):
        with patch('builtins.input', return_value='username2') as mock_input:
            # Arrange
            self.peer.loginCredentials = ['username1', 'Password-1']
            self.mock_socket.recv.return_value = b'search-success 192.168.1.1'
            capturedOutput = io.StringIO()          # Create StringIO object
            sys.stdout = capturedOutput             # Redirect stdout.

            # Act
            self.peer.searchUser(username='username2')

            # Assert
            sys.stdout = sys.__stdout__             # Reset redirect.
            self.mock_socket.send.assert_called_once_with(
                "SEARCH username2".encode())
            self.assertTrue(
                "username2 is found successfully..." in capturedOutput.getvalue())

    def test_rooms_List_found(self):
        # Arrange
        self.mock_socket.recv.return_value = b'Available rooms: room1 room2'
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        # Act
        self.peer.roomList()

        # Assert
        sys.stdout = sys.__stdout__
        self.mock_socket.send.assert_called_once_with(
            "ROOM-LIST".encode())  # Adjust the expected message
        self.assertTrue(
            "Available rooms: room1 room2\n" in capturedOutput.getvalue())

    def test_rooms_List_not_found(self):
        # Arrange
        self.mock_socket.recv.return_value = b'no-rooms'
        capturedOutput = io.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput             # Redirect stdout.

        # Act
        self.peer.roomList()

        # Assert
        sys.stdout = sys.__stdout__             # Reset redirect.
        # Ensure that no call to send was made in this case
        self.assertTrue("no-rooms\n" in capturedOutput.getvalue())

    def test_user_createRoom_success(self):
        with patch.object(self.peer.tcpClientSocket, 'recv', return_value=b'create-room-success'):
            # Arrange
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput

            # Act
            self.peer.createRoom(roomId='roomID')

            # Assert
            sys.stdout = sys.stdout  # Reset redirect.
            print("Captured Output:", repr(capturedOutput.getvalue()))
            assert 'Chat room created successfully' in capturedOutput.getvalue()

    def test_user_createRoom_exists(self):
        with patch.object(self.peer.tcpClientSocket, 'recv', return_value=b'chat-room-exist'):
            # Arrange
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput

            # Act
            self.peer.createRoom(roomId='roomID')

            # Assert
            sys.stdout = sys.stdout  # Reset redirect.
            assert 'Chat room already exits\n' in capturedOutput.getvalue()

    def test_user_joinRoom_success(self):
        with patch('builtins.input', side_effect=['roomName', 'roomID']), \
                patch.object(self.peer.tcpClientSocket, 'recv', return_value=b'join-room-success'):
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            self.peer.joinRoom(roomId='roomID')
            sys.stdout = sys.__stdout__
            assert "join-room-success\nroomID is joined successfully" in capturedOutput.getvalue()

    def test_user_joinRoom_not_exist(self):
        with patch('builtins.input', side_effect=['roomName', 'roomID']), \
                patch.object(self.peer.tcpClientSocket, 'recv', return_value=b'join-room-fail'):
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            self.peer.joinRoom(roomId='roomID')
            sys.stdout = sys.__stdout__
            assert "join-room-fail" in capturedOutput.getvalue()

    def test_user_leaveRoom_success(self):
        with patch.object(self.peer.tcpClientSocket, 'recv', return_value=b'leave-room-success'):
            # Arrange
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput

            # Act
            self.peer.leaveRoom(roomid='roomID')

            # Assert
            sys.stdout = sys.stdout  # Reset redirect.

            assert 'You have left the room\n' in capturedOutput.getvalue()

    def test_sendHelloMessage(self):
        # Arrange
        self.peer.loginCredentials = ['username1', 'Password-1']
        mock_socket = MagicMock()
        self.peer.udpClientSocket = mock_socket

        # Act
        self.peer.sendHelloMessage()

        # Let the sendHelloMessage run for some time
        # time.sleep(2)
        # Stop the timer
        self.peer.timer.cancel()

        # Assert
        mock_socket.sendto.assert_called_with("HELLO username1".encode(
        ), (self.peer.registryName, self.peer.registryUDPPort))

    def test_bold_text(self):
        message = "*Hello, World!*"
        expected_output = '\033[1mHello, World!\033[0m'
        self.assertEqual(peerMain.format_message(message), expected_output)

    def test_italic_text(self):
        message = "_Hello, World!_"
        expected_output = '\033[3mHello, World!\033[0m'
        self.assertEqual(peerMain.format_message(message), expected_output)


if __name__ == '__main__':
    unittest.main()
