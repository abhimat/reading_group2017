#!/usr/bin/env python

import numpy as np

def cabinet_trial():
    ball = ''
    drawer = -1
    
    # Pick drawer
    drawer = np.random.randint(1, high=4)
    
    # Pick ball
    if drawer == 1:
        ball = 'red'
    elif drawer == 3:
        ball = 'blue'
    else:
        ball_pick = np.random.random()
        if ball_pick < 0.5:
            ball = 'red'
        else:
            ball = 'blue'
    
    return (drawer, ball)


# Perform trials
num_trials = 10000

drawers_arr = np.empty(num_trials, dtype=int)
balls_arr = np.empty(num_trials, dtype=object)

for cur_trial in range(num_trials):
    (drawer, ball) = cabinet_trial()
    ## Store out trial results
    drawers_arr[cur_trial] = drawer
    balls_arr[cur_trial] = ball


# Calculate interesting values
## Pick out red balls trials
red_balls = np.where(balls_arr == 'red')
num_passing_balls = len(balls_arr[red_balls])

## From red balls trials, pick out drawer 1 trials
num_passing_drawers = len(drawers_arr[np.where(drawers_arr[red_balls] == 1)])

## Calculate fraction
passing_fraction = float(num_passing_drawers)/float(num_passing_balls)
print('p(drawer = 1 | ball = red) = {0:.4f}'.format(passing_fraction))