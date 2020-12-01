import sys

num_lines = int(sys.stdin.readline())

data = []
unique_ppl = []
unique_wait_time = []

for i in range(num_lines):
    status = sys.stdin.readline().replace(" ", "")
    data.append(status)
    if status[0] in ["R", "S"] and status[1:] not in unique_ppl:
        unique_ppl.append(status[1:])

start_times = dict()
end_times = dict()

for person_id in unique_ppl:
    current_time = 0
    for line in data:
        if line[0] == "W":
            current_time += int(line[1:]) - 1
        elif line == "R" + person_id:
            current_time += 1
            start_times[person_id] = current_time
        elif line == "S" + person_id:
            current_time += 1
            end_times[person_id] = current_time
        elif line[0] in ["R", "S"]:
            current_time += 1

    times = end_times[person_id] - start_times[person_id]
    print(person_id.replace("\n",""), times, start_times, end_times)