import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Comando inválido!")

    _, source, destination = parts

    if destination.endswith("/"):
        filename = os.path.basename(source)
        os.mkdir(destination)
        shutil.copy(source, os.path.join(destination, filename))
        os.remove(source)

    elif os.path.dirname(destination):
        destiny = os.path.dirname(destination)
        os.makedirs(destiny, exist_ok=True)
        shutil.copy(source, destination)
        os.remove(source)
    else:
        shutil.copy(source, destination)
        os.remove(source)
