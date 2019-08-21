#!/usr/bin/env python
# ----------------------------------------------------------------------------
from Tkinter import *
import time
import socket
import os
IP=os.environ.get("IPraspDRI")

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
		# Configuracion UDP
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		# Boton para terminar el programa
		self.bcl = Button(self.root, text='Cerrar',
							  command=self.root.destroy).place(x=490, y=20)
		# Mantiene la app abierta
		self.root.mainloop()
	def Straight(self):
		self.data = "straight"
		self.sock.sendto(self.data, (IP, 4002))
	def Left(self):
		self.data = "left"
		self.sock.sendto(self.data, (IP, 4002))
	def Right(self):
		self.data = "right"
		self.sock.sendto(self.data, (IP, 4002))
	def Back(self):
		self.data = "back"
		self.sock.sendto(self.data, (IP, 4002))
	def Stop(self):
		self.data = "stop"
		self.sock.sendto(self.data, (IP, 4002))

# Fin de la clase Aplicacion()
app = Control()  # Creando objeto app de la clase Aplicacion