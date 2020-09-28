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
socket.connect("tcp://www.orancollins.com:5555")

if __name__ == "__main__":
    try:
        for request in range(10):
            print(f"(client) Sending Request {request}")

            user_input = input("(client)>")

            # results = f"(from client) {user_input}"

            socket.send(user_input.encode())

            # get a reply back
            message = socket.recv()
            print(f"(from server) {request}>[{message.decode()}]")
    except KeyboardInterrupt:
        print("\nShutting down")