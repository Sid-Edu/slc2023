import pygame
import subprocess
import subprocess

pygame.init()



# Set window size
window_size = (400, 400)

# Create window
screen = pygame.display.set_mode(window_size)

# Set title of the window
pygame.display.set_caption("Main Page")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Load font
font = pygame.font.Font(None, 25)

# Define button class
class Button:
    def __init__(self, x, y, width, height, text, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color

    def draw(self, screen, font):
        # Draw the button
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        # Add text to the button
        text = font.render(self.text, True, black)
        screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

# Create buttons
button1 = Button(30, 160, 100, 50, "hangman", white)
button2 = Button(280, 160, 100, 50, "wordle", white)
button3 = Button(150, 100, 100, 50, "leaderbaord", white)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check if a button is clicked
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button1.x < mouse_x < button1.x + button1.width and button1.y < mouse_y < button1.y + button1.height:
                # Open file for button 1
                #with open("hangman.py", "r") as file:
                    #content = file.read()
                    #print(content)
                subprocess.call(["python", "hangman.py"])

            if button2.x < mouse_x < button2.x + button2.width and button2.y < mouse_y < button2.y + button2.height:
                # Open file for button 2
                #with open("file2.txt", "r") as file:
                    #content = file.read()
                    #print(content)
                subprocess.call(["python", "youtubemain.py"])

            if button3.x < mouse_x < button2.x + button2.width and button3.y < mouse_y < button3.y + button3.height:
                # Open file for button 2
                #with open("file2.txt", "r") as file:
                    #content = file.read()
                    #print(content)
                subprocess.call(["python", "leaderboard.py"])


    # Draw buttons on the screen
    screen.fill(black)
   
    
    button1.draw(screen, font)
    button2.draw(screen, font)
    button3.draw(screen, font)

    pygame.display.update()

# Quit Pygame
pygame.quit()
