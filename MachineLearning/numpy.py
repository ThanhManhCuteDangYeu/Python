import numpy as np
s = input()
if len(s) < 2:
    print("")
else:
    print(s[0:2] + s[-2:])