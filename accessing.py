 import code as x 

x.create("Hello",25)

x.create("src",70,3600) 

x.read("Hello")

x.read("src")

x.create("Hello",50)

x.modify("Hello",55)
 
x.delete("Hello")

t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t2.start()
t2.sleep()