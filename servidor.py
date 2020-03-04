import socket
import threading
import sys
import pickle
import os

class Servidor():

	def __init__(self, host=socket.gethostname(), port=int(input("Que puerto quiere usar "))):
		self.clientes = []
		print('\nSu ip actual es : ',socket.gethostbyname(host))
		self.s = socket.socket()
		self.s.bind((str(host), int(port)))
		self.s.listen(30)
		self.s.setblocking(False)

		threading.Thread(target=self.aceptarC, daemon=True).start()
		threading.Thread(target=self.procesarC, daemon=True).start()

		while True:
			msg = input('\n << SALIR = 1 >> \n')
			if msg == '1':
				print("Apagando el servidor")
				self.s.close()
				sys.exit()
			else: pass

	def aceptarC(self):
		print("\t____Hilo que acepta conexiones iniciado en modo DAEMON\n")
		while True:
			try:
				conn, addr = self.s.accept()
				print(f"\nConexion aceptada via {addr}\n")
				conn.setblocking(False)
				self.clientes.append(conn)
			except: pass

	def procesarC(self):
		print("\t____Hilo que procesa mensajes  iniciado en modo DAEMON\n")
		while True:
			if len(self.clientes) > 0:
				for c in self.clientes:
					try:
						data = c.recv(32)
						if data: self.broadcast(data,c)
					except: pass

	def broadcast(self, msg, cliente):
		for c in self.clientes:
			print("Clientes conectados rigth now = ", len(self.clientes))
			try:
				if c != cliente: 
					print(pickle.loads(msg))
					c.send(msg)
			except: self.clientes.remove(c)

arrancar = Servidor()