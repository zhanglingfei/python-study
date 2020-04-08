import random
import time
from multiprocessing import Process


def piao(name):

    time.sleep(random.randint(1,5))
    print('%s is piao end' %name)


for i in range(8):
    i=Process(target=piao,args=(f'{i}',))
    i.start()


