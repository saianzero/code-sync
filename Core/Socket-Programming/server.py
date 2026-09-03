import socket

# Create a TCP/IP socket 
s = socket.socket()

# Bind the socket to an address and port so clients know where to reach it
s.bind(("localhost", 9999))
print("Socket created")

# Start listening; allow up to 3 pending connections in the backlog queue
s.listen(3)
print("waiting for connections")

while True:
    # Block until a client connects; returns a new socket for that client
    c, addr = s.accept()
    print(f"connected with addr: {addr}")

    # Send a greeting to the client (data must be bytes, hence the encode)
    c.send(bytes("Hi", "utf-8"))

    # Close this client's connection; the server keeps listening for more
    c.close()
