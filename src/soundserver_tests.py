import unittest

import zmq

from soundserver import SoundServer, CONTROL_PORT


class SoundServerTests(unittest.TestCase):

    def test_sound_server_creates_control_port(self):
        # This step creates the control port
        server = SoundServer()

        # Attempt to connect to the control port
        ctx = zmq.Context()
        socket = ctx.socket(zmq.REQ)
        socket.connect('tcp://localhost:{0}'.format(CONTROL_PORT))
        socket.rcvtimeo = 1

        # ZMQ connections do not fail when the other end doesn't exist - need
        # to actually receive a response to verify all is well
        socket.send(b'ping')
        self.assertRaises(zmq.error.Again, socket.recv())


if __name__ == '__main__':
    unittest.main()