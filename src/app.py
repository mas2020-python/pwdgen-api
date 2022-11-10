import sys
#print(sys.path)
from config import Config

# global properties
config = Config()

if __name__ == "__main__":
  print(config.app_config["log"])