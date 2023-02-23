import psutil
import time 
import requests

while True:
    # Retrieving network connection statistics
    net_io_counters = psutil.net_io_counters()
    bytes_sent = net_io_counters.bytes_sent
    bytes_recv = net_io_counters.bytes_recv

    # Start time of the bandwidth measurement
    start_time = time.time()

    # URL to use to test the speed of the connection
    url = "https://google.com/"
    response = requests.get(url)

    # End time of the bandwidth measurement
    end_time = time.time()

    # Calculation of the bandwidth used during the measurement
    bytes_sent_new = psutil.net_io_counters().bytes_sent
    bytes_recv_new = psutil.net_io_counters().bytes_recv
    used_bandwidth = (bytes_sent_new - bytes_sent) + (bytes_recv_new - bytes_recv)
    response_time = end_time - start_time

    # Bandwidth threshold not to be exceeded
    bandwidth_threshold = 10000
    # Response time threshold not to be exceeded
    response_time_threshold = 1

    if used_bandwidth > bandwidth_threshold and response_time > response_time_threshold:
        print("La connexion est lente ! Temps de réponse :", response_time, "Bande passante utilisée :", used_bandwidth)
    else:
        print("La connexion est normale. Temps de réponse :", response_time, "Bande passante utilisée :", used_bandwidth)

    # Waiting time between each test
    time.sleep(60)