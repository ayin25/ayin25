
import socket 
from IPy import IP


class PortScan():

	banners = []
	open_ports = []

	def __init__(self,target,port_num):
		self.target = target
		self.port_num = port_num

	def get_ip(self):
		try:
			IP(self.target)
			return(self.target)
		except ValueError:
			return socket.gethostbyname(self.target)


	def scan(self):
		
		for port in range (1,500):
			self.scan_port(port)


	def scan_port(self,port):
		try:
			c_ip = self.get_ip()
			s = socket.socket()
			s.settimeout(0.5)
			s.connect((c_ip,port))
			self.open_ports.append(port)
			try:
				banner = socket.recv(1024).decode().strip('\n').strip('\r')
				self.banners.append(banner)
			except:
				self.banners.append(' ')
		except:
			s.close()
