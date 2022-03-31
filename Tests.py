# prize = 0
# charity = 0

# for I in range(0, 40):
#     prize = prize + 1000
#     charity += 0.05 * prize
#     print (prize, charity)

from turtle import *
speed(1000)
color("green")
bgcolor("black")
b = 200
while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1

# bgcolor ("black")
# color("cyan")
# speed(11)
# right(45)

# for i in range (150):
#     circle(30)
#     if 7 < i < 62:
#         left(5)
#     if 80 < i < 133:
#         right(5)
#     if i < 80:
#         forward(10)
#     else:
#         forward(5)