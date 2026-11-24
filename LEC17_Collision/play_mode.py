from pico2d import *
import game_world
import game_framework
from boy import Boy
from grass import Grass
from ball import Ball
from zombie import Zombie
import random

boy = None


def handle_events():


    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global boy, grass, balls, zombies

    boy = Boy()
    game_world.add_object(boy)

    grass = Grass()
    game_world.add_object(grass, 0)

    balls = [Ball(random.randint(100, 700), 60, 0) for _ in range(30)]
    game_world.add_objects(balls, 1)

    game_world.add_collision_pair('boy:ball', boy, None)
    game_world.add_collision_pair('grass:ball', grass, None)
    for ball in balls:
        game_world.add_collision_pair('boy:ball', None, ball)
        game_world.add_collision_pair('grass:ball', None, ball)

    zombies = [Zombie() for _ in range(4)]
    game_world.add_objects(zombies, 1)


def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy, grass, balls, zombies
    game_world.clear()
    boy = None
    grass = None
    balls = []
    zombies = []


def update():
    game_world.update()
    game_world.handle_collisions()

def render():
    clear_canvas()
    game_world.render()
    update_canvas()

def handle_collision():
    for group, pairs in game_world.collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if a is not None and b is not None:
                    if collide(a, b):
                        a.handle_collision(group, b)
                        b.handle_collision(group, a)








