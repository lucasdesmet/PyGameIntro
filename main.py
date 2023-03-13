from pygame import *
import sys

# prepare window
w_width = 1052
w_height = 768
window = display.set_mode((w_width, w_height))
display.set_caption("First application")

# set window background
background = transform.scale(image.load(
    r'pictures\backgrounds\galaxy_2.jpg'), (w_width, w_height))


# add ufo
ufo_h = 100
ufo_w = 100
# draw.rect(window, (0, 0, 255), (x, y, ufo_w, ufo_h))
ufo_img = transform.scale(image.load(
    r'pictures\heroes\ufo_1.png'), (ufo_w, ufo_h))

x = 100
y = 100
dist = 10
run = True
while run:
    # erase - TODO: follow https://www.pygame.org/docs/tut/MoveIt.html
    window.blit(background, (0, 0))
    # loop runs every 0.1 second
    time.delay(50)
    # sort through all the events that could have happened
    for e in event.get():
        if e.type == QUIT:
            sys.exit()
        if e.type == KEYDOWN:
            keys = key.get_pressed()
            # check which buttons were pressed
            if keys[K_LEFT]:
                x -= dist
            if keys[K_RIGHT]:
                x += dist
            if keys[K_UP]:
                y -= dist
            if keys[K_DOWN]:
                y += dist
            if keys[K_q]:
                run = False
    window.blit(ufo_img, (x, y))
    display.update()
