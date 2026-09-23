import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    source = parts[1]
    destination = parts[2]

    if destination.endswith("/"):
        filename = os.path.basename(source)
        os.makedirs(destination, exist_ok=True)
        shutil.move(source, destination + filename)

    elif os.path.dirname(destination):
        destiny = os.path.dirname(destination)
        os.makedirs(destiny, exist_ok=True)
        shutil.move(source, destination)

    else:
        shutil.move(source, destination)
