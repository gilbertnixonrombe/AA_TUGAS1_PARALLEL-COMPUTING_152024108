def bankers_algorithm(available, maximum, allocation):
    n = len(allocation)      # jumlah process
    m = len(available)       # jumlah jenis resource

    # Hitung Need matrix
    need = [
        [maximum[i][j] - allocation[i][j] for j in range(m)]
        for i in range(n)
    ]

    work = available[:]          # salinan available resource
    finish = [False] * n         # status process selesai / belum
    safe_sequence = []           # urutan aman

    print("=== BANKER'S ALGORITHM EXECUTION ===")
    print(f"Initial Available Resources: {work}\n")

    print("Need Matrix:")
    for i in range(n):
        print(f"P{i}: {need[i]}")
    print()

    step = 1
    while len(safe_sequence) < n:
        found = False

        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                print(f"Step {step}: Process P{i} can execute")
                print(f"  Need[{i}] = {need[i]} <= Available = {work}")
                print(f"  P{i} finishes, then releases Allocation[{i}] = {allocation[i]}")

                # Resource dikembalikan ke sistem
                for j in range(m):
                    work[j] += allocation[i][j]

                print(f"  New Available Resources: {work}\n")

                safe_sequence.append(i)
                finish[i] = True
                found = True
                step += 1

        if not found:
            print("System is NOT in a safe state.")
            return False, []

    print("System is in a SAFE state.")
    print("Safe Sequence:", " -> ".join(f"P{i}" for i in safe_sequence))
    return True, safe_sequence


# Data contoh
available = [3, 3, 2]

maximum = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]

allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

bankers_algorithm(available, maximum, allocation)