from pico2d import *
from random import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND_FULL.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2

def handle_events():

    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

hand_points = [(randint(-640, 640), randint(-512, 512)) for i in range(10)]

while running:

    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    
    for px, py in hand_points:
        hand_arrow.draw(px, py)

    character.clip_draw(frame * 100, 0, 100, 100, x, y, 150, 150)
    update_canvas()

    handle_events()
    if not running:
        break

    frame = (frame + 1) % 8
    delay(0.05)


close_canvas()
