i = 0

try:
  while True:
    print(f"{i}\r", end="")
    i += 1
except KeyboardInterrupt:
  print("FK!!!")
