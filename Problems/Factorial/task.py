N = int(input())

counter = N - 1

while counter != 0:
	N *= counter
	counter -= 1
print(N)


