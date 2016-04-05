"""
What if we want to catch different exceptions and do different things with them? 
Or maybe we want to do something with an exception and then allow it to continue to bubble up to the parent function, as if it had never been caught? 
"""

def funny_division3(anumber):
       try:
           if anumber == 13:
               raise ValueError("13 is an unlucky number")
           return 100 / anumber
       except ZeroDivisionError:
           return "Enter a number other than zero"
       except TypeError:
           return "Enter a numerical value"
       except ValueError:
           print("No, No, not 13!")
           #raise raise