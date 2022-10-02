#!/usr/bin/env python3

# Sample of relatively fast browser automation using Docker & a Headless Chrome

# See here https://github.com/Zenika/alpine-chrome

# Author: Dan Zulla <dan@mescalin.co>
# 2022 (c) Some rights reversed.

from sh import docker

def main():
    dom = docker(
        "container",
        "run", "--rm", "--security-opt",
        "seccomp=chrome.json", "zenika/alpine-chrome",
        "--dump-dom",
        "https://www.google.com"
    )
    print(dom)

if __name__ == "__main__":
    main()
