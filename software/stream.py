import time

with open("test.txt", "r", buffering=1) as a:
    while True:
        print(a.line_buffering)
        line = a.buffer
        if line == "\n":
            print("no change")
            time.sleep(3)
        else:
            print(line.readlines())
            time.sleep(3)