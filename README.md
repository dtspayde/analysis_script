# analysis_script

This repository is essentially a template which can be used to create data analysis scripts in Python or Jupyter.

# Prerequisites

- `git`
    - Windows:  Download [Git for Windows](https://gitforwindows.org/index.html) and follow installation instructions.
    - Linux:  Almost certainly already installed.  Type `git --version` at the command line to make sure.
    - MacOS:  Open a `Terminal` window and type `git --version` at the command line.  If prompted, install the "command line developer tools".  You __do not__ need to install `Xcode`.
- `uv`:  See [Installation](https://docs.astral.sh/uv/getting-started/installation/) at the [uv](https://docs.astral.sh/uv/) website.
- `python` (provided by `uv`, no need to install your own)
- `dtspayde/analysis_script`
    - Make sure git is installed and operational on your computer.
    - Open a terminal window so you can access the command line.
    - Change into whatever directory you want to work in.
    - Type the following command (or copy and pasted) into your terminal and hit `Return`.
    ```bash
    git clone https://github.com/dtspayde/analysis_script.git analysis_script
    ```

    - Change into the `analysis_script` directory with `cd analysis_script`

# How to Use

## Use a Jupyter Lab Notebook
Issue the following command on the command line to start a Jupyter Lab server on your computer:
```bash
uv run jupyter lab
```
This command will install Python (if necessary), download and install the necessary supporting libraries, and start a Jupyter Server. A new window should open on your browser containing the Jupyter interface.  You may create your own Jupyter notebook or use `analysis_script.ipynb` as a starting point.

## Use a Python Script
Create your script as desired or use `analysis_script.py` as a starting point.  Execute your script with the following command:
```bash
uv run <SCRIPT>
```
where `<SCRIPT>` is the name of the Python file you want to execute, e.g. `analysis_script.py`.

# Installed Libraries
This framework automatically installs the following Python libraries so they are ready for import.
- [numpy](https://numpy.org/)
- [scipy](https://scipy.org/)
- [matplotlib](https://matplotlib.org/)
- [pandas](https://pandas.pydata.org/)
- [jupyter](https://jupyter.org/)

