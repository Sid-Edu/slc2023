import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
import hashlib, uuid
import subprocess
string=''
hashed_password=''
current_string_p=[]
display_p=[]
symbol='*'

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)

  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string_un = []
  display_box(screen, question + ": " + string.join(current_string_un))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string_un = current_string_un[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_LSHIFT or inkey == K_RSHIFT:
      inkey=get_key()
      if inkey <= 127:
        upper_case=inkey-32
        current_string_un.append(chr(upper_case))
    elif inkey <= 127:
      current_string_un.append(chr(inkey))
    display_box(screen, question + ": " + string.join(current_string_un))
  return string.join(current_string_un)

def main():
  global display_p
  display_p=[]
  screen = pygame.display.set_mode((500,300))
  user_name = (ask(screen, "Username") )
  
  if len(user_name) > 0:
   subprocess.run(["python", "mainpage.py"])
  else:
   #print("User name is mandatory")   
   display_box(screen,"User Name Is Mandatory")

if __name__ == '__main__':
      main()