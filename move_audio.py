import os
import shutil


files = [f for f in os.listdir() if os.path.isfile(
    os.path.join(os.getcwd(), f))]

for file in files:
    try:
        if ".py" in file:
            pass
        elif ".txt" in file:
            pass
        else:
            shutil.move(os.path.join(os.getcwd(), file),
                        os.path.join(os.getcwd(), 'songs'))
            print(f'[MOVED]{file}')
    except:
        pass
