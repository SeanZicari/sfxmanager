SFXManager Server(s)
####################

There are as many servers as there are computers with available audio outputs.

A server provides a ``control`` socket (*port 5600*) for sending commands to
the server.

A server also provides a ``status`` socket for receiving real time audio
playback information. This port is intended to provide information to keep a
GUI updated. The same GUI would ideally provide the ability to send commands
to the sound server over the ``control`` socket. As those commands are carried
out, the GUI would update itself from information received over the ``status``
socket.

*Information*

.. toctree::
   :maxdepth: 1

   messages
   available_sockets