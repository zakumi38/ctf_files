import os

print(type(os.popen("echo 123").read()))
print(os.system("echo 123"))