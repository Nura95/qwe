def get_data(file_name):
    time, sig_1_1, sig_1_3, sig_2_1, sig_2_2, sig_3_1, sig_3_3 = [], [], [], [], [], [], []
    with open(file_name, 'r') as text_file:
        for line in text_file:
            arr = []
            for value in line.strip().split('\t'):
                try:
                    value = float(value.strip('﻿'))
                    arr.append(value)
                except ValueError:
                    break
            if not len(arr) == 0:
                time.append(arr[0])
                sig_1_1.append(arr[1])
                sig_1_3.append(arr[2])
                sig_2_1.append(arr[3])
                sig_2_2.append(arr[4])
                sig_3_1.append(arr[5])
                sig_3_3.append(arr[6])
    return time, sig_1_1, sig_1_3, sig_2_1, sig_2_2, sig_3_1, sig_3_3