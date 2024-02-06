import datetime
import random
import gzip
import time
import os

print("Worked! " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if not os.path.exists("dataSet"):
    os.makedirs("dataSet")


def allOperations():
    def format_datetime():
        formatted_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        return formatted_datetime

    def generate_random_data():
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

    def save_data_to_file(filename, data):
        with open(filename, 'w') as file:
            for row in data:
                file.write(','.join(map(str, row)) + '\n')

    def compress_file(filename):
        with open(filename, 'rb') as f_in:
            with gzip.open(filename + '.gz', 'wb') as f_out:
                f_out.writelines(f_in)

    dataset = generate_random_data()
    formatted_datetime = format_datetime()
    save_data_to_file("C:/Users/user/Downloads/dataSet/data" + formatted_datetime + ".txt", [dataset])
    compress_file("C:/Users/user/Downloads/dataSet/data" + formatted_datetime + ".txt")


def run_function(timeValue):
    start_time = time.time()
    while time.time() - start_time < timeValue:
        allOperations()


run_function(5)

print("It's run! " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))