import datetime
import os
import random
import tarfile

path = '.\\dataSet\\'
os.mkdir(path) if not os.path.exists(path) else None


def get_integer_input():
    while True:
        try:
            # value = int(input("Kaç adet dosya üretilsin? "))
            value = random.randint(2,15)
            print("Worked! " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            return value
        except ValueError:
            print("Geçerli bir tam sayı giriniz.")


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
        msisdn, priv_ip, priv_port, pub_ip, pub_port, baslangic, sure, termination_cause, target_ip, target_port,
        imsi,
        imei, lac, cell, apn, ggsn_ip, ggsn_hostname, sgsn_ip, sgsn_hostname, yy, protocol, usage_octet,
        usage_packet,
        direction, kayit_tipi, charging_id, nat_device_ip, nat_hostname)


def generate_time_stamp():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")


def saved_txt():
    data = []
    for i in range(random.randint(2, 100)):
        data.append(generate_data())
    with open(path + generate_time_stamp() + ".txt", "w") as file:
        for item in data:
            file.write(str(item) + ",\n")


def created_tar_files():
    for i in range(random.randint(2, 10)):
        saved_txt()

    files = os.listdir(path)

    with tarfile.open(path + generate_time_stamp() + ".tar", "w") as tar:
        for file in files:
            if file.endswith(".txt"):
                tar.add(os.path.join(path, file), arcname=file)

    for file_name in files:
        if file_name.endswith(".txt"):
            os.remove(os.path.join(path, file_name))


def run_function():
    for i in range(0, get_integer_input()):
        created_tar_files()


run_function()
print("It's run! " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))