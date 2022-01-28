from threading import Lock,Thread
import time

n=0
nn=Lock()

def navi(): 
    for i in range(10000):
        global n
        nn.acquire()
        n+=1
        nn.release()


Thread(target=navi,args=()).start()
Thread(target=navi,args=()).start()
time.sleep(5)
print(n)
