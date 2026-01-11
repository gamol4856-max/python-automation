import os

base_dir = os.getcwd()   # current working directory

for i in range(1, 501):
    folder_name = f"company_{i}"

    # folder create (if not exists)
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    # go inside folder
    os.chdir(folder_name)

    # create log.txt
    with open("log.txt", "w") as f:
        f.write(f"Log file for {folder_name}\n")

    # go back to base directory
    os.chdir(base_dir)
