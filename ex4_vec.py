P1 = [0, 0, 0]
P2 = [0, 0, 0]
P3 = [0, 0, 0]

P1[0] += 1
print("P1 event:", P1)

P1[0] += 1
message = P1.copy()
print("P1 sends:", message)

for i in range(3):
    P2[i] = max(P2[i], message[i])
P2[1] += 1
print("P2 receives:", P2)

P2[1] += 1
print("P2 event:", P2)

P2[1] += 1
message = P2.copy()
print("P2 sends:", message)

for i in range(3):
    P3[i] = max(P3[i], message[i])
P3[2] += 1
print("P3 receives:", P3)
