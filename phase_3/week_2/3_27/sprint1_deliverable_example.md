# Sprint 1 Deliverable

## GitHub Repository

Create a GitHub repository, invite your team-members, and post a link to this repository below

https://github.com/F-said/casa

## DataSet Research

* [ChatGPT Test Suite](https://paperswithcode.com/dataset/chatgpt-software-testing)
* [GPT Sentiment](https://www.kaggle.com/datasets/konradb/chatgpt-the-tweets)

## DataSet Documentation

For each dataset that you find and are able to download locally, document the following: 

**ChatGPT Test Suite** 
* Quality: Some columns missing comments, mostly filled data
* Columns & their definitions: question-type, question-content, questions, answers, & their validity
* Dimensions: 32 samples & 32 columns
* Limitations: small-batch of questions
* Time-Period: Early 2023
* Source: https://github.com/sajedjalil/ChatGPT-Software-Testing-Study/tree/main/dataset

**GPT Sentiment** 
* Quality: Mostly filled data
* Columns & their definitions
* Dimensions: 295k samples, 12 features
* Limitations: General use sentiment of GPT outside of education
* Time-Period: 5Dec22 - Present
* Source: https://www.kaggle.com/datasets/konradb/chatgpt-the-tweets

As none of this data will be relevant for my project, I will not be saving this to ANY remote database.

## Minimal Viable Model

I will be generating two MVP's:

A meta-analysis of ChatGPT and its application in education

* Where is the data coming from? (A csv file is perfectly fine)
    * Datasets posted above downloaded locally
* What are some quick data transformations you can implement.
    * Drop missing values
    * Drop irrelevant columns (location)
* Which machine learning model will you use?
    * cluster analysis to figure out sentiment of ChatGPT in tweeting domain

And a seperate web-app model that will give hints on various programming problems (TKH affiliated)

