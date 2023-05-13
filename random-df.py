# generate a file or a directory depend on the parameter pass
# add root directory to the environment path
# type f or d in the any directory to create a random file or directory 

import os
import logging
import datetime
import random
import string
import argparse


# Get the directory where the current script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create the "logs" directory if it doesn't exist
logs_dir = os.path.join(current_dir, "logs")
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Set up logging
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



def create_directory(root_dir, name_dir):
    new_dir = os.path.join(root_dir, name_dir)
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    else:
        # TODO generate new name
        random_id = generate_random_id()
        create_directory(root_dir, directory_name(random_id))


def create_file(root_dir, name_file):
    new_file = os.path.join(root_dir, name_file)
    if not os.path.exists(new_file):
        file = open(new_file, 'w')
        file.close()
    else:
        # TODO generate new name
        random_id = generate_random_id()
        create_file(root_dir, file_name(random_id))


def generate_random_id(length=4):
    letters_and_digits = string.ascii_letters + string.digits
    random_name = ''.join(random.choice(letters_and_digits)
                          for i in range(length))
    random_name = str.upper(random_name)
    return random_name


def file_name(random_id):
    return "file-"+random_id


def directory_name(random_id):
    return "new-"+random_id


def main():
    # default directory
    default_directory = r"D:\\"
    parser = argparse.ArgumentParser(description="Simple command line utility")
    # The 'nargs' parameter is set to '?' to make the argument optional
    parser.add_argument("-root_dir", type=str, default=default_directory,
                        nargs='?', help="directory to scan")
    parser.add_argument("-ford", type=str , help="for file")
    args = parser.parse_args()
    root_dir = args.root_dir
    ford = args.ford
    logging.info(f"--> {ford}")
    logging.info(f"--> {root_dir}")

    random_id = generate_random_id()
    if ford == "f" :
        # Block of code when 'f' is defined
        logging.info(f"creating file")
        create_file(root_dir, file_name(random_id))

    elif ford == "d":
        # Block of code when 'd' is defined
        logging.info(f"creating directory")
        create_directory(root_dir,directory_name(random_id))

    else:
        # Block of code when neither 'f' nor 'd' is defined
        logging.error(f" Neither 'f' nor 'd' is defined, a parameter argument is necesary for file or directory creation")


if __name__ == "__main__":
    main()
