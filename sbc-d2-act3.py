import random

print("Please enter the numbers you're betting on.")

first = int(input("Please enter the first number: "))
second = int(input("Please enter the second number: "))
third = int(input("Please enter the third number: "))

Lfnum = random.randint(1, 3)
Lsnum = random.randint(1, 2)
Ltnum = random.randint(2, 3)

mylist = [first, second, third]
lotolist = [Lfnum, Lsnum, Ltnum]
s
print("Your numbers are:", mylist)
print("And the lottery results are:", lotolist)

if first == Lfnum and second == Lsnum and third == Ltnum:
    print("Jackpot!")
elif (first in {Lfnum, Lsnum, Ltnum} and
      second in {Lfnum, Lsnum, Ltnum} and
      third in {Lfnum, Lsnum, Ltnum} and
      len({first, second, third}) == 3):
    print("You partially win some rewards.")
else:
    print("Better luck next time.")
