# --- Day 4: Giant Squid ---

import aoc_helper

def get_numbers(lst):
	return lst[0].split(",")

def get_boards(lst):

	raw_boards = [x.split("\n") for x in lst[1:]]

	boards = []
	for x in raw_boards:
		board = []
		for y in x:
			row = {}
			for z in y.split():
				row[z] = 0
				# board.append(y.split())
			board.append(row)
		
		boards.append(board)
	return boards

def win_bingo(numbers, b):
	boards = b[:]
	for num in numbers:
		for board_number, board in enumerate(boards):
			cols_count = [0,0,0,0,0]
			for row in board:
				if num in row:
					row[num] = 1
					if sum(row.values()) == 5:
						winning_board = board_number
						break
				for i, val in enumerate(row.values()):
					cols_count[i] += val
			else:
				continue
			break

			if 5 in cols_count:
				winning_board = board_number
				break
		else:
			continue
		break

	accum_unmarked = 0
	for row in boards[winning_board]:
		for k, v in row.items():
			if v == 0:
				accum_unmarked += int(k)

	return accum_unmarked * int(num)

def main():
	
	linelist = aoc_helper.load_input("day04_input.txt", separator="\n\n")

	numbers = get_numbers(linelist)
	boards = get_boards(linelist)

	result_1 = win_bingo(numbers, boards)
	# result_2 = lose_bingo(numbers, boards)

	print(f"Part 1: {result_1}")
	# print(f"Part 2: {result_2}")


if __name__ == "__main__":
	main()


