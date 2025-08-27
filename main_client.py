import socket
import os
import logging

server_ip = 192.192.192.0
server_port = 92778

print("DNSbypass v.1")

def main():
  global s
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def establish_connection():
  s.connect(server_ip, server_port)

def relay_request(request):
  message = request
  s.sendall(message.encode('utf-8'))
