
processes = [1, 2, 3, 4]

token_holder = 1

for i in range(8):
    print("Token is with Process", token_holder)

    if token_holder == 2:
        print("Process 2 enters Critical Section")
        print("Process 2 leaves Critical Section")

    token_holder = (token_holder % len(processes)) + 1

    print("Token passed to next process")
    print()
