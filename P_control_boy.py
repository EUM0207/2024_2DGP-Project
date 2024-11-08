from pico2d import *
from P_map import Background
from P_boy import Boy
import P_game_world as game_world

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)

def reset_world():
    global boy, background, running
    running = True

    background = Background()
    game_world.add_object(background, 0)  # 배경을 레이어 0에 추가

    boy = Boy()
    background.set_center_object(boy)  # 캐릭터를 배경과 연결
    game_world.add_object(boy, 1)  # 캐릭터를 레이어 1에 추가

def update_world():
    game_world.update()

def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()

open_canvas(800, 600)  # 화면 크기 설정
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)

close_canvas()
