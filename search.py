import multiprocessing
import os

def search_keyword_in_file(keyword, file):
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if keyword in line:
                print(f'Ключевое слово "{keyword}" найдено в файле {file}')
                break

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Поиск ключевого слова в текстовых файлах с использованием multiprocessing.")
    parser.add_argument("keyword", help="Ключевое слово для поиска")
    parser.add_argument("files", nargs='+', help="Список файлов для поиска ключевого слова")
    args = parser.parse_args()

    keyword = args.keyword
    files = args.files

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

    for file in files:
        pool.apply_async(search_keyword_in_file, args=(keyword, file))

    pool.close()
    pool.join()