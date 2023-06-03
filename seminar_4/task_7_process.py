import multiprocessing
from timer import timer, arr


num_processes = 4
summa = multiprocessing.Value('i', 0)


def sum_array(arr, start_idx, end_idx, sum_):
    local_sum = 0
    for i in range(start_idx, end_idx):
        local_sum += arr[i]
    with sum_.get_lock():
        summa.value += local_sum


processes = []


@timer
def multy_summ():
    for i in range(num_processes):
        start_idx = i * len(arr) // num_processes
        end_idx = (i + 1) * len(arr) // num_processes
        process = multiprocessing.Process(target=sum_array, args=(arr, start_idx, end_idx, sum_))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    return summa


if __name__ == '__main__':
    multy_summ()
