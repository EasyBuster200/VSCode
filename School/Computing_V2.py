import pygame

screen_width = 1600
screen_height = 1000
spaceship_width = 80
spaceship_height = 140
color_black = (0,0,0)
color_white = (255,255,255)
color_green = (0,255,0)

spaceship_x = screen_width/2 - spaceship_width/2
spaceship_y = screen_height - spaceship_height

screen = pygame.display.set_mode((screen_width,screen_height ))
## Fill screen color

## Add background image
## Load the image
background_img = pygame.image.load("img/space.jpg")
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("img/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.x = 90
        self.rect.y = 90


## Spaceship image
spaceship_img = pygame.image.load("img/spaceship.png")
spaceship_img = pygame.transform.scale(spaceship_img, (spaceship_width, spaceship_height))
screen.fill(color_green)

## Stone image
stone1_img = pygame.image.load("img/rock1.png")
stone1_img = pygame.transform.scale(stone1_img, (100, 100))
# spaceship_img = pygame.transform.scale(spaceship_img, (spaceship_width, spaceship_height))
screen.fill(color_green)
run = True
while run:
    screen.blit(background_img, (0,0))
    screen.blit(stone1_img, (screen_width/2 -50 , 0))
    screen.blit(spaceship_img, (spaceship_x, spaceship_y))
    pygame.display.update()


# Using Git and Github 
#All the commands are used in the git cmd (administrator)
#To download a file from github use: git clone sshkey from github
#to get the ssh key go to the code on github and press the green code button and copy the ssh key 
#To check updates use git status 
#To save a change to a specific file use git add file name 
#To save all use git add --all or git add .
#That only saves to the computer itself to send back to github use git commit -m "changes made"
#The changes made will be like the name of the change on github
#Now everything should be in github and you should be able to see the old versions without the changes on github 
#Use cd to change cmd directory 
#Use git branch to check existing branches on the project 
#Use git checkout -b name of branch
#you always create a new branch, only change it to the main once the full code is done and working 
#To  merge: git checkout main (main being the one you want to merge into)
#git merge name (name of the brach merging into main)
#Use git checkout ssh key of version, to see older versions without recent changes  