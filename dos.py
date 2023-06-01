import requests
from multiprocessing import Process
import time

start = time.time()
#target = input("Enter ip add of target host: ")
fake_ip = '132.21.20.32'
#port = int(input("Port address: "))
attack_num = 0


def attack():
	for i in range(10):
		res = requests.get('https://example.com/')
		print(res)


threads=[]
for i in range(100):
	thread = Process(target=attack,args=())
	thread.start()
	threads.append(thread)

for t in threads:
	t.join()

end = time.time()

print(end-start)


