# Lab Title: SQL SELECT and Aggregation

## Objective
The goal of this lab is to provide participants with hands-on experience in using the SELECT statement, filtering data with the WHERE clause, grouping data with the GROUP BY clause, and applying conditions with the HAVING clause.

## Lab Outline

### 1. Connecting to the Database (5 minutes)
Please make sure you are connected to the database in your PGAdmin4 and have properly loaded the Instagram SQL.

### 2. SELECT Statement
The SELECT statement is the core of SQL. Without the SELECT statement we would not be able to pull in any of the data we need.

```sql
-- Retrieve all columns from the users table
SELECT * FROM users;

-- Retrieve specific columns from the posts table
SELECT id, user_id, caption, created_at 
FROM posts;

-- Retrieve posts with renamed columns
    SELECT id AS "Post ID", 
    user_id AS "User ID", 
    caption AS "Post Caption"
    FROM posts;
```


### 3. WHERE Clause and Filtering
The WHERE Clause lets us filter our data. This is great for a couple reasons. 
1. It minimizes the amount of data that we are processing at once since SQL performs this filtering first, this makes our query faster.
2. We can focus on the data that is the most interesting to us without having to sift through as much data
3. It can show us where there might be issues in our data.


```sql
-- Retrieve posts with a specific user_id
SELECT * 
FROM posts 
WHERE user_id = 1;

-- Retrieve users who do not have an empty bio
SELECT username, bio
FROM users
WHERE bio IS NOT NULL;

-- Retrieve posts that were created after 2015 
SELECT id, created_at
FROM posts
WHERE created_at > '2015-01-01'

-- Retrieve posts with likes created after 2015  AND posted by user_id 123
SELECT user_id, id, created_at
FROM posts
WHERE created_at > '2015-01-01' AND user_id = 123;
```

### 4. GROUP BY Clause
Group by allows to bunch a bunch of rows together. For example, the same person can post multiple times and we want to know how many posts they've made. We would group by user ID's and then do a COUNT(*) function in order to get a count.

```sql
-- Count the number of posts by each user
SELECT user_id, COUNT(*) AS post_count 
FROM posts 
GROUP BY user_id;

```

### 5. Aggregation Functions

There are other aggregate functions in SQL other than just COUNT(). Let's try a few.
```sql
-- Find the average number of likes per post
-- This introduces the idea of a subquery, because of how we have our tables structured we can't just do "AVG(LIKES)"
-- We'll explain how this works and you'll see it tomorrow!
SELECT AVG(total_likes)
FROM (
SELECT post_id, COUNT(id) total_likes
FROM likes 
WHERE post_id IS NOT NULL
GROUP BY post_id
ORDER BY total_likes DESC
) like_counts;


-- Find the total number of posts made by each user
SELECT user_id, COUNT(*) AS post_count 
FROM posts 
GROUP BY user_id;

-- Find the earliest and latest post creation dates for each user
SELECT user_id, MIN(created_at) AS earliest_post, 
MAX(created_at) AS latest_post
FROM posts
GROUP BY user_id;

```

### 6. HAVING Clause

```sql
-- Find users who have given more than 50 likes
SELECT user_id, COUNT(likes) AS total_likes 
FROM likes 
GROUP BY user_id 
HAVING COUNT(likes) > 50;

```


# EXERCISES
For the following exercises, use the images as a guide to know when you have the right answer. Since we are all using the same database the answers should be pretty similar! But if it's slightly off, it might be due to random selection by SQL unless we specifically have an order. 

Do your best to figure out which table fits the best for the question. If you need help, please ask!

1. Retrieve the usernames and email addresses of users who joined before '2015-01-01' but after `2013-01-01`, try to figure out how to filter out `NULL` values

![Alt text](images\q1.png)

SELECT user_id, COUNT(*) AS post_count 
FROM posts 
GROUP BY user_id;

```sql
SELECT user_id, COUNT(*) AS post_count 
FROM posts 
GROUP BY user_id;

```

2. Find the total number of posts made by each user. Display the user's ID and the count of posts. BONUS: Try to order by `DESC` order.

![Alt text](images\q2.png)

3. Find the month with the highest number of new user sign-ups. Display the month and the count of new users. Show only the highest month.
Hint: You may need to use the EXTRACT() function. See the following for help: https://www.w3resource.com/PostgreSQL/extract-function.php 

The examples show specific TIMESTAMPS but assume you can replace those with your column.

![Alt text](images\q3.png)

4. Find the average length of a post caption. Then find the top 5 longest. Hint: you may need to find what the `LENGTH` function for PostGreSQL is

![Alt text](images\q4a.png)

![Alt text](images\q4b.png)


5. Find the users who have more than 8 posts. No hints on this one! Might be a bit of a challenge.

![Alt text](images\q5.png)