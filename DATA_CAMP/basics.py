""" DataCamp - notes from foundation courses """

import os

# --------------------------------------------------------
# List comprehensions
# --------------------------------------------------------


num_list = [num ** 2 for num in range(1000) if num % 2 == 0]
print(num_list)


# --------------------------------------------------------
# Other
# --------------------------------------------------------


def list_files_in_wd():
    """ list all files in the working directory """
    print(os.listdir(os.getcwd()))
