# demo project for testing out zmq
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20200927

import time
import zmq
import os

def read_time():
    return "TODO"

# zmq setup
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

if __name__ == "__main__":
    try:
        print("Server has started")
        while True:
            message = socket.recv()
            print(f"(from client)> {message}")

            time.sleep(1)

            socket.send(f"(from server) {os.popen(message.decode()).read()}".encode())
    except KeyboardInterrupt:
        print("\nShutting down")