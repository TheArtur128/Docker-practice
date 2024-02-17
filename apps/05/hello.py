from os import getenv


name = getenv("NAME", "unknown")
print(f"Hello {name}!")

