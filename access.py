import accesscode as a
from threading import *
import time
a.create("apple",10)
a.create("banana",2,10)# 200 is time-to-live value
print(a.read("banana"))
time.sleep(10)
a.read("banana")
a.create("apple",0)# duplicate key
a.read("mango")# invalid key
a.modify("apple",11)
print(a.read("apple"))
a.delete("apple")
a.read("apple")
a.delete("apple")
a.read("banana")
t1=Thread(target=a.create,args=("orange",30,))
t1.start()
t2=Thread(target=a.read,args=("orange",)) 
t1.join()
t2.start()
t2.join()

