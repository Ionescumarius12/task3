import os
import time
from multiprocessing import Pool
from threading import Thread
from queue import Queue

def process_matrix_file(file_path, output_dir):
    # Replace this with your actual file processing logic
    with open(file_path, 'r') as f:
        matrix = [line.strip() for line in f.readlines()]
    
    # Perform some operation on the matrix
    result = [row.upper() for row in matrix]
    
    # Write the result to a new file
    output_file_path = os.path.join(output_dir, os.path.basename(file_path) + '.out')
    with open(output_file_path, 'w') as f:
        f.write('\n'.join(result))

def process_files_sequentially(input_dir, output_dir):
    files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith('.in')]
    for f in files:
        process_matrix_file(f, output_dir)

def process_files_in_parallel(input_dir, output_dir, use_multiprocessing):
    files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith('.in')]
    
    if use_multiprocessing:
        with Pool() as pool:
            pool.starmap(process_matrix_file, [(f, output_dir) for f in files])
    else:
        queue = Queue()
        threads = []
        
        for f in files:
            thread = Thread(target=lambda file_path, output_dir: process_matrix_file(file_path, output_dir), args=(f, output_dir))
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()

if __name__ == "__main__":
    input_dir = './input'
    output_dir = './output'

    os.makedirs(output_dir, exist_ok=True)

    # Sequential processing
    start_time = time.time()
    process_files_sequentially(input_dir, output_dir)
    end_time = time.time()
    print(f"Sequential processing time: {end_time - start_time} seconds")

    # Multiprocessing
    start_time = time.time()
    process_files_in_parallel(input_dir, output_dir, use_multiprocessing=True)
    end_time = time.time()
    print(f"Multiprocessing time: {end_time - start_time} seconds")

    # Multithreading
    start_time = time.time()
    process_files_in_parallel(input_dir, output_dir, use_multiprocessing=False)
    end_time = time.time()
    print(f"Multithreading time: {end_time - start_time} seconds")