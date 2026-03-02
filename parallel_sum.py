from multiprocessing import Process, Queue

def partial_sum(start, end, q, pid):
    s = sum(range(start, end + 1))
    print(f"Process {pid}: sum({start} to {end}) = {s}")
    q.put(s)

if __name__ == "__main__":
    q = Queue()

    # Membagi tugas menjadi 2 proses
    p1 = Process(target=partial_sum, args=(1, 3, q, 1))
    p2 = Process(target=partial_sum, args=(4, 5, q, 2))

    # Memulai proses
    p1.start()
    p2.start()

    # Menunggu proses selesai
    p1.join()
    p2.join()

    # Menggabungkan hasil
    total = q.get() + q.get()
    print("Final Parallel Sum =", total)
