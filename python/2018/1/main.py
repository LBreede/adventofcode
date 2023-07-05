# --- Day 1: Chronal Calibration ---

line_list = open("input.txt", "r").read().split("\n")
adjustment_list = [int(line) for line in line_list]
freq_sum = sum(adjustment_list)

print(freq_sum)

freq = 0
freq_list = []
i = 0
while True:
    freq += adjustment_list[i % len(adjustment_list)]
    if freq in freq_list:
        break
    else:
        freq_list.append(freq)
        i += 1

# print(freq) # 73364
