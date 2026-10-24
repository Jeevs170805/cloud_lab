
# Lamport's Logical Clock

clock = [0, 0, 0]

# Process 1 performs an event
clock[0] += 1
print("P1 event:", clock[0])

# Process 1 sends a message
clock[0] += 1
message = clock[0]
print("P1 sends message with timestamp:", message)

# Process 2 receives the message
clock[1] = max(clock[1], message) + 1
print("P2 receives message. Clock:", clock[1])

# Process 2 performs another event
clock[1] += 1
print("P2 event:", clock[1])

# Process 2 sends a message to P3
clock[1] += 1
message = clock[1]
print("P2 sends message with timestamp:", message)

# Process 3 receives the message
clock[2] = max(clock[2], message) + 1
print("P3 receives message. Clock:", clock[2])
