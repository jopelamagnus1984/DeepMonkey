#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from model import DQN
from unityagents import UnityEnvironment

def main():
    """ Trains a reinforcement learning agent to solve the Unity Banana
    Environment. """

    DEFAULT_BINARY_PATH='./bin/Banana.x86_64'
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '-b',
            '--binary',
            help='path to the environment binary',
            default=DEFAULT_BINARY_PATH
            )

    args = parser.parse_args()

    # Spawn an environment for training.
    env = UnityEnvironment(file_name=args.binary)
    brain_name = env.brain_names[0]
    brain = env.brains[brain_name]

    s_size = brain.vector_observation_space_size
    a_size = brain.vector_action_space_size


    # Train the model using DQN
    print(s_size, a_size)

    return

if __name__ == '__main__':
    main()

