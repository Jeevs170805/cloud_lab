
processes = [1, 2, 3]

timestamp = {1: 1, 2: 2, 3: 3}
requesting = {1: True, 2: False, 3: False}

for p in processes:
    if p == 1:
        continue

    print("Process 1 sends REQUEST to", p)

    if requesting[p] and (
        timestamp[p], p
    ) < (timestamp[1], 1):
        print("Process", p, "defers REPLY")
    else:
        print("Process", p, "sends REPLY")

print("Process 1 receives all permissions")
print("Process 1 enters Critical Section")
print("Process 1 leaves Critical Section")
print("Deferred replies are sent")
