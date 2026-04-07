from __future__ import annotations

import math
import os
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass
from typing import Iterable, List


@dataclass
class WorkerResult:
    worker_pid: int
    chunk_id: int
    input_data: list[int]
    output_data: list[int]
    elapsed_ms: float


def split_into_chunks(values: list[int], chunk_size: int) -> list[list[int]]:
    return [values[i:i + chunk_size] for i in range(0, len(values), chunk_size)]


def heavy_transform(chunk_id: int, values: list[int]) -> WorkerResult:
    start = time.perf_counter()

    transformed: list[int] = []
    for value in values:
        acc = 0.0
        for i in range(1, 25000):
            acc += math.sqrt(value * i) / (i + 1)
        transformed.append(round(acc))

    elapsed_ms = (time.perf_counter() - start) * 1000
    return WorkerResult(
        worker_pid=os.getpid(),
        chunk_id=chunk_id,
        input_data=values,
        output_data=transformed,
        elapsed_ms=elapsed_ms,
    )


def run_demo(dataset: list[int], max_workers: int = 4, chunk_size: int = 4) -> list[WorkerResult]:
    chunks = split_into_chunks(dataset, chunk_size)
    results: list[WorkerResult] = []

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        future_map = {
            executor.submit(heavy_transform, chunk_id, chunk): chunk_id
            for chunk_id, chunk in enumerate(chunks, start=1)
        }
        for future in as_completed(future_map):
            results.append(future.result())

    results.sort(key=lambda item: item.chunk_id)
    return results


def main() -> None:
    dataset = list(range(2, 34, 2))
    results = run_demo(dataset, max_workers=4, chunk_size=4)

    print("DATA PARALLELISM DEMO (PYTHON)")
    print("=" * 72)
    print(f"Main PID       : {os.getpid()}")
    print(f"Dataset        : {dataset}")
    print("Model          : Data parallelism using ProcessPoolExecutor")
    print("Goal           : Different workers execute different chunks of the same task")
    print("-" * 72)

    for item in results:
        print(f"Task {item.chunk_id}")
        print(f"  Worker PID   : {item.worker_pid}")
        print(f"  Input chunk  : {item.input_data}")
        print(f"  Output chunk : {item.output_data}")
        print(f"  Runtime      : {item.elapsed_ms:.2f} ms")
        print("-" * 72)

    print("SUMMARY")
    print("Each worker handled a different subset of the even dataset.")
    print("This proves the code executed different data in parallel.")


if __name__ == "__main__":
    main()
