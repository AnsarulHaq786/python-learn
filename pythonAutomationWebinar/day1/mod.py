import os

script_dir = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(script_dir)

for file in files:
    if file == ("func.py"):
        print("greeter exists!")