# --- Day 4: Repose Record ---

import re


def process_data(file):
    with open(file) as fp:
        lines = sorted(fp.read().split("\n"))

    guard = -1
    sleep_time = 0
    curr_date = None
    dic = {}

    for line in lines:
        result = re.search(r"\[(\d\d\d\d-\d\d-\d\d) \d\d:(\d\d)\] (.+)", line)
        date, minute, description = result.groups()
        minute = int(minute)

        if "begins shift" in description:
            guard = int(re.search(r"\d+", description).group())

        elif "falls asleep" in description:
            sleep_time = minute

        elif "wakes up" in description:

            if date != curr_date:
                curr_date = date

            sleep_list = [i for i in range(sleep_time, minute)]

            if date not in dic:
                dic[date] = {}

            if guard not in dic[curr_date]:
                dic[curr_date][guard] = []

            dic[curr_date][guard] += sleep_list

    return dic


def find_laziest_guard(date_dic):
    dic = {}
    for date, guard_dic in date_dic.items():
        for guard, times in guard_dic.items():
            if guard not in dic:
                dic[guard] = 0
            dic[guard] += len(times)
    sorted_dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}
    return list(sorted_dic.keys())[-1]


def find_laziest_minute_from_guard(date_dic, guard_id):
    minutes_dic = accum_all_minutes_per_guard(date_dic)
    minutes_lst = minutes_dic[guard_id]
    return max(set(minutes_lst), key=minutes_lst.count)


def accum_all_minutes_per_guard(date_dic):
    dic = {}
    for date, guard_dic in date_dic.items():
        for guard, times in guard_dic.items():
            if guard not in dic:
                dic[guard] = []
            dic[guard] += times
    return dic


def find_guard_and_minute(date_dic):
    minutes_dic = accum_all_minutes_per_guard(date_dic)

    guard = -1
    amount = 0
    minute = -1

    for k, v in minutes_dic.items():
        m = max(set(v), key=v.count)
        a = v.count(m)
        if a > amount:
            amount = a
            minute = m
            guard = k
    return guard, minute


date_dic = process_data("day04_input.txt")
guard = find_laziest_guard(date_dic)
minute = find_laziest_minute_from_guard(date_dic, guard)

print(guard * minute)

guard, minute = find_guard_and_minute(date_dic)

print(guard * minute)
