from sys import argv,path
print('================python from import===================================')
print('path为：',path)#  因为已经导入path成员，所以此处引用时不需要加sys.path
for i in argv:
    print(i)

number1=100
number2=100.235
a='asfdsafdsafd'
print(number1)
print(number2)
print(a)

a=b=c=100
f,g,h=1,2,'123'
print(h)
a=111
b=isinstance(a,int)
print(b)

print(5+4)
print(2**5)
print(2/5)
print(20//5)
print(17%3)
print(3.14j)

world='python'
print(world[2],world[5])
print(world[-1],world[-6])#Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
g=['123456','adb',123,78]
f=[987,564,'afdsaf']
print(g)
print(f*2)
print(g[0],g[3])
print(f[-1],f[-3])
print(g+f)
g[0]=100
g[2:3]=[2,3]
print(g)
g[2:4]=[]
print(g)
g[2]=[]
print(g)

tup=(1,2,3,4,5,6,)
print(tup)
print(tup[-1],tup[-6])
print(tup[-6:])
'''tup[5]=7
print(tup[5])'''

student={'a','b','c','d','e','a','e'}
print(student)
if "g" in student:
    print("g")
else:
    print("g not int set")

a1=set('abcdefg')
a2=set('abcdehk')
print(a1)
print(a2)
print(a1-a2)
print(a1|a2)
print(a1&a2)
print(a1^a2)

dic={}
dic['one']='122222'
dic[2]=12344
print(dic)
print(dic['one'])
tinydic={'name':'张三','age':24,'gender':'男'}
print(tinydic)
print(tinydic.keys())
print(tinydic.values())

dic={'name':'张三','age':28,'gender':'男','age':99}
dic['age']=36
dic['name']='刘西美子'
print("dic['age']:",dic['age'])
print("dic['name']:",dic['name'])