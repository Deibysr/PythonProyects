#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input().strip()
    count = Counter(s)
    common_chars = count.most_common()

    # Sort primarily by count (descending), then by character (ascending)
    common_chars = sorted(common_chars, key=lambda x: (-x[1], x[0]))

    # Print the top 3 most common characters
    for char, freq in common_chars[:3]:
        print(char, freq)
