import time


def insertionsorted(a):
	length = len(a)

	for i in range(1, length):

		for x in range(0, i):

			if len(a[i]) < len(a[x]):
				move = a[i]

				for j in range(i, x, -1):
					a[j] = a[j-1]

				a[x] = move
				break

		time.sleep(0.5)
		print(a)

	return a


if __name__ == '__main__':
	a = [
		"10########",
		"8#######",
		"4###",
		"5####",
		"6#####",
		"3##",
		"7######",
		"2#",
		"9########",
		"1",
	]
	
	insertionsorted(a)


""" Output
['8#######', '10########', '4###', '5####', '6#####', '3##', '7######', '2#', '9########', '1']
['4###', '8#######', '10########', '5####', '6#####', '3##', '7######', '2#', '9########', '1']
['4###', '5####', '8#######', '10########', '6#####', '3##', '7######', '2#', '9########', '1']
['4###', '5####', '6#####', '8#######', '10########', '3##', '7######', '2#', '9########', '1']
['3##', '4###', '5####', '6#####', '8#######', '10########', '7######', '2#', '9########', '1']
['3##', '4###', '5####', '6#####', '7######', '8#######', '10########', '2#', '9########', '1']
['2#', '3##', '4###', '5####', '6#####', '7######', '8#######', '10########', '9########', '1']
['2#', '3##', '4###', '5####', '6#####', '7######', '8#######', '9########', '10########', '1']
['1', '2#', '3##', '4###', '5####', '6#####', '7######', '8#######', '9########', '10########']
"""