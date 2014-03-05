def a (num):
    i = 0
    numbers = []
    while i < num:
        print "At the top i is %d" % i
        numbers.append(i)
        i = i + 1
        print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
    print "The numbers: "
    for mynum in numbers:
        print num


def b (num1):
    i = 0
    numbers = []
    for i in range(0,num1):
        print "At the top i is %d" % i
        numbers.append(i)
        i = i + 1
        print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
    print "The numbers: "
    for mynum in numbers:
        print mynum

a(int(raw_input("num=")))
b(int(raw_input("num1=")))

