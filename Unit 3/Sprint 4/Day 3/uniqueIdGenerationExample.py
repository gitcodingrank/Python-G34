import uuid

#To Generate Unique id in string
#print("".join(str(uuid.uuid4()).split("-")))


#To Generate Unique Id in Integer


# print(str(uuid.uuid4().int)[:10:])


import time

# print(time.ctime())
print(int(time.time()*1000))

