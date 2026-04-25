from mpi4py import MPI

comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()

data = rank * 10

print(f"Hello from process {rank} of {size}. Data = {data}")

if rank == 0:
    print("Process 0 is the master process.")
else:
    print(f"Process {rank} sends message to master process.")