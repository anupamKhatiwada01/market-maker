import sys
from profit_generator import profit_generated


if len(sys.argv)!=6:
  raise Exception("Please enter the necessary arguments.")

profit_generated(sys.argv[1:])