import os
from datetime import datetime

NUM_DISHES = 2


def main() -> None:
    """Create a directory and a log file for today's subculture."""

    time_now = datetime.now()
    folder_name = time_now.strftime("%m-%d")
    folder_path = os.path.join(os.getcwd(), folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Directory '{folder_name}' created.")
    else:
        print(f"Directory '{folder_name}' already exists.")

    for i in range(NUM_DISHES):
        dish = f"dish-{chr(65 + i)}"
        dish_path = os.path.join(folder_path, dish)
        if not os.path.exists(dish_path):
            os.makedirs(dish_path)
            print(f"Subdirectory '{dish}' created.")
        else:
            print(f"Subdirectory '{dish}' already exists.")

    file_name = f"log_{time_now.strftime('%Y_%m_%d')}.txt"
    file_path = os.path.join(folder_path, file_name)

    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(time_now.strftime("%Y-%m-%d") + "\n\n")
            for i in range(NUM_DISHES):
                dish = f"dish-{chr(65 + i)}"
                f.write(f"{dish}\n")
                f.write("cell type: \n")
                f.write("medium type: \n")
                f.write("culture date: \n")
                f.write("p = \n")
                f.write("confluence: \n\n")
            f.write("Activity:\n")
        print(f"File '{file_name}' created.")
    else:
        print(f"File '{file_name}' already exists.")


if __name__ == "__main__":
    main()
