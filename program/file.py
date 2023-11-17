# file.py

import os
from utils import generate_random_id

def create_file(root_dir, name_file):
    new_file = os.path.join(root_dir, name_file)
    if not os.path.exists(new_file):
        print(f"Creating file: {new_file}")
        with open(new_file, 'w') as file:
            pass
        return new_file
    else:
        random_id = generate_random_id()
        new_name = "file-" + random_id
        return create_file(root_dir, new_name)
