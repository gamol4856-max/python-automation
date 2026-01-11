"""import os
os.mkdir("test")"""

"""import os
folder_name = "test"
if not os.path.exists("test"):
    os.mkdir("test")
    print("folder created succsessfuly")
else:
    print("folder exist allready")
"""
"""import os
print(os.path.exists("test"))
"""

"""import os
folder = "test"
if os.path.exists("test"):
    os.rmdir(folder)
    print("Folder deleted")
else:
    print("Nothing to delete")
"""

import os
for i in range(1, 6):
   folder=f"data_{i}"
if not os.path.exists(folder):
    os.mkdir(folder)
    print(folder, "created")
else:
    print(folder, "already exists – skipped")

