
# Assignment by HV
# For Loop Basic I

# 1. Basic - Print all the numbers/integers from 0 to 150.

for count in range (0,150):
    print ("", count)

#2.	Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.

for count in range (5,1000001,5):
    print ("", count)

#3.Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".

for x in range (1,101):
    if x % 5 == 0 and x % 10 != 0:
        print ("Coding")
    elif x % 5 == 0 and x % 10 == 0:
        print ("Dojo")
    else:
        print (x)


# 4.Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

x = 1
odd = 0
while x <= 500000:
    if x % 2 != 0:
        odd = odd + x
        print (x)
    x = x+1
print ("Final sum:", odd)

# 5.Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).

countDown4 = 2018
while (countDown4 >=0):
    if countDown4 !=0:
        print(countDown4)
        countDown4 = countDown4 - 4
    else: 
        break

#6. Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)

lowNum = 2
highNum = 9
mult = 3
for count in range (lowNum,highNum+1):
    if count % mult == 0:
        print (count)