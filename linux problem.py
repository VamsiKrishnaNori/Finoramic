 #pip version should be 9.0.3
def pac(i):
    try:
        pip.main(['install',''+str(i)])
    except:
        lst.append(i)
import pip
d=open('depen.json').read()
d1=d.replace("\n","")
d1=d1.replace("}","")
d1=d1.replace('{',"")
d2=d1.split(',')
d2[0]=str(d2[0]).replace("Dependencies =   ","")
d2[0]=str(d2[0]).replace(" ","")
s=len(d2)
lst=[]
for i in d2:
   pac(i)  
if(len(lst)==0):
    print("Success")
else:
    for i in lst:
        print(i)