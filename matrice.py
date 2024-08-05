import os
import numpy as np

def generate_matrix():
    return np.random.randint(1, 100, size=(5, 5)).tolist()

def create_input_file(file_path, num_lines=100000):
    with open(file_path, 'w') as f:
        for _ in range(num_lines):
            matrix = generate_matrix()
            f.write(str(matrix) + '\n')

def generate_input_files(directory, num_files=10, num_lines=100000):
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i in range(num_files):
        file_path = os.path.join(directory, f'mat{i + 1}.in')
        create_input_file(file_path, num_lines)

if __name__ == "__main__":
    input_dir = './input'
    generate_input_files(input_dir)