
## Question 1
```python
L = [4,3,55,6,5,44,3,4,3,55,66,77]

for i in range(len(L)):
    print(L[i])
```


## Question 2
```python
class color(object):
    def __init__(self,r,g,b):
        self.color = (r,g,b)
    
    def __str__(self):
        c = self.color
        return "(red: %d , green: %d , blue: %d)" % (c[0],c[1],c[2])
        
```

## Question 3
```python
def __add__(self,rhs):
    c1 = self.color
    c2 = rhs.color
    return color(min(c1[0]+c2[0],255),min(c1[1]+c2[1],255),min(c1[2]+c2[2],255))

c1 = color(160,32,240)
c2 = color(178,34,34)
c3 = c1 + c2
print(c3)
```

## Question 4

```python
class GrayScaler(object):
    def __init__(self,c):
        self.color = c
        
    def average(self):
        c = self.color.color
        avg = (c[0]+c[1]+c[2]) / 3
        return color(avg,avg,avg)
        
    def custom(self,w1,w2,w3):
        c = self.color.color
        w = (c[0]*w1 + c[1] * w2 + c[2] * w3)
        return color(w,w,w)
        
        
    def __str__(self):
        return self.color.__str__()

myColor = color(160,32,240)
gray = GrayScaler(myColor)
print(gray)
avg = gray.average()
print(avg)
cust = gray.custom(.2,.5,.3)
print(cust)
```

## Question 5

```python
class Pet(object):

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "< %s is a %s >" % (self.name, self.species)

class Dog(Pet):
	def __init__(self,name):
		super().__init__(name,"Dog")
	
	def makesSound(self):
		return "Bark"
		
myDog = Dog("Fido")
print(myDog)
print(myDog.makesSound())
```

## question 6
```python
def exists(filename):
	try:
		f = open(filename,"r")
		f.close()
		return True
	except:
		return False
```

## Question 7

```python
```


## Question 8
```python
class Email(object):
	def __init__(self, msg, subj, sender, receiver):
		self.message = msg
		self.subject = subj
		self.sender = sender 	#email address
		self.receiver = receiver #email address
		
class EmailLogger(object):
	def __init__(self):
		self.emails_sent = {}
		self.emails_received = {}
		
	def add(self,email):
		if not email.sender in self.emails_sent:
			self.emails_sent[email.sender] = []
		self.emails_sent[email.sender].append(email)
		
		if not email.receiver in self.emails_received:
			self.emails_received[email.receiver] = []
		self.emails_received[email.receiver].append(email)		
			
	def get_sent_by(self,sender):
		return self.emails_sent[sender]
		
	def get_received_by(self,receiver):
		return self.emails_received[receiver]
		
Logger = EmailLogger()

Email1 = Email("fake message 1","fake subject 1","joe@yahoo.com","sue@gmail.com")
Logger.add(Email1)

Email2 = Email("fake message 2","fake subject 2","bill@yahoo.com","sue@gmail.com")
Logger.add(Email2)

Email3 = Email("fake message 3","fake subject 3","bill@yahoo.com","joe@yahoo.com")
Logger.add(Email3)

Email4 = Email("fake message 4","fake subject 4","jon@hotmail.com","sue@gmail.com")
Logger.add(Email4)


list1 = Logger.get_sent_by("bill@yahoo.com")
print(list1)
# list1 = [Email2,Email3]

list2 = Logger.get_received_by("sue@gmail.com")
print(list2)
# list2 = [Email1,Email2,Email4]
```
