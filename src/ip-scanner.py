import re
import threading

from urllib import request

ips = []

with open('../resources/exports.txt') as exports:
	count = 0

	def scan():
		global count

		while count < len(ip_addresses):
			ip_address = ip_addresses[count]
			count += 1
			req = request.Request('http://' + ip_address + ':8080')

			try:
				request.urlopen(req, timeout=3)

				print(ip_address, 'succeeded')
			except Exception as e:
				print(e)

	ip_addresses = re.findall(r'(?:IP Address: )(.*)', exports.read())
	threads = [threading.Thread(target=scan).start() for i in range(0, 20)]
