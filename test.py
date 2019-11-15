# import subprocess, threading
# state = True

# def checker(thread):
#     global state

#     while state:

#         if thread.is_alive():
#             print("alive")
#         else:
#             print("dead")
#             state = False

# def work():

#     command = "python \"C:\\Users\\ayieko\\Projects And  Research\\PycharmProjects\\Guthub-Repo-Auto-Creator\\test2.py\""
#     print(command)
#     subprocess.run(command, shell=True)

# th1 = threading.Thread(target=work)
# th1.start()
# checker(th1)

import os

os.system("cmd")