name = 'Aaron J. Harnish'
age = 16.0
height = 73.0
weight = 145.0
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'
meters = height / 39.37

print "Let's talk about %s." % name
print "He's %d inches tall and %s meters tall." % (height, meters)
print "He's %d pounds heavy" % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
