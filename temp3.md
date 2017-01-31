# Title


- Item 1
- Item 2
  - Item 2a
  - Item 2b
  
1. Item 1
- Item 2
  - Item 2a
  - Item 2b


```python
class DataBase(object):
    def __init__(self,data_file):
        f = open(data_file,'r')
        self.data = f.read()
        self.data = json.loads(self.data)
        self.data = self.data['results']

    def __str__(self):
        length = len(self.data)
        emails = ""
        for entry in self.data:
            email = unicodedata.normalize('NFKD', entry['email']).encode('ascii','ignore')
            emails = emails + str(email) + ",\n"
        return "Database size: %d, \n Email:%s" % (length,emails)

    def IndexLookup(self,i):
        return self.data[i]

    def GetUserByEmail(self,id):
        for e in self.data:
            if e['email'] == id:
                return e
        return None
```
