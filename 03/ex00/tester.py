from S1E9 import Character, Stark

Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)

#------------------------ERROR TEST---------------------------
try:
	hodor1 = Character("hodor")
except Exception as e:
	print("Error:", e)

try:
	hodor2 = Stark()
except Exception as e:
	print("Error:", e)

try:
	hodor3 = Stark("Lyanna", False, False)
except Exception as e:
	print("Error:", e)