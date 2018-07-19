import time

cycles = int()
def hanoi(discs, mainTower, target, auxTower):
  global cycles
  if discs >= 1:
    cycles += 1
    hanoi(discs - 1, mainTower, auxTower, target)
    print("[Cycle {:<3}]\tMove disc {:<5} from {:^10} to {:^10}".format(cycles, discs, mainTower, target))
    hanoi(discs - 1, auxTower, target, mainTower)


if __name__ == "__main__":
  discs = int(input("discs >  "))
  if discs <= 0:
    import sys
    sys.exit("Nothing to do.")
  start = time.time()
  hanoi(discs, "m-Tower", "t-Tower", "x-Tower")
  print("Execution time was: {:.4f}".format(time.time() - start))
  print("[m-Tower = Main Tower] - [x-Tower = Auxiliary Tower] - [t-Tower = Target Tower]")
