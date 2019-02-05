import subprocess
from time import sleep
process1 = subprocess.Popen(['python3.6', 'time30s.py']) #, stdin=subprocess.PIPE, stdout=subprocess.PIPE
process2 = subprocess.Popen(['python3.6', 'time30s.py'])
sleep(3)
process1.terminate()
process2.terminate()

