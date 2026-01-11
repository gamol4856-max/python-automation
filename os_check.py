import os
import platform

print("===== SYSTEM CHECK REPORT =====")

print("OS Name           :", os.name)
print("System            :", platform.system())
print("Release           :", platform.release())
print("Version           :", platform.version())
print("Architecture      :", platform.machine())
print("Processor         :", platform.processor())

print("\n===== WORKING DIRECTORY =====")
print(os.getcwd())

print("\n===== FILES IN PROJECT =====")
for item in os.listdir():
    print("-", item)
