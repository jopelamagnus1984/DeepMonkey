#!/usr/bin/env python
# -*- coding: utf-8 -*-

import torch.nn as nn

class DQN(nn.Module):

    def __init__(self, s_size, a_size, h_size=256, nbr_hidden_layers=1):
        """ Neural Net used in the DQN algorithm.

        Args:
            s_size (int): size of the state space.
            a_size (int): size of the action space.
            h_size (int): size of the hidden layer.
            nbr_layers (int): nbr_hidden_layers.
        Returns:
            DQN (object): object representing a Deep Q Network.
        """

        self.layers = []

        # first layer
        layer1 = nn.Linear(s_size, h_size)
        self.layers.append(layer1)

        # layers in between
        for i in range(nbr_hidden_layers):
            layer = nn.Linear(h_size, h_size)
            self.layers.append(layer)

        # last layer
        layerN = nn.Linear(h_size, s_size)
        self.layers.append(layerN)

        return

    def forward(self, x):
        """ Computes the forward pass on a batch of states.

        Args:
            x (tensor): batch of state vector.
        Returns:
            Q (tensor): batch of Q table values for each possible action to
            take from that state.
        """

        for l in self.layers:
            x = l(x)

        return x


