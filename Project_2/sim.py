from copy import deepcopy
import json
import numpy as np


class Simulator:
    def __init__(self, map, sticky_cubes):
        self.map = map
        self.sticky_cubes = sticky_cubes
    
    def take_action(self, action):
        # TODO implement the game logic here
        # actions +90 : 1 , 180 : 0 , -90 : -1
        # axis x : 0 , y : 1 , z : 2
        index = action[0]
        degree = action[1]
        cube1 = self.map[index]
        cube2 = self.map[index+1]
        cube3 = self.map[index+2]
        axis = None
        sticky_status = False

        if [index+1, index+2] in self.sticky_cubes:
            sticky_status = True

        for i in range(3):
            if cube1[i] != cube2[i]:
                axis = i
                break
        
        if cube3[axis] != cube2[axis]:
            if sticky_status == False:
                return
            else:
                for i in range(index+2 ,26):
                    if [i, i+1] not in self.sticky_cubes:
                        return self.take_action([degree, i])
        else:
            for i in range(index+2, 26):
                self.map[i] = self.rotate(degree, cube2, self.map[i], axis)            
     
    def rotate(self, action , center_cube, cube, axis):
        for i in range(3):
            cube[i] = cube[i] - center_cube[i]

        if action == 1:
            sin_action = 1
            cos_action = 0
        elif action == 0:
            sin_action = 0
            cos_action = -1
        else :
            sin_action = -1
            cos_action = 0
        
        if axis == 0:
            cube[1] = cube[1] * cos_action - cube[2] * sin_action
            cube[2] = cube[1] * sin_action + cube[2] * cos_action
        elif axis == 1:
            cube[0] = cube[0] * cos_action + cube[2] * sin_action
            cube[2] = cube[2] * cos_action - cube[0] * sin_action
        else :
            cube[0] = cube[0] * cos_action - cube[1] * sin_action
            cube[1] = cube[1] * cos_action + cube[0] * sin_action

        for i in range(3):
            cube[i] = cube[i] + center_cube[i]
        return cube


class Interface:
    def __init__(self):
        pass

    def copy_state(self, state):
        _copy = Simulator(None,None)
        _copy.map = deepcopy(state.map)
        _copy.sticky_cubes = deepcopy(state.sticky_cubes)
        return _copy

    def perceive(self, state):
        # TODO return what the agent will see ('map' and 'location') as json
        return json.dumps({'map':state.map , 'sticky_cubes':state.sticky_cubes})

    def goal_test(self, state):
        # TODO return if goal has been reached
        xs, ys, zs = [], [], []
        for cube in state.map:
            xs.append(cube[0])
            ys.append(cube[1])
            zs.append(cube[2])
        
        if max(xs) - min(xs) == 2:
            if max(ys) - min(ys) == 2:
                if max(zs) - min(zs) == 2:
                    return True
        return False

    def evolve(self, state, action):
        state.take_action(action)

    def valid_actions(self, state):
        degree = [-1, 0, 1]
        res=[]
        for i in range(1,25):
            for k in degree:
                res.append([i,k])
        
        return res

    def valid_state(self, state):
        axs = state.map
        return len(np.unique(axs, axis=0)) == len(axs)