#new script, 10 diff ways to use a function
def fingers_toes(fingers, toes):
    print "I have %d fingers" % fingers
    print "I have %d toes\n" % toes

fingers_toes(10, 10)

fingers_toes(5 + 5, 5 + 5)

fing_count = 10
toes_count = 10

fingers_toes(fing_count, toes_count)

print "How many fingers do you have?"
fing_count = raw_input('?' )
print "How many toes do you have?"
toes_count = raw_input('?' )

print "So you have %r fingers and %r toes?" % (
    fing_count, toes_count)
