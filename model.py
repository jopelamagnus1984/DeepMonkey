#!/usr/bin/env python
# -*- coding: utf-8 -*-

import torch.nn as nn

class DQN(nn.Module):

    def __init__(self, s_size, a_size):
        """ Neural Net used in the DQN algorithm """

        self.fc1 = nn.Linear()
