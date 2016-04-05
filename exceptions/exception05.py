"""
 We handle exceptions by wrapping any code that might throw one (whether it is exception code itself, or a call to any function or method that may have an exception raised inside it) inside a try...except clause.
 
 Catches ANY type of exception
 """
 
 try:
    no_return()
except:
    print("I caught an exception")
print("executed after the exception")