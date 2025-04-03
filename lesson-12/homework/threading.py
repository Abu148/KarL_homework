#task3:
import threading


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes_in_range(start, end, result):
    primes_in_range = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes_in_range.append(number)
    result.extend(primes_in_range)


def find_primes_in_parallel(start, end, num_threads):
   
    step = (end - start + 1) // num_threads
    threads = []
    result = []


    for i in range(num_threads):
        thread_start = start + i * step
        thread_end = start + (i + 1) * step - 1 if i != num_threads - 1 else end
        thread = threading.Thread(target=find_primes_in_range, args=(thread_start, thread_end, result))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()

   
    return result


if __name__ == "__main__":
    start = 1
    end = 100
    num_threads = 4  

    primes = find_primes_in_parallel(start, end, num_threads)
    print(f"Prime numbers between {start} and {end} are: {sorted(primes)}") 





# task2:

import threading
from collections import defaultdict

def count_words_in_chunk(start_line, end_line, lines, result):
    local_count = defaultdict(int)
    for line in lines[start_line:end_line]:
        words = line.strip().split()
        for word in words:
            word = word.lower() 
            local_count[word] += 1
    

    with result_lock:
        for word, count in local_count.items():
            result[word] += count

def count_words_in_file(file_path, num_threads):

    with open(file_path, 'r') as f:
        lines = f.readlines()

    total_lines = len(lines)
    lines_per_thread = total_lines // num_threads
    threads = []
    result = defaultdict(int)
    global result_lock
    result_lock = threading.Lock()


    for i in range(num_threads):
        start_line = i * lines_per_thread
        end_line = (i + 1) * lines_per_thread if i != num_threads - 1 else total_lines
        thread = threading.Thread(target=count_words_in_chunk, args=(start_line, end_line, lines, result))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()

  
    return dict(result)


if __name__ == "__main__":
    file_path = 'large_text_file.txt'
    num_threads = 4

    word_count = count_words_in_file(file_path, num_threads)

    for word, count in word_count.items():
        print(f"'{word}': {count}")

