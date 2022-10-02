#!/usr/bin/env python3

# Sample of relatively fast browser automation using Docker & a Headless Chrome

# See here https://github.com/Zenika/alpine-chrome

# Author: Dan Zulla <dan@mescalin.co>
# 2022 (c) Some rights reversed.

import socket
import os

from sh import docker

def main():

    if os.path.exists("/tmp/stealthy"):
        os.remove("/tmp/stealthy")

    server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    server.bind("/tmp/stealthy")

    while True:
        datagram = server.recv(2038 + 4 + 1) # max RFC url size + proto + space

        if not datagram:
            break
        else:
            print("-" * 80)
            print(datagram)
            if "KILL" == datagram:
                break
            elif "LOAD" == datagram[:3]:
                url = datagram.split(" ")[1]
                # add urlparse verification here @TODO
                dom = docker(
                    "container",
                    "run", "--rm", "--security-opt",
                    "seccomp=chrome.json", "zenika/alpine-chrome",
                    "--dump-dom",
                    url
                )
                print("Requested " + url)
                server.send(dom)
                print("Returned DOM into Unix")


        print("-" * 80)
        print("Shutting down.")
        server.close()
        os.remove("/tmp/stealthy")

if __name__ == "__main__":
    main()
