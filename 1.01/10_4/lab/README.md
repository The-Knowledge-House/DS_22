# Version Control Lab with Python and Git

## Objective
This lab aims to introduce you to the basics of version control using Git and GitHub. By the end of this exercise, you'll know how to:
1. Create a new repository on GitHub.
2. Clone the repository to your local machine.
3. Make changes to your Python code and commit them.
4. Push your changes back to the GitHub repository.

## Prerequisites
1. An account on [GitHub](https://github.com/).
2. [Git](https://git-scm.com/) installed on your computer.
3. Basic knowledge of Python.

## Part 1: Create a New Repository on GitHub

1. Log in to your GitHub account.
2. Click the '+' icon on the top right corner and select `New repository`.
3. Name your repository `version-control-lab`.
4. Add a description if you like.
5. Choose `Public` for the repository's visibility.
6. Initialize the repository with a README file.
7. Click `Create repository`.

## Step 2: Clone the Repository to Your Local Machine

Open your terminal or command prompt and navigate to the directory where you want to clone the repository. Then run:

```bash
git clone https://github.com/YOUR_USERNAME/version-control-lab.git
cd version-control-lab
```
Replace `YOUR_USERNAME` with your actual GitHub username.

### Step 3: Create a Simple Python Program

Using your favorite text editor or IDE, create a new Python file in the cloned directory named `hello_world.py` with the following content:

```python
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    print(hello_world())
```

## Step 4: Commit Your Changes

1. Open your terminal or command prompt and navigate to the `version-control-lab` directory if you aren't already there.
2. Run the following commands:

```bash
git add hello_world.py
git commit -m "Add hello_world Python script"
```

## Step 5: Push Your Changes to GitHub

Run the following command to push your changes to the GitHub repository:

```bash
git push origin main
```

## Bonus Challenge
1. Modify the `hello_world.py` file to take a name as an argument and greet that name. For example, `hello("Alice")` should return "Hello, Alice!".
2. Commit and push your changes as you did in Steps 4 and 5.

## Submission

This exercise will **not** be submitted for grading.