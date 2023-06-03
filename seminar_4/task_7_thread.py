from timer import timer, arr
import threading


threads = []
summa = 0
num_threads = 4


def sum_array(start_idx, end_idx):
    global summa
    for i in range(start_idx, end_idx):
        summa += arr[i]


@timer
def get_summa():
    for i in range(num_threads):
        start_idx = i * len(arr) // num_threads
        end_idx = (i + 1) * len(arr) // num_threads
        thread = threading.Thread(target=sum_array, args=(start_idx, end_idx))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    return summa


if __name__ == '__main__':
    get_summa()
