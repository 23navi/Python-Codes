import os
parent="/Users/navi/Desktop/100daysofcode"
for i in range(1,101):
    directory=f"Day{i}"
    path=os.path.join(parent, directory)
    os.mkdir(path)
    print(f"created day{i}")