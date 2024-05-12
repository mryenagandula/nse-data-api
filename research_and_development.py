import os
from niftystocks import ns

print(ns.get_nifty_next50());

print(ns.get_nifty50())

print(ns.get_nifty_smallcap50())


print(ns.get_nifty_private_bank())

print(ns.get_nifty_psu_bank())



# # Specify the path for the new directory
# directory = "MyNestedFolder/Subfolder"
# parent_dir = "logs"  # Change this to your desired parent directory

# # Join the parent directory and the new directory
# path = os.path.join(parent_dir, directory)

# # Create the directory (including intermediate-level directories)
# os.makedirs(path)
# print(f"Directory '{directory}' created at {path}")

import time

# Start the stopwatch
start_time = time.process_time()

# Your code or process here
for i in range(1000000):
    pass

# Stop the stopwatch
end_time = time.process_time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")

