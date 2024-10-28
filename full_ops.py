# full_ops.py
#
# Usage: python3 script_name.py arg1 arg2 ...
# Text explaining script usage
# Parameters:
# arg1: description of argument 1
# arg2: description of argument 2
# ...
# Output:
# A description of the script output
#
# Written by Erik Judy
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.
# import Python modules
# e.g., import math # math module
import sys
import math
# "constants"
# helper functions
## function description
# def calc_something(param1, param2):
# pass
# initialize script arguments
if len(sys.argv)==3:
  c_in = float(sys.argv[1])
  n_wv = float(sys.argv[2])
else:
  print(\
   'Usage: '\
   'python3 conv_ops.py c_in n_wv'\
  )
  exit()
# write script below this line
adds = n_wv*c_in
muls = n_wv*c_in
divs = 0
c_out = n_wv
h_out = 1
w_out = 1

print(int(c_out))
print(int(h_out))
print(int(w_out))
print(int(adds)) 
print(int(muls)) 
print(int(divs))  