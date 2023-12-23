import time


def sequential():
  """
  An example of sequential programming
  """
  s = time.perf_counter()
  print("@me")
  time.sleep(2)
  print("says hello!")
  elapsed = time.perf_counter() - s
  print("Sequential Programming Elapsed Time: " + str(elapsed) + " seconds")


sequential()
