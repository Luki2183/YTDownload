import sys, os
print(os.getcwd())
print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.realpath(__file__)))
print(sys.path[0])
print(os.getenv('APPDATA'))