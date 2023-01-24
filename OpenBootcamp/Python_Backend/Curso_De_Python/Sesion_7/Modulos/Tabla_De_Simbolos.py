""" import pprint

def test():
    print("Hola")

pprint.pprint(globals())
test() """

variable = 5
print(variable)

def prueba():
    # globals()['variable'] = 6
    global variable
    variable = 6
    
prueba()
print(variable)
