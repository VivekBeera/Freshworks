import time
import threading 

dictionery={}

def create(key,value,timeout=0):
    if key in dictionery:
        print("ERROR: this key already exists") 
    else:
        if(key.isalpha()):
            if len(dictionery)<(1024*1020*1024) and value<=(16*1024*1024): 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    dictionery[key]=l
            else:
                print("ERROR: Memory limit exceeded!")
        else:
            print("ERROR: INVALID KEYNAME. IT MUST NOT CONTAIN SPECIAL CHARECTERS OR NUMBERS")
            
def read(key):
    if key not in dictionery:
        print("ERROR: GIVEN KEY DOES NOT EXIST. ENTER A VALID KEY") 
    else:
        b=dictionery[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                stri=str(key)+":"+str(b[0]) 
                return stri
            else:
                print("ERROR: TIME-TO-LIVE OF GIVEN", key," HAS EXPIRED") 
        else:
            stri=str(key)+":"+str(b[0])
            return stri


def delete(key):
    if key not in dictionery:
        print("ERROR: GIVEN KEY DOES NOT EXIST. ENTER A VALID KEY") 
    else:
        b=dictionery[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del dictionery[key]
                print("KEY IS SUCCESSFULLY DELETED")
            else:
                print("ERROR: TIME-TO-LIVE OF GIVEN", key," HAS EXPIRED") 
        else:
            del dictionery[key]
            print("key is successfully deleted")



def modify(key,value):
    b=dictionery[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in dictionery:
                print("ERROR: GIVEN KEY DOES NOT EXIST. ENTER A VALID KEY")
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                dictionery[key]=l
        else:
            print("ERROR: TIME-TO-LIVE OF GIVEN", key," HAS EXPIRED")
    else:
        if key not in dictionery:
            print("ERROR: GIVEN KEY DOES NOT EXIST. ENTER A VALID KEY") 
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            dictionery[key]=l
