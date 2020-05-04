import os
import sys
import time
from pathlib import Path


def load_urls_from_csv(filepath, encoding='UTF-8'):
    sys.stdout.write('===== getting urls from file\r\n')
    sys.stdout.flush()
    wait_for_file_to_exist(filepath)
    with open(filepath, newline='', encoding=encoding) as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def wait_for_file_to_exist(filepath, seconds=30):
    iteration = 0
    while iteration < seconds:
        iteration += 1
        try:
            with open(filepath, 'rb') as file:
                return file
        except IOError:
            time.sleep(1)  # try every second
            continue
    raise IOError('Could not access {filepath} after {seconds} seconds'.format(filepath=filepath, seconds=str(seconds)))


def ensure_folder_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def wait_for_download_finished(download_folder, seconds=30):
    iteration = 0
    while iteration < seconds:
        iteration += 1
        firefox_temp_file = sorted(Path(download_folder).glob('*.part'))
        if len(firefox_temp_file) == 0:
            return
        else:
            time.sleep(1)  # try every second
            continue
    raise IOError('Could not finish download after {seconds} seconds'.format(seconds=str(seconds)))
