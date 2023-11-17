# directory.py

import os
from .utils import generate_random_id

def create_directory(root_dir, name_dir):
    new_dir = os.path.join(root_dir, name_dir)
    if not os.path.exists(new_dir):
        print(f"Creating directory: {new_dir}")
        os.makedirs(new_dir)
        return new_dir
    else:
        random_id = generate_random_id()
        new_name = "new-" + random_id
        return create_directory(root_dir, new_name)
