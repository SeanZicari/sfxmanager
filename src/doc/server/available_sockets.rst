Available Sockets
#################

+-------------------+-------------+-----------------+
| Socket Name       | Socket Port | ZMQ Type        |
+===================+=============+=================+
| `Control Socket`_ | 5600        | REQ/REP         |
+-------------------+-------------+-----------------+
| `Status Socket`_  | 5601        | REQ/REP         |
+-------------------+-------------+-----------------+


Control Socket
==============

This socket is sending commands to the server. The server will respond by
acknowledging the command and then carry it out.

Status Socket
=============

This socket is for receiving real time status updates from the server.
Updates will only be sent out when changes occur. This could be frequently.