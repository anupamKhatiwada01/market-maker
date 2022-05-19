# What input should this application take?
# It will take the below parameters in order

# Current target,average,current quantity possesed, the new price of the stock, the quantity to buy

import sys
from profit_generator import profit_generated


if len(sys.argv)!=6:
  raise Exception("Please enter the necessary arguments.")

profit_generated(sys.argv[1:])