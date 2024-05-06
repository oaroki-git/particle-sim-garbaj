import random
import time
import numpy
import matplotlib
import matplotlib.pyplot as plt
import tkinter
import yaml

import particlerules.rules as rules

try:
    with open(".\\config.yml", "r") as file:
        dump = yaml.safe_load(file)
        WIDTH = dump["dimensions"]["x"]
        HEIGHT = dump["dimensions"]["y"]
        SCALE = dump["scale"]
        GRAVITY = dump["gravity"]
        DENSITY = dump["density"]
        TIMEOUT = dump["seconds_between_frames"]
except:
    print("make sure your config is valid!(and that you actually have a config lol)\nthe format is:\nwidthxheight\nscale\n\ngravity\ndensity\ntimeout")
    exit()

def probability(threshold):
    num = random.randint(1, 100)
    if num >= 100 - threshold:
        return True
    return False

def draw_grid(arr):
    pass

def apply_rules(arr, rule, *args):
    active = False
    for row in range(arr.shape[0], -1, -1):
        for col in range(arr.shape[1]):
            if rule(arr, row, col, args[0]):
                active = True
    return active

cells = numpy.zeros((HEIGHT, WIDTH), dtype=numpy.bool_)
for row in range(HEIGHT):
    for col in range(WIDTH):
        cells[row, col] = probability(DENSITY)

matplotlib.use("TkAgg")
matplotlib.rcParams['toolbar'] = "None"
plt.figure(figsize=(SCALE*WIDTH / 100, SCALE * HEIGHT/100))
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
tk_instance = plt.get_current_fig_manager().window
tk_instance.title("little baby particle sim")
tk_instance.iconbitmap(".\\terminal.ico")
image = plt.imshow(cells, cmap="binary")
image.axes.get_xaxis().set_visible(False)
image.axes.get_yaxis().set_visible(False)

step = 1
active = True
while active:
    image.set_data(cells)
    active = apply_rules(cells, rules.sand_rule, int(step))
    step += GRAVITY
    plt.draw()
    plt.pause(TIMEOUT)

tkinter.messagebox.showinfo("particle sim", "simulation ended, you can close properly now")
plt.show()
