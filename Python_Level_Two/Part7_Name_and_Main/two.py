import one

print("top-level in two.py")

one.func()

if __name__ == "__main__":
    print("two.py is being run directly")
    print(__name__)
else:
    print("two.py is being imported into another module")
