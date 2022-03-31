# class 
# class Student:
#  pass
#  def __init__(self, name, age):
#     self.name = name
#     self.age = age 

# Duarte = Student("Duarte Coelho", 17)
# Enzo = Student ("Enzo Gazoto", 16)
# Eduardo = Student("Eduardo Machado", 16)

# print (Duarte.name)
# print (Enzo.age)
# print (Eduardo.name)

# Create a class 
# Add atleast 3 objects to that class 
# add three properties to the class

# class rtx_graphics():
#     def __init__(self, name, ghz, cuda_cores, mem):
#         self.name = name 
#         self.ghz = ghz
#         self.cuda_cores = cuda_cores
#         self.mem = mem

# object_list = []
# rtx_3090 = rtx_graphics("rtx_3090", "1.70 Ghz", "10496", "24GB")
# object_list.append(rtx_3090)
# rtx_3080 = rtx_graphics("rtx_3080", "1.71 Ghz", "8704", "10GB")
# object_list.append(rtx_3080)
# rtx_3070 = rtx_graphics("rtx_3070", "1.73 Ghz", "5888", "8GB")
# object_list.append(rtx_3070)
# rtx_3060 = rtx_graphics("rtx_3060", "1.78 Ghz", "3584", "12GB")
# object_list.append(rtx_3060)

# graphics = (input ("What graphics card do you want to see: "))

# info = (input ("What do you want to know about: "))


# for g in object_list:
#     if g.name == graphics:
#         print ("You have %s chosen with a %s clockspeed, %s of ram and %s cudacores" %(g.name, g.ghz, g.mem, g.cuda_cores))

# Mutable = something u can change 
# immutable = something that cannot be changed 
# List[] --> mutable´
# Tuple() --> immutable 
# Immutable things can be changed, but when changed they delete the old thing in the memeory and create something new (in a diferent place in the memory) 

#  my_list = [1, "Hello", 3.4, -5]
#  my_list.__len__()
#  my_list.remove("Hello")
#  my_list.__len__()
#  new_list = [8, 4, 6]
#  my_list = my_list + new_list
#  x = my_list.__len__()
#  print(my_list[x-1])

#  my_tup = ("Orange", [10, 20, 30], (5, 15, 25))
#  my_tup.__len__()
#  print((my_tup [1][my_tup[1].index(30)])) 

#  my_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#  print(my_dict.keys())
#  print (my_dict.items())
#  list(my_dict)
#  dict([(1, 10), (2, 20), (3, 30), (4, 40), (5, 50), (6, 60)])

#  sum_values = 0 
#  for key, value in my_dict.items():
#      print (key,value)
#      sum_values = sum_values + value
#  print (sum_values)



#  import pygame 
#  import random

#  pygame.init()
#  screen_size = (600, 480)
#  screen = pygame.display.set_mode(screen_size)

#  color = (30, 35, 190)

#  while True:
#      for event in pygame.event.get():
#          if event.type == pygame.QUIT:
#              color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255) )
#              print (event.type)
#      screen.fill(color)
#      pygame.display.update()

#      pass



#  how to close a program
#  import pygame 
#  import random

#  pygame.init()
#  screen_size = (600, 480)
#  screen = pygame.display.set_mode(screen_size)

#  color = (30, 35, 190)
#  run = True
 
#  while run:
#      for event in pygame.event.get():
#          if event.type == pygame.QUIT:
#              run = False 
#      screen.fill(color)
#      pygame.display.update()

#      pass



# more color changing windows 
#  import pygame 
#  import random
#  import time

#  pygame.init()
#  screen_size = (600, 480)
#  screen = pygame.display.set_mode(screen_size)

#  color = (30, 35, 190)
#  run = True
 
#  while run:
#       for event in pygame.event.get():
#           if event.type == pygame.QUIT:
#               print ("Pressed quit button")

#               for i in range(100):
#                   color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255) )
#                   screen.fill(color)
#                   pygame.display.update()
#                   time.sleep(.5) 
#       screen.fill(color)
#       pygame.display.update()



#  import pygame 
#  screen_size = (600, 480)
#  screen = pygame.display.set_mode(screen_size)

#  pygame.draw.line(screen, (255, 255, 255), (0, 240), (600,240))
#  pygame.draw.line(screen, (255, 255, 255), (300, 0), (300, 480))
#  run = True
#  while run:
#      for event in pygame.event.get():
#          if event.type == pygame.QUIT():
#              pygame.quit() 
#      pygame.display.update()



#  random color changing rectangle falls down

# First try at making a game 

import pygame 
import time
import random

run = True
screen_size = (600, 800)
pos_x = 300
pos_y = 800 - 60
y = 10
x = 225
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
color_player = (0, 0, 255)
blocks_passed = 0 

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
collision = False
while run:

    if not collision:
       pygame.display.update()

    screen.fill((0,0,0)) 
    pygame.draw.rect(screen, color, (x,y,70,60))
    pygame.draw.rect(screen, color_player, (pos_x, pos_y, 70, 60))
    y = y + 5
    if y > 750:
        y = 10 
        x = random.randint(5, 445) 
        color = (random.randint(0,255), random.randint(0, 255), random.randint(0, 255))
        blocks_passed = blocks_passed + 1
    
    if color == (0,0,0):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if y > (800 - 120):
        if pos_x < x < (pos_x + 70):
            collision = True
            print("Blocks passed:",blocks_passed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print("Blocks passed: ",blocks_passed)

        if event.type == pygame.KEYDOWN:
        
            if event.key == pygame.K_LEFT:
                pos_x = pos_x - 10

            if event.key == pygame.K_RIGHT:
             pos_x = pos_x + 10

    clock.tick(60)


