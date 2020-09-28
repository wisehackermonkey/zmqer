# client for the zmq test
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20200927

import zmq 

# zmq setup
context = zmq.Context()

print("Connecting to the Zmq server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

if __name__ == "__main__":
    for request in range(10):
        print(f"(client) Sending Request {request}")
        socket.send(b"(from client) zmq to the rez que")

        # get a reply back
        message = socket.recv()
        print(f"(client) received reply from server {request} [{message}]")