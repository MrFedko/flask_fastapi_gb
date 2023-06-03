import os
import threading

PATH = '../seminar_4/'


def parser_text(name: str):
    with open(name, 'r', encoding='UTF-8') as file:
        content = file.read()
        count = len(content.split())
        print(f'{name} count = {count}')


threads = []


def threads_count(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            t = threading.Thread(target=parser_text, args=(file_path, ))
            threads.append(t)
            t.start()


if __name__ == '__main__':
    threads_count(PATH)

    for thread in threads:
        thread.join()

    for thread in threads:
        print(thread.is_alive())
