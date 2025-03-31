# error handling------------> only for run-time errors, can't handle syntax errors 
'''
->Error handling is the process of managing and responding to errors in a program so that it doesn't crash unexpectedly. 
->In Python, errors are handled using the try-except block to catch and fix issues gracefully.

Types of errors:
    -> Compile time errors: (syntax errors)
        -> Occur when the Python interpreter finds incorrect syntax in the code.
        -> The program won’t run until the syntax error is fixed.
    -> Run time errors: (exceptions)
        -> These errors occur during program execution.
        ->An exception is a runtime error that occurs during the execution of a program and disrupts its normal flow.
'''
#syntax
'''
try:
    #try to execute this code
except:
    # if error, execute this code
else:
    # if no error, execute this code
finally:
    # if error or no error, always execute this code

    
# there can be only 1 try block and any no.of except blocks (atleast 1)
'''
'''
try:
    #risky code that have a chance to get error in the future
    print("hello")
    print(1/0)
except:
    print("error vachindhi")
else:
    print("error raledhu")
finally:
    print("always")
#o/p:-
    #hello
    #error vachindhi
    #always

a=5
try:
    print("hello")
    print(a)
except:
    print("error vachindhi")
else:
    print("error raledhu")
finally:
    print("always")

#o/p:-
    #hello
    #5
    #error raledhu
    #always
'''
'''
try:
    print('a'+12)
except Exception as e:
    print("Error:",e)
print('hi')
'''
'''
try:
    print('a'+12)
except TypeError as e:
    print("type error:",e)#type error: can only concatenate str (not "int") to str
# or

try:
    print(a+12)
except NameError:
    print("name error")#name error
'''
'''
try:
    print(a+12)#error occurs
    print('a'+12)#this statement do not be executed
except NameError:
    print("name error")#name error
except TypeError:
    print("type error:")

#o/p:-
    #name error
'''
'''
Error Type	                            Description	                                                Example
----------                              -----------                                                 -------
ZeroDivisionError   	Occurs when dividing by zero.	                                            x = 10 / 0
ValueError	            Raised when an operation gets an invalid value.	                            int("abc")
TypeError	            Occurs when an operation is performed on an incompatible type.	            5 + "hello"
IndexError          	Raised when accessing an index that doesn’t exist in a list or tuple.	    lst = [1,2]; print(lst[5])
KeyError	            Raised when a dictionary key is not found.	                                d = {}; print(d["name"])
FileNotFoundError	    Raised when trying to open a file that doesn’t exist.	                    open("missing.txt", "r")
ModuleNotFoundError	    Raised when an imported module is not found.	                            import nonexistent_module
AttributeError	        Raised when an invalid attribute is accessed on an object.	                num = 10; num.append(5)
NameError	            Raised when trying to use an undefined variable.	                        print(x) (if x is not defined)
IndentationError	    Occurs when indentation is incorrect.	                                    def func():
                                                                                                    print("Hello") (missing indentation)

'''
#================================================================value error======================================================================
yeah here also
while True:
    try:
        a=int(input("Enter an integer:"))
        break
    except ValueError:
        print("Invalid input! please enter a valid input.")
print("you entered:",a)





#practice python problems at   https://www.youtube.com/watch?v=AhgxApbyGiM&list=PLbMVPNscUopS0sl1pHuPWGp_lEzEznMlI


I made changes to this second repository
