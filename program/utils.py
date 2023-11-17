# utils.py

import os
import logging
import datetime
import random
import string
import argparse

def setup_logging():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logs_dir = os.path.join(current_dir, "logs")
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(
                os.path.join(
                    logs_dir,
                    f"log-{datetime.datetime.now().strftime('%Y-%m-%d')}.log"
                ),
                mode="w",
            ),
            logging.StreamHandler(),
        ],
    )

def generate_random_id(length=4):
    letters_and_digits = string.ascii_letters + string.digits
    random_name = ''.join(random.choice(letters_and_digits) for i in range(length))
    random_name = str.upper(random_name)
    return random_name

def parse_args():
    default_directory = r"D:\\"
    parser = argparse.ArgumentParser(description="Simple command line utility")
    parser.add_argument("-root_dir", type=str, default=default_directory, nargs='?', help="directory to scan")
    parser.add_argument("-file_or_directory", type=str, default="d", help="f or d parameter meaning file or directory")
    return parser.parse_args()
