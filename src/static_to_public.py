import os
import shutil


def static_to_public(source, destination):
    if os.path.exists(destination):
        print(f"Clearing out {destination}")
        shutil.rmtree(destination)
 
    os.mkdir(destination)

    if not os.path.exists(source):
        raise ValueError("directory to copy from does not exist")
    
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)
           
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
            print(f"Copied file: {source_path} to {dest_path}")
        else:
            static_to_public(source_path, dest_path)

        


