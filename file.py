import concurrent.futures
import string
import random

def generate_random_filename():
     return ''.join(random.choices(string.digits, k=8))

def file_name(filename):
    content=f"this is the filename {filename}"
    with open(filename,"w")as file:
        file.write(content)
    print(f"File {filename} created.")

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        filenames = [generate_random_filename() for _ in range(5)]
        executor.map(file_name, filenames)
        
if __name__ == "__main__":
    main()
