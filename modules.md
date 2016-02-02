## Importing

Source: Python 3 Object Oriented Programming - Dusty Phillips

- importing stuff

```python
import database
db = database.Database()
# Do queries on db

# OR

from database import Database
db = Database()
# Do queries on db
```

- If, for some reason, products already has a class called Database, and we don't want the two names to be confused, we can rename the class when used inside the products module: 
```python
from database import Database as DB
db = DB()
# Do queries on db
```
- We can also import multiple items in one statement. If our database module also contains a Query class, we can import both classes using:

```python
from database import Database, Query
```

- Some sources say that we can even import all classes and functions from the database module using the following example:
- Don't do this.
```python
from database import *
```




