from re import findall
from dateutil import parser as date_parser
from collections import defaultdict
from datetime import datetime

def parse_line(line):
    time_stamp, _, guard_id, woke_up, fell_asleep = \
    findall(r"\[(.*)\] (Guard #(\d+) begins shift)?(wakes up)?(falls asleep)?", line)[0]
    return date_parser.parse(time_stamp), int(guard_id) if guard_id else 0, bool(woke_up), bool(fell_asleep)


def dumbest_guard(file):

    history = {}

    for line in file:
        tmstmp, guard_id, woke_up, fell_asleep = parse_line(line)
        history[tmstmp] = (guard_id, woke_up, fell_asleep)

    sleep_totals = defaultdict(int) # { guard_id : total_minutes_slept }
    minute_totals = defaultdict(lambda : defaultdict(int)) # { guard_id : { minute : count }}

    active_guard_id = -1
    prev_tmstmp = None

    for curr_tmstmp in sorted(history):
        guard_id, woke_up, fell_asleep = history[curr_tmstmp]

        if guard_id: # if a guard id exists, then she just started her shift and she is awake
            active_guard_id = guard_id
        elif woke_up: # if a guard woke up, that implies that he was asleep before 
            sleep_totals[active_guard_id] += (curr_tmstmp.minute - prev_tmstmp.minute)

            for m in range(prev_tmstmp.minute, curr_tmstmp.minute):
                minute_totals[active_guard_id][m] += 1

        prev_tmstmp = curr_tmstmp

    # part 1
    sleepiest_guard = max(sleep_totals.items(), key=lambda tup : tup[1])[0] # sort by time slept
    sleepiest_minute = max(minute_totals[sleepiest_guard], key=minute_totals[sleepiest_guard].get)
    print(f"Strategy 1: { sleepiest_guard * sleepiest_minute }")

    # part 2
    most_consistent_guard = max(minute_totals.items(), key=lambda kv : kv[1][max(kv[1], key=kv[1].get)])[0]
    most_consistent_time = max(minute_totals[most_consistent_guard], key=minute_totals[most_consistent_guard].get)
    print(f"Strategy 2: { most_consistent_guard * most_consistent_time }")


if __name__ == "__main__":
    with open("input/day_4.txt") as f:
        dumbest_guard(f)
