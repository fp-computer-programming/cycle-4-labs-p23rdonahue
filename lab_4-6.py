#author: RED 10/18/22
from xmlrpc.server import DocCGIXMLRPCRequestHandler


animal = input("Name an animal that can bring a dish to the feast")
dish = input("What dish are they bringing?")


first_letter_1 = animal[0]
first_letter_2 = dish[0]
reverse = dish [::-1]
last_letter_2 = reverse[0]

if first_letter_1 == first_letter_2 and first_letter_1 == last_letter_2:
    print('true')
else:
    print('false')