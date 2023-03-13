from pygame import *

# prepare window
w_width = 1052
w_height = 768
window = display.set_mode((w_width, w_height))
display.set_caption("First application")

# set window background
background = transform.scale(image.load(
    r'pictures\backgrounds\galaxy_2.jpg'), (w_width, w_height))
window.blit(background, (0, 0))

# add character
height = 100
width = 100
x = 100
y = 100

# draw.rect(window, (0, 0, 255), (x, y, width, height))
img1 = transform.scale(image.load(
    r'pictures\heroes\ufo_1.png'), (width, height))
window.blit(img1, (x, y))
display.update()
time.delay(5000)
