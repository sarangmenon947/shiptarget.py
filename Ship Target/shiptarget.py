import pgzrun
import itertools
import random

WIDTH = 400
HEIGHT = 400

blockpositions = [(350, 50), (350, 350), (50, 350), (50, 50)]
positions = itertools.cycle(blockpositions)
ship = Actor("ship", center = (200, 200))
block = Actor("block", center = (50, 50))

def draw():
    screen.clear()
    ship.draw()
    block.draw()

def move_block():
    animate(block, "bounce_end", duration = 1, pos = next(positions))
move_block()

clock.schedule_interval(move_block, 2)

def next_ship_target():
    x = random.randint(100, 300)
    y = random.randint(100, 300)
    ship.target = x, y
    target_angle = ship.angle_to(ship.target)
    target_angle += 360*((ship.angle - target_angle + 180)//360)
    animate(ship, angle = target_angle, duration = 0.5, on_finished = move_ship)

def move_ship():
    anim = animate(ship, tween = "accel_decel", duration = ship.distance_to(ship.target)/200, on_finished = next_ship_target)

next_ship_target()
pgzrun.go()
