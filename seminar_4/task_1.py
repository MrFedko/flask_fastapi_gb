import threading
import requests


URL_LIST = ["https://gb.ru",
            "https://ya.ru",
            "https://google.com",
            "https://mail.ru",
            "https://vk.ru",
            "https://rambler.ru"]


def parser_url(url: str, name: str):
    response = requests.get(url)
    with open(name, 'w', encoding='UTF-8') as file:
        file.write(response.text)


threads = []


if __name__ == '__main__':
    for i, url in enumerate(URL_LIST):
        t = threading.Thread(target=parser_url, args=(url, f'thread-{i}.txt'))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
