import os
import sys

print(sys.path)
help("modules")

dayOfWeek = 7

def sayHello(recipient):
    print("Hello, world! Hello {} ".format(recipient))
    return recipient