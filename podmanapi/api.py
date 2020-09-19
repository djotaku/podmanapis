import socket
import os

client = socket.socket(socket.AF_UNIX)
client.connect("/run/podman/podman.sock")
send_me = "http://d/v1.0.0/libpod/info".encode('utf-8')
response = client.send(send_me)
print(response)