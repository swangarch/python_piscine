from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(333)):
	sleep(0.005)
print()

for elem in tqdm(range(333)):
	sleep(0.005)
print()

for elem in ft_tqdm(["hello", "world", "my friend", "let's", "test"]):
	sleep(0.005)
	print(elem)
print()

for elem in tqdm(["hello", "world", "my friend", "let's", "test"]):
	sleep(0.005)
	print(elem)
print()

# print(ft_tqdm.__doc__)
# print(tqdm.__doc__)