import threading
import sys
import socket
import pickle
import os

class Cliente():

	def __init__(self, host=input("Intoduzca la ip del servidor ?  "), port=int(input(" Intoduzca el puerto del servidor ?"))):
		self.s = socket.socket()
		self.s.connect((host, int(port)))
		threading.Thread(target=self.recibir, daemon=True).start()
		print('Hilo con PID = ',os.getpid(), ' y total Hilos activos =', threading.active_count())

		while True:
			msg = input('\nEscriba texto ?   ** Enviar = ENTER   ** Salir Chat = 1 \n')
			if msg != '1' : self.enviar(msg)
			else:
				print(" **** Me piro vampiro; cerrando socket = ", s.getpid())
				self.s.close()
				sys.exit()

	def recibir(self):
		while True:
			try:
				data = self.s.recv(32)
				if data: print(pickle.loads(data))
			except: pass

	def enviar(self, msg):
		self.s.send(pickle.dumps(msg))

arrancar = Cliente()

		