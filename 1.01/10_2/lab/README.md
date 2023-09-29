# installations-lab

All data scientists should be well aware of virtual environments. Environments allow us to quickly set ourselves up with project requirements and save us hours of development effort. 

Always create or activate an environment before you begin coding. Equate this with brushing your teeth.

## Objective
This lab aims to introduce you to virtual environments. By the end of this exercise, you will be able to: 
1. Create a virtual environment with preset packages.
2. Activate your environment.
3. Make changes to your environment via `pip`.
4. Deactivate your environment. 

## Prerequisites
* VSCode. If you have not installed VSCode yet, click [here](https://code.visualstudio.com/download) and select your operating system (OS).
* Git. If you have not installed git yet, click [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and follow the listed instructions according to your OS.
* Anaconda. If you have not installed Anaconda yet, click [here](https://docs.anaconda.com/free/anaconda/install/index.html) and follow the listed instructions according to your OS.

## Part 1: Add conda to the path

If you did not check off the "Add Anaconda to Path" checkbox during installation, you must do this now.

Follow the respective guides based on your operating system:

* [Windows](https://saturncloud.io/blog/setting-up-anaconda-path-environment-variable-in-windows-a-guide/)
* [MacOS](https://saturncloud.io/blog/adding-anaconda-to-your-path-a-guide-for-data-scientists/#:~:text=On%20macOS%20and%20Linux%3A%20Open,path%20to%20your%20Anaconda%20installation.)

Note, that you must restart your terminal/VSCode for this change to take effect. After restarting, verify that your installation works by opening your `zsh` or `git bash` terminals and running:

```bash
conda --version
```

If this results in an error, this means that your setup is not complete.

## Part 2: Create & activate a conda environment

Now that you can run `conda` commands in your terminal, we will begin by creating a conda environment. 

Notice the `environment.yml` file in this folder. This file outlines exactly which Python [packages](https://www.geeksforgeeks.org/python-packages/) we will use throughout the fellowship. 

To get started, follow the respective guide starting at [step 3](https://saturncloud.io/blog/how-to-create-a-conda-environment-based-on-a-yaml-file-a-guide-for-data-scientists/#step-3-create-the-conda-environment).

As our conda environment is named `ds23`, you will run the following command to activate your environment.

```bash
conda activate ds23
```

Going forward, you will always activate an environment before coding.

## Part 3: Verify and Deactivate

To verify that this environment has been set up properly, run the following command in your terminal.

```bash
python verify.py
```

If you see the success message `SUCCESS!``, your environment is functioning properly. Deactivate it by closing your terminal or by running:

```bash
conda deactivate
```

## Submission

This exercise will **not** be submitted for grading. However, you will not be able to run code without creating an environment.

If you are done early, feel do guide your peers in completing this workflow.