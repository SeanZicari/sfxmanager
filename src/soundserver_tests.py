import unittest
from multiprocessing import Process

import zmq

from soundserver.server import SoundServer, CONTROL_PORT


class SoundServerTests(unittest.TestCase):

    def setUp(self):
        self._p = Process(target=self._start_soundserver)
        self._p.start()

        # Attempt to connect to the control port
        self._ctx = zmq.Context()
        self._socket = self._ctx.socket(zmq.REQ)
        self._socket.connect('tcp://127.0.0.1:{0}'.format(CONTROL_PORT))

    def tearDown(self):
        self._p.terminate()
        self._p = None

    def test_sound_server_creates_control_port(self):

        # ZMQ connections do not fail when the other end doesn't exist - need
        # to actually receive a response to verify all is well
        self._socket.send_string('hi')
        self.assertEqual(self._socket.recv_string(), "sup?")

    def _start_soundserver(self):
        server = SoundServer()
        server.start()


if __name__ == '__main__':
    unittest.main()