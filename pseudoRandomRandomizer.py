import os
import re
import numpy as np

if os.path.exists("./RAFFLE.md"):
    with open("./RAFFLE.md", 'r') as fst:
        lines = fst.readlines()
        rnd = np.random.randint(len(lines))
        while not re.match(".*?Loic.*?", lines[rnd]):
            rnd = np.random.randint(len(lines))

    print("The winner is %s, oh my god that was unexpected !" %lines[rnd])
