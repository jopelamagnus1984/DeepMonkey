#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from model import DQN
from unityagents import UnityEnvironment
from collections import deque

def main():
    """ Trains a reinforcement learning agent to solve the Unity Banana
    Environment. """

    BINARY_PATH_DEFAULT='./bin/Banana.x86_64'
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '-b',
            '--binary',
            help='path to the environment binary',
            default=BINARY_PATH_DEFAULT
            )

    MEMORY_SIZE_DEFAULT=1048576 # 2**20
    parser.add_argument(
            '-m',
            '--memory-size',
            help='Size of the replay memory',
            type=int,
            default=MEMORY_SIZE_DEFAULT
            )

    args = parser.parse_args()

    # Spawn an environment for training.
    env = UnityEnvironment(file_name=args.binary)

    return

def deepqn_train(env, model_class, memory_size):
    """ trains a deep q network on the given environment

    Args:
        env (object): A Unity environment for model training.
        model_class (class): The model type to use for training
    """

    # Extract the state space and action space size.
    brain_name = env.brain_names[0]
    brain = env.brains[brain_name]

    s_size = brain.vector_observation_space_size
    a_size = brain.vector_action_space_size

    # Instanciate models.
    target_model = model_class(s_size, a_size)
    action_value_model = model_class(s_size, a_size)

    # Initialize the replay memory.
    D = deque(maxlen=memory_size)

    # train the model.
    info = env.reset(train_mode=True)
    cur_state = info.vector_observations[0]
    reward = 0

if __name__ == '__main__':
    main()

