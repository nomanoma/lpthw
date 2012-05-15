def loop(n,m=1):
    numbers = []
    for i in range(0, n, m):
        print "At the top i is %d" % i
        numbers.append(i)
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers

numbers=loop(5,2)

print "The numbers: "

for num in numbers:
    print num
