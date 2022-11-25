from ai import *
from sim import *
from gui import *


sample_input_json={"coordinates": [[2, -1, -2], [1, -1, -2], [1, 0, -2], [2, 0, -2], [2, 0, -1], [2, 0, 0], [2, -1, 0], [2, -1, -1], [1, -1, -1], [0, -1, -1], [0, -1, 0], [1, -1, 0], [1, 0, 0], [1, 0, -1], [0, 0, -1], [0, 0, 0], [0, 1, 0], [-1, 1, 0], [-1, 1, -1], [0, 1, -1], [0, 1, -2], [-1, 1, -2], [-2, 1, -2], [-2, 1, -1], [-2, 1, 0], [-3, 1, 0], [-4, 1, 0]], "stick_together": [[2, 3], [7, 8], [8, 9], [11, 12], [17, 18], [23, 24], [24, 25]]}


if __name__ == "__main__":
    game = Simulator(sample_input_json['coordinates'], sample_input_json['stick_together'])
    interface=Interface()
    agent = Agent()
    gui = Graphics()

    print("initial map")
    gui.display(game)
    action_count = 0
    while not (interface.goal_test(game)):
        action = agent.act(interface.perceive(game))
        interface.evolve(game, action)
        # print(game)
        if not interface.valid_state(game): raise 'reached invalid state'
        action_count += 1
        gui.display(game)
    # return action_count

    print(
        "\nyour cost (number of actions):", action_count,
        '\n\ncurrent map state:'
    )
    gui.display(game)
