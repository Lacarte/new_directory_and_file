# main.py

import logging
from program.utils import setup_logging, parse_args, generate_random_id
from program.directory import create_directory
from program.file import create_file


if __name__ == "__main__":
    setup_logging()
    args = parse_args()
    root_dir = args.root_dir
    file_or_directory = args.file_or_directory
    logging.info(f"root_dir : --> {root_dir}")
    logging.info(f"file_or_directory option d/f --> {file_or_directory}")

    random_id = generate_random_id()
    if file_or_directory == "f":
        logging.info("Entering file creation")
        created_file = create_file(root_dir, "file-" + random_id)
        logging.info(f"File created: {created_file}")
    elif file_or_directory == "d":
        logging.info("Entering directory creation")
        created_dir = create_directory(root_dir, "new-" + random_id)
        logging.info(f"Directory created: {created_dir}")
    else:
        logging.error("Neither 'f' nor 'd' is defined, a parameter argument is necessary for file or directory creation")
