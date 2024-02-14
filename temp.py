import datetime
import random
import gzip
import sys
import tarfile
import os

maxValue = 100000
inputValue = 1


def get_integer_input():
    while True:
        try:
            value = int(input("Kaç adet dosya üretilsin? "))
            return value
        except ValueError:
            print("Geçerli bir tam sayı giriniz.")


if __name__ == "__main__":
    while True:
        number = get_integer_input() + 1
        if number > maxValue:
            print(f"Girdiğiniz değer {maxValue}'ten büyük olamaz. Lütfen {maxValue} veya daha küçük bir değer girin!")
        else:
            inputValue = number
            break

print("Worked! " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if not os.path.exists("dataSet"):
    os.makedirs("dataSet")


def all_operations():
    def format_datetime():
        return datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")



    def save_data_to_file(filename, data):
        with open(filename, 'w') as file:
            for row in data:
                file.write(',\n'.join(map(str, row)))

    def compress_file(files):

        print("Bulunan dosyalar: ")
        print(files)
        sys.exit()










        # for file in files:
        #     if file.endswith(".txt"):
        #         with tarfile.open(file + ".tar", "w") as tar:
        #             tar.add(os.path.join(".\\dataSet", file), arcname=file)
        #
        #     with open(".\\dataSet\\" + file + ".tar", "rb") as tar_dosya:
        #         with gzip.open(".\\dataSet\\" +file + ".tar.gz", "wb") as g_file:
        #             g_file.write(tar_dosya.read())
        #
        #         # os.remove(file)
        #         # os.rename(file + '.tar.gz', file[:-4] + '.tar.gz')



    for j in range(random.randint(0, 2)):
        for i in range(random.randint(2, 9)):
            dataset = [generate_random_data()]
            path = f"./dataSet/data{format_datetime()}-{i}.txt"
            save_data_to_file(path, [dataset])

        txt_files = [file for file in os.listdir(".\\dataSet\\") if file.endswith('.txt')]
        compress_file(txt_files)
        # os.remove(path)
        # os.remove(path[:-4] + ".tar")

    # for file in os.listdir(".\\dataSet\\"):
    #     os.rename(file + '.tar.gz', file[:-4] + '.tar.gz')
    #     os.remove(file[:-4] + ".tar")


def run_function(time_value):
    for i in range(time_value):
        all_operations()


run_function(inputValue)

print("It's run! " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
