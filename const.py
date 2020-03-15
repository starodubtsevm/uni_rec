#!/usr/bin/env python3

import sounddevice as sd
import sys
import queue
import numpy as np
import matplotlib

fs = 8000
data_rate = 12.897
fn = fs/2
LEN_OF_BIT = int(fs/data_rate)
