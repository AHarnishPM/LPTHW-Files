if True and True:
    print "True"
else:
    print "Paradox?"

with open('test.txt', 'w') as f:
    f.write("Hola")

assert True

value = 0

while True:
    value += 1
    print "this loop will be broken when this is 50: %d " % value
    if value < 50:
        continue
    else:
        break

def screaming():
    print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa"

screaming()

numbers = "1 2 3 4 5"

for n in numbers:
    if n == "4":
        break
    print(n)

print "Numeros que no son cuatro"

print "Does 2 = 1 + 1?"
print 2 is 1 + 1

x = lambda a, b : a * b

print "What's 2 times 2?"
print (x(2, 2))
