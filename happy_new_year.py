import random
import string
import time
import os

s = "-------    -------    -------    |     |      |    |     |          |    |     |      |    |     |          |    |     |-------    |     |    -------    |-----||          |     |    |                ||          |     |    |                |-------    -------    -------          |"
t = [0]*280

while True:
	r = ''.join(random.choice(
			string.punctuation + '         '
		) for _ in range(280))

	for idx, (c1, c2) in enumerate(zip(s, r)):
		t[idx] = t[idx] or (c1 == c2)

	for idx, tpl in enumerate(zip(r, s), start=1):
		print(tpl[t[idx-1]], end="")
		if (idx%40) == 0:
			print()

	time.sleep(0.4)
	os.system('clear')