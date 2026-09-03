import socket

# Create a TCP/IP socket
c = socket.socket()

# Connect to the server listening on localhost:9999
c.connect(("localhost", 9999))

# Receive up to 1024 bytes from the server
msg = c.recv(1024)

# Decode the bytes to a string and print the message
print(msg.decode("utf-8"))

# Close the connection
c.close()
