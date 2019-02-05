import subprocess
from time import sleep
process1 = subprocess.Popen(['python3.6', 'time30s.py'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
process2 = subprocess.Popen(['python3.6', 'time30s.py'], shell=True, stdin=subprocess.PIPE)
sleep(9)
out = process1.communicate(input=' \n'.encode())[0]
process2.communicate(input=' \n'.encode())
print(out.decode())

