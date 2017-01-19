import random


print("hello world")

a = []

print(a)

a.append(3)

print(a)

a.append(5)

print(a)

a.append("mcdonalds")

print(a)

a.append([1,2,3,'a','b'])

print(a)

# a = "hello"

# print(a)

# a = a + '3'

# print(a)

for i in range(10):
  a.append(random.randint(0,100))


for x in a:
  print(x)
  
for j in range(len(a)):
  print(a[j])

print()

print(a[len(a)-1])

print()

print(a[-1])

print(a)

print(a[2:5])

print()

for i in range(0,len(a),2):
  print(a[i])

print(a)

a.insert(7,'dont jack my list')

print(a)

a.insert(len(a),'please work')

print(a)

a.insert(len(a)+3,'hmmmm')

print(a[-2])

a[len(a)+2] = '999999'
  

