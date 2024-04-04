import os
import time
import threading


def create_file_with_delay():
    time.sleep(1)
    filename = f"file_{time.time()}.txt"
    with open(filename, 'w') as file:
        file.write("This is a test file.")


start_time = time.time()
for _ in range(100):
    create_file_with_delay()
end_time = time.time()
total_time = end_time - start_time
print(f"Total time taken for sequential execution: {total_time} seconds")


def run_multithreaded():
    threads = []
    start_time = time.time()
    for _ in range(100):
        thread = threading.Thread(target=create_file_with_delay)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time
    print(
        f"Total time taken for multithreaded execution: {total_time} seconds")


run_multithreaded()
