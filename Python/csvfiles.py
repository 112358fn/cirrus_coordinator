import csv
from datetime import datetime as dt

keys = ['sensor', 'hour', 'min', 'sec', 'day', 'month', 'year', 'temp', 'humidity', 'val1', 'val2', 'val3', 'val4',
        'val5', 'val6']

keys_new = ['date', 'temp', 'humidity', 'val1', 'val2', 'val3', 'val4', 'val5', 'val6']


def store(filename, values):
    tm = dt.now()
    vals = [tm.hour, tm.minute, tm.second, tm.day, tm.month, tm.year]
    values.update(dict(zip(keys[1:7], vals)))
    with open(filename, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys, restval=0.0, extrasaction='ignore')
        writer.writerow(values)


def store_new(filename, values):
    with open(filename, 'a') as csvfile:
        values['date'] = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        writer = csv.DictWriter(csvfile, fieldnames=keys_new, restval=0.0, extrasaction='ignore')
        writer.writerow(values)


def readrate(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            value = int(row[1])
    return value
