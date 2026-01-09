"""Generic Analysis Script Starter

This script is a starting point for analysis scripts.  It defines standard 
imports for a few useful libraries:  numpy, scipy, and matplotlib.

"""

# These lines import the installed version number of each library.  Can
# be commented out if desired.
from matplotlib import __version__ as mpl_version
from numpy import __version__ as np_version
from scipy import __version__ as scp_version

# Uncomment the following line to import the fft and ifft modules from
# scipy's fft library.  Use this as a model for your own scipy imports.
###
# from scipy.fft import fft, ifft

# Uncomment the following line to import the pyplot interface of
# matplotlib and call it plt.  This is the standard way of doing
# matplotlib plotting. 
###
# import matplotlib.pyplot as plt

# Uncomment the following line to import numpy and refer to it as np.
# This is the standard way of handling numpy.
###
# import numpy as np


def main():
    """
    Analysis Script Primary Function

    All of your analysis code should go in this function.  You can define 
    additional functions elsewhere to compartmentalize your code logically 
    but this is where all the work should happen.
    """

    # The following lines can be safely commented out if you do not want 
    # to print the library version numbers.  They _should_ be commented
    # out if the corresponding imports are commented out or removed.
    print(f"numpy version:  {np_version}")
    print(f"matplotlib version:  {mpl_version}")
    print(f"scipy version:  {scp_version}")


# Do not add code below this line unless you know what you are doing.
# The following lines are what allow your analysis function (main()) to
# be executed automatically when you run this script via 'uv run
# main.py' or 'python main.py'.
if __name__ == "__main__":
    main()
