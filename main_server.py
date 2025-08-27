import socket
import os
import logging

conaddr_name = 0
var_num = 0
var_name = con+str(var_num)

def main():
  global s
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind('localhost', 12345)
  Listening = True
  while Listening:
    s.listen(1)
    eval(str(conadr_name)+"_conn"", "+str(conaddr_name)+"_addr = s.accept()")              # NAME_conn, NAME_addr = s.accept()
    eval(str(var_name)+"= client("+str(conadr_name)+"_conn", str(conadr_name)+"_addr)")    # VAR_NAME = client(NAME_conn, NAME_addr)
    var_num += 1
    conaddr_name += 1
    
  
class client(supplied_conn, supplied_addr):
  def __init__(self, conn, addr):
    self.conn = supplied_conn
    self.addr = supplied_addr
  
