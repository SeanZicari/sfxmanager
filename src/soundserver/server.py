import sys

import zmq
from zmq.eventloop import IOLoop
from zmq.eventloop.zmqstream import ZMQStream


CONTROL_PORT = 5600


class SoundServer(object):

    def __init__(self):
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.REP)
        self._socket.bind('tcp://127.0.0.1:{0}'.format(CONTROL_PORT))
        self._stream = ZMQStream(self._socket)
        self._stream.on_recv(self._handle_msg)

    def start(self):
        IOLoop.instance().start()

    def _handle_msg(self, msg):
        method = '_handler_{0}'.format(msg[0].decode("utf-8"))

        try:
            print("Trying method {0}".format(method))
            getattr(self, method)()
        except AttributeError:
            sys.exit(1)

    def _handler_hi(self):
        self._socket.send_string('sup?')

    def _handler_exit(self):
        pass


if __name__ == '__main__':
    SoundServer().start()
