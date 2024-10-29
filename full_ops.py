# full_ops.py

# Usage: python3 full_ops.py c_in n_wv
# Calculate the output shape/operation count of a fully-connected layer

# Parameters:
# c_in: input channel count
# n_wv: number of weight vectors

# Output:
# The shape and operation count of a fully-connected layer

# Written by Maxwell Oross
# Other contributors: None

# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import sys  # argv


# initialize script arguments
c_in = int(sys.argv[1])
n_wv = int(sys.argv[2])

# parse script arguments
if len(sys.argv) == 3:
    c_in = int(sys.argv[1])
    n_wv = int(sys.argv[2])
else:
    print('Usage: python3 full_ops.py c_in n_wv')
    exit()

c_out = n_wv
h_out = 1
w_out = 1
muls = c_in * n_wv
adds = (c_in - 1) * n_wv
divs = 0

# Print the results
print(int(c_out))  # output channel count
print(int(h_out))  # output height count
print(int(w_out))  # output width count
print(int(adds))   # number of additions performed
print(int(muls))   # number of multiplications performed
print(int(divs))   # number of divisions performed

