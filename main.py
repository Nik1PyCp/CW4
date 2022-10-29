try:
    print("start code")
    print(error)
    print("No errors")
except ImportError:
    print("We have an ImportError")
except NameError:
    print("NameError")
print("code after capsule")