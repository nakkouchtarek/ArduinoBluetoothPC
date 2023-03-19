import pygame
import socket


class ConnectHC06:
    def __init__(self, addr, channel):
        self.addr = addr
        self.channel = channel

    def connect(self):
        self.socket = socket.socket(socket.AF_BLUETOOTH,
                                    socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        # socket.AF_BLUETOOTH : low level bluetooth protocol
        # socket.SOCK_STREAM : tcp protocol
        # BTPROTO_RFCOMM : radio frequency communication that accepts bluetooth address and channel params used for serial communication
        try:
            self.socket.connect((self.addr, self.channel))
            print("Connected succesfully!!")
        except:
            print("Connection failed...")
            self.close_connection()

    def send(self, command):
        self.socket.send(command.encode())

    def close_connection(self):
        self.socket.close()
