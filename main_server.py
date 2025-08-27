import socket
import os
import logging

def main():
  global s
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind('localhost', 12345)
  while Listening:
    s.listen(1)
    
  
class client(supplied_conn, supplied_addr):
  def __init__(self, conn, addr):
    self.conn = supplied_conn
    self.addr = supplied_addr
  
