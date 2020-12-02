import sys

num_lines = int(sys.stdin.readline())

data = []
unique_ppl = []

for i in range(num_lines):
    status = sys.stdin.readline().replace(" ", "").replace("\n","")
    data.append(status)
    if status[0] in ["R", "S"] and status[1:] not in unique_ppl:
        unique_ppl.append(status[1:])

start_times = dict()
end_times = dict()
done = dict()
times = dict()

for person_id in unique_ppl:
    start_times[person_id] = 0
    end_times[person_id] = 0
    done[person_id] = False
    times[person_id] = 0

for person_id in unique_ppl:
    person_id = person_id
    current_time = 0
    for line in data:
        line = line
        if line[0] == "W":
            current_time += int(line[1:]) - 1
        elif line == "R" + person_id:
            current_time += 1
            if done[person_id] in [False, None]:
                start_times[person_id] = current_time
            else:
                start_times[person_id] = current_time - (end_times[person_id] - start_times[person_id])
        elif line == "S" + person_id:
            current_time += 1
            end_times[person_id] = current_time
            done[person_id] = True
        elif line[0] in ["R", "S"]:
            current_time += 1
    times[person_id] = end_times[person_id] - start_times[person_id]

for person_id in sorted(unique_ppl):
    if data.count("R" + person_id) != data.count("S" + person_id):
        times[person_id] = -1
    print(person_id, times[person_id])