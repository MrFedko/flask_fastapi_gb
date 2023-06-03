import os
import multiprocessing

PATH = '../seminar_4/'


def parser_text(name: str):
    with open(name, 'r', encoding='UTF-8') as file:
        content = file.read()
        count = len(content.split())
        print(f'{name} count = {count}')


processes = []


def process_count(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            p = multiprocessing.Process(target=parser_text, args=(file_path, ))
            processes.append(p)
            p.start()


if __name__ == '__main__':
    process_count(PATH)

    for proc in processes:
        proc.join()

    for proc in processes:
        print(proc.is_alive())
