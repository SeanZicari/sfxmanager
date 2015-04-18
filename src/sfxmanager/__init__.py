import zmq


class SFXManager(object):
    """
    This is the client that manages all available sound servers.
    """

    def __init__(self):
        self._context = zmq.Context()

if __name__ == '__main__':
    SFXManager()