# DeepMonkey
An agent that collects bananas, trained using the famous DQN algorithm.

## Project details
DeepMonkey is a reinforcement learning agent that solves 
the Unity Banana environment. DeepMonkey accomplishes this by using an
algorithm called Deep Q Learning.

### Environment Description
The DeepMonkey agent lives in a world where the following rules apply:

1. The world is filled with bananas of 2 types; yellow and blue. Yellow 
   bananas award +1 point and blue bananas award -1 point.

2. DeepMonkey can move into the world by taking the following actions:
    a. Move forward.
    b. Move backward.
    c. Move left.
    d. Move right.
   The cardinality of the action space is thus 4.

3. DeepMonkey observes the environment through a state vector of dimension 37.
   The state vector includes information about the *velocity* of the agent and 
   the *locations* of banana's through ray tracing information. The cardinality
   of the observation space is thus 37.

The goal of the agent is to collect as much reward as it can. The environment
is considered *solved* when the agent collects an average reward of +13, over
the last 100 episodes.

## Getting Started
installation instructions

## Instruction
how to run the training code

## Author
Jonathan Pelletier (@jopelamagnus)
