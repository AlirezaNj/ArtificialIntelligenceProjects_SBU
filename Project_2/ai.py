from gui import *
from time import time
from sim import Simulator, Interface
import json
import numpy as np

# *** you can change everything except the name of the class, the act function and the sensor_data ***

class Agent:
    # ^^^ DO NOT change the name of the class ***

    def __init__(self):
        self.predicted_actions = []

    # the act function takes a json string as input
    # and outputs an action string
    # action example: [1,2,-2]
    # the first number is the joint number (1: the first joint)
    # the second number is the axis number (0: x-axis, 1: y-axis, 2: z-axis)
    # the third number is the degree (1: 90 degree, -2: -180 degree, -1000: -90000 degree)
    def act(self, percept):
        # ^^^ DO NOT change the act function above ***
        sensor_data = json.loads(percept)

        # ^^^ DO NOT change the sensor_data above ***

        alg = self.BFS_SAMPLE_CODE
    
        if self.predicted_actions == []:
            t0=time()
            initial_state=Simulator(sensor_data['map'], sensor_data['sticky_cubes'])
            self.predicted_actions = alg(initial_state)
            if self.predicted_actions is None: 
                raise Exception("No Solution found")
            print("run time:", time()-t0)

        action = self.predicted_actions.pop()

        # action example: [1,2,-2]
        return action
    
    def BFS_SAMPLE_CODE(self, root_game):
        interface=Interface()
        gui = Graphics()
        q = []
        # append the first state as (state, action_history)
        q.append([root_game, [[-1,-1]]])

        while q:
            # pop first element from queue
            node = q.pop(0)
            # get the list of legal actions
            actions_list = interface.valid_actions(node[0])
            
            # randomizing the order of child generation
            np.random.shuffle(actions_list)
            
            for action in actions_list:
                # copy the current state
                child_state = interface.copy_state(node[0])
                
                # take action and change the copied node
                interface.evolve(child_state, action)
                
                if not interface.valid_state(child_state):
                    continue
                # add children to queue
                q.append([child_state, [action] + node[1]])

                # return if goal test is true
                if interface.goal_test(child_state):
                     return [action] + node[1][:-1]
        