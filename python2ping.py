import os

ip_addr = input('Enter the IP address: ') 
stream = os.popen('ping -c 4 {}'.format(ip_addr)) 
output = stream.read() 
if '0 received' in output: 
 print('IP unreachable') 
else:
 print('IP reachable')
 
