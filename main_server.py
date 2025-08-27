import socket
import os
import logging

def main():
  global s
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind('localhost', 12345)
  s.listen(1)
class client:
  
