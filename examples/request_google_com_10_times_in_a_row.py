#!/usr/bin/env python3

# This is your project description.

# Author: Your Name <your@name.me>
# 2022 (c) some rights reversed.

import socket
import os


def send_message_grab_response(message=b""):
    client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    client.connect("/tmp/stealthy")
    client.send(b'LOAD ' + message)
    data = client.recv(200000)
    return data

def main():
    url = "https://www.parship.de".encode("utf-8")

    if os.path.exists("/tmp/stealthy"):
        data = send_message_grab_response(message=url)
        print("Responded with %d bytes." %len(data))
    else:
        print("Stealthy is not running, Unix socket unreachable.")

if __name__ == "__main__":
    main()
