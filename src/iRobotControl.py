#!/usr/bin/env python
# ----------------------------------------------------------------------------
from Tkinter import *
import time
import socket
fondo = 'SlateBlue'

class Control():
	def __init__(self):  # Metodo constructor
		fondo = 'SlateBlue'
		fuente = 'SlateBlue'
		# Iniciando la ventana, con sus configuraciones
		self.root = Tk()
		self.root.geometry('600x300')
		self.root.resizable(width=True, height=True)
		self.root.configure(bg=fondo)
		self.root.title('IRobot2 Control')

		#Controles
		self.btn = Button(self.root, text="Straight",
								command=self.Straight).place(x=140, y=90)
		self.btn = Button(self.root, text="Left",
								command=self.Left).place(x=50, y=150)
		self.btn = Button(self.root, text="Stop", 
								command=self.Stop).place(x=150, y=150)
		self.btn = Button(self.root, text="Right",
								command=self.Right).place(x=250, y=150)
		self.btn = Button(self.root, text="Back",
								command=self.Back).place(x=140, y=200)
		# Configuracion TCP
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		IP = '10.154.116.54'
		PORT = 4002
		BUFFER_SIZE = 1024

		# Boton para terminar el programa
		self.bcl = Button(self.root, text='Cerrar',
							  command=self.root.destroy).place(x=490, y=20)
		# Mantiene la app abierta
		self.root.mainloop()
	def Straight(self):
		self.data = "straight"
		self.sock.connect((IP, PORT))
		self.sock.send(self.data)
		self.data2 = self.sock.recv(BUFFER_SIZE)
		self.sock.close()
		print "received data:", self.data2
	def Left(self):
		self.data = "left"
		self.sock.connect((IP, PORT))
		self.sock.send(self.data)
		self.data2 = self.sock.recv(BUFFER_SIZE)
		self.sock.close()
		print "received data:", self.data2
	def Right(self):
		self.data = "right"
		self.sock.connect((IP, PORT))
		self.sock.send(self.data)
		self.data2 = self.sock.recv(BUFFER_SIZE)
		self.sock.close()
		print "received data:", self.data2
	def Back(self):
		self.data = "back"
		self.sock.connect((IP, PORT))
		self.sock.send(self.data)
		self.data2 = self.sock.recv(BUFFER_SIZE)
		self.sock.close()
		print "received data:", self.data2
	def Stop(self):
		self.data = "stop"
		self.sock.connect((IP, PORT))
		self.sock.send(self.data)
		self.data2 = self.sock.recv(BUFFER_SIZE)
		self.sock.close()
		print "received data:", self.data2
# Fin de la clase Aplicacion()
app = Control()  # Creando objeto app de la clase Aplicacion
