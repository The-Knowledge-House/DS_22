# verson-control-lab

## Objective
Introduce version control basics using Git and GitHub. By the end of this lab, you should:
1. Setup Git with your personal details.
2. Create and use a personal access token on GitHub.
3. Know how to create, clone, commit to, and push from a repository.

## Prerequisites
* An account on [GitHub](https://github.com/).
* [Git](https://git-scm.com/) installed on your computer.

## Part 1: Setting Up Git

Before using Git, you should configure your name and email address as they'll be associated with your commits. 

Open your terminal or command prompt and run:

```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

Replace "Your Name" with your actual name and "youremail@example.com" with the email address that you used when signing up for GitHub.

## Part 2: Creating a Personal Access Token on GitHub

1. Log in to your GitHub account.
2. Click on your profile picture in the top right and select `Settings`.
3. In the left sidebar, click on `Developer settings`.
4. Click on `Personal access tokens` in the left sidebar.
5. Click the `Generate new token` button.
6. Give your token a descriptive name.
7. Under scopes, select the checkbox `repo` to grant access to your repositories.
8. Click the `Generate token` button at the bottom.
9. **Important**: Copy the generated token and store it somewhere safe. You won't be able to see it again!

## Part 3: Use the Token with Git

When you clone or push to a repository for the first time, you'll be prompted for a username and password. 

- For the username: Enter your GitHub username.
- For the password: **Use the personal access token you just created**, not your GitHub password.

## Part 4: Create a New Repository on GitHub

Follow the [listed instructions](https://docs.github.com/en/get-started/quickstart/create-a-repo) to create a repository called `version-control-lab` in your GitHub profile.

## Part 5: Clone the Repository

Follow the the [listed instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to clone the `version-control-lab` repository to your local machine.

## Part 6: Copy over tdsp-template to cloned repo

Using your file navigator or terminal, copy the folders and files in the `tdsp-template` to your `version-control-lab` repository.

## Part 7: Commit and Push

Follow the [instructions](https://dev.to/mrfrontend/git-101--step-2-add-stage-commit--push-3p3p) starting at "Check local changes" to add, commit, and push the `tdsp-template` files and folders to your GitHub repository.

## Bonus Challenge
Create a repository for project 1 and push the template code provided from canvas. 

## Submission

This exercise will **not** be submitted for grading.