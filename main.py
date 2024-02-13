import datetime
import random
import gzip
import os
import platform

platformEnum = 0

if platform.system() == "Windows":
    platformEnum = 0
elif platform.system() == "Linux":
    platformEnum = 1


def get_integer_input():
    while True:
        try:
            value = int(input("Kaç adet sıkıştırılmış dosya üretilsin? "))
            return value
        except ValueError:
            print("Geçerli bir tam sayı giriniz.")


print("Worked! " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    while True:
        input_value = get_integer_input()
        break

fileNumbers = random.randint(1, 10)

path = "C:\\Users\\user\\Desktop\\dataSet\\"

os.makedirs(path, exist_ok=True)


def generate_data():
    msisdn = random.randint(1000000000, 9999999999)
    priv_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    priv_port = random.randint(0, 65535)
    pub_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    pub_port = random.randint(0, 65535)
    baslangic = f"2024-01-{'{:02d}'.format(random.randint(1, 31))} {'{:02d}'.format(random.randint(0, 23))}:{'{:02d}'.format(random.randint(0, 59))}:{'{:02d}'.format(random.randint(0, 59))}"
    sure = random.randint(0, 86400)
    termination_cause = random.randint(1, 5)
    target_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    target_port = random.randint(0, 65535)
    imsi = ''.join(str(random.randint(0, 9)) for _ in range(15))
    imei = ''.join(str(random.randint(0, 9)) for _ in range(15))
    lac = "LAC" + ''.join(str(random.randint(0, 9)) for _ in range(3))
    cell = "CELL" + ''.join(str(random.randint(0, 9)) for _ in range(3))
    apn = random.choice(["internet", "vpn", "extranet"])
    ggsn_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    ggsn_hostname = "ggsn" + str(random.randint(1, 10)) + ".example.com"
    sgsn_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    sgsn_hostname = "sgsn" + str(random.randint(1, 10)) + ".example.com"
    yy = 2024
    protocol = random.randint(1, 3)
    usage_octet = random.randint(0, 1000000000)
    usage_packet = random.randint(0, 1000000)
    direction = random.randint(1, 2)
    kayit_tipi = random.randint(1, 3)
    charging_id = ''.join(str(random.randint(0, 9)) for _ in range(5))
    nat_device_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    nat_hostname = "nat" + str(random.randint(1, 10)) + ".example.com"

    return (
        msisdn, priv_ip, priv_port, pub_ip, pub_port, baslangic, sure, termination_cause, target_ip, target_port, imsi,
        imei, lac, cell, apn, ggsn_ip, ggsn_hostname, sgsn_ip, sgsn_hostname, yy, protocol, usage_octet, usage_packet,
        direction, kayit_tipi, charging_id, nat_device_ip, nat_hostname)


def generate_file_name():
    return path + "data" + datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")


def compress_data():
    temp_value = ""
    for i in range(random.randint(2, 100)):
        temp_value += str(generate_data()) + "\n"
    return temp_value


def generate_file():
    for i in range(fileNumbers + 1):
        file_name = f"{generate_file_name()}-{i + 1}.txt"
        with open(os.path.join(path, file_name), "w") as file:
            file.write(compress_data())


def file_list():
    return os.listdir(path)


def remove_folder(file_name):
    # os.remove(os.path.join(file_name))
    print("remove folder " + file_name)


def create_and_move_folder(folder_name):
    os.makedirs(folder_name, exist_ok=True)

    generate_file()

    for file_name in os.listdir(path):

        if file_name.endswith(".txt"):
            print("FileName:" + file_name)
            os.rename(path + file_name, os.path.join(folder_name, file_name))


def compress_file():
    folder_name = generate_file_name()
    create_and_move_folder(folder_name)

    with gzip.open(folder_name + ".gz", "wb") as gzip_file:
        for file in os.listdir():
            with open(file,"rb") as file_obj:
                gzip_file.write(file_obj.read())

    remove_folder(folder_name)


def run_function():
    compress_file()


run_function()

print("It's run! " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# **************************************************
#     def compress_file(filename):
#         base_name = os.path.splitext(filename)[0]
#         with open(filename, 'rb') as f_in:
#             with gzip.open(filename + '.gz', 'wb') as f_out:
#                 f_out.writelines(f_in)
#
#         new_compressed_filename = os.path.splitext(filename)[0] + '.gz'
#         os.rename(filename + '.gz', filename[:-4] + '.gz')
#         os.remove(filename)
#
#     dataset = generate_random_data()
#     formatted_datetime = format_datetime()
#     save_data_to_file("./dataSet/data" + formatted_datetime + ".txt", [dataset])
#     compress_file("./dataSet/data" + formatted_datetime + ".txt")
#
#
# /**************************************************
