# Author: IBN (AMDG) 10/19/2021

q = int(input("What was the day of the month? "))
m = int(input("What was the month? "))
y = int(input("What was the year? "))
if m == 1:
    m = 13
if m == 2:
    m = 14
if m == 13 or 14:
    y -= 1

j = int(y / 100)
k = int(y % 100)

h = int(((q + ((26 * (m+1)) // 10) + k + (k // 4) + (j // 4) + (5 * j)) % 7))

if h == 0:
    h = "Saturday"
elif h == 1:
    h = "Sunday"
elif h == 2:
    h = "Monday"
elif h == 3:
    h = "Tuesday"
elif h == 4:
    h = "Wednesday"
elif h == 5:
    h = "Thursday"
elif h == 6:
    h = "Friday"

if m == 13:
    m = 1
elif m == 14:
    m = 2

if m == 1:
    y += 1
if m == 2:
    y += 1
print(str(m) + "/" + str(q) + "/" + str(y) + " was a: " + str(h))

# This is needlessly complicated but it works
