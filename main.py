try:
    print("start code")
    print(error)
    print("No errors")
except (ImportError, NameError):
    print("We have an ImportError")
print("code after capsule")