import sys
#print(sys.path)
from password_gen import PwdGenerator

if __name__ == "__main__":
  gen = PwdGenerator()
  gen.generate(100)