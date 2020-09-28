# demo project for testing out zmq
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20200927

import time
import zmq

def read_time():
    return "TODO"

# zmq setup
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

if __name__ == "__main__":
    
    print("Server has started")
    while True:
        message = socket.recv()
        print(f"(server) Recieved request: {message}")

        time.sleep(1)

        socket.send(b"(from server) Time TODO send here")
