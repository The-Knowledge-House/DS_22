# Lab Title: SQL SELECT and Aggregation

## Objective
The goal of this lab is to provide participants with hands-on experience in using the SELECT statement, filtering data with the WHERE clause, grouping data with the GROUP BY clause, and applying conditions with the HAVING clause.

## Lab Outline

### 1. Connecting to the Database (5 minutes)
Participants should connect to the database where the tables `users` and `posts` are stored.

### 2. SELECT Statement
- Introduce the basic structure of the SELECT statement.
- Perform simple SELECT queries to retrieve data from the `users` and `posts` tables.

   ```sql
   -- Retrieve all columns from the users table
   SELECT * FROM users;

   -- Retrieve specific columns from the posts table
   SELECT post_id, user_id, caption, created_at 
   FROM posts;

   -- Retrieve posts with renamed columns
    SELECT post_id AS "Post ID", 
    user_id AS "User ID", 
    caption AS "Post Caption"
    FROM posts;
    ```

### 3. WHERE Clause and Filtering

```sql
-- Retrieve posts with a specific user_id
SELECT * FROM posts WHERE user_id = 1;

-- Retrieve users who joined after a certain date and have more than 500 followers
SELECT * FROM users WHERE joined_at > '2023-01-01' AND followers > 500;

-- Retrieve posts with likes greater than 1000
SELECT * FROM posts WHERE likes > 1000;

-- Retrieve posts with likes greater than 1000 OR posted by user_id 2
SELECT * 
FROM posts 
WHERE likes > 1000 OR user_id = 2;
```

### 4. GROUP BY Clause

```sql
-- Count the number of posts by each user
SELECT user_id, COUNT(*) AS post_count FROM posts GROUP BY user_id;

```

### 5. Aggregation Functions
```sql
-- Find the average number of likes per post
SELECT user_id, AVG(likes) AS avg_likes 
FROM posts 
GROUP BY user_id;

```

```sql
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
-- Find users with an average number of likes greater than 50
SELECT user_id, AVG(likes) AS avg_likes 
FROM posts 
GROUP BY user_id 
HAVING avg_likes > 50;

```

```sql
-- Find users who posted at least once and have an average likes greater than 50
SELECT user_id, COUNT(*) AS post_count, AVG(likes) AS avg_likes
FROM posts
GROUP BY user_id
HAVING post_count > 0 AND avg_likes > 50;

```
# EXERCISES
For the following exercises, use the images as a guide to know when you have the right answer. Since we are all using the same database the answers should be pretty similar! But if it's slightly off, it might be due to random selection by SQL unless we specifically have an order. 

Do your best to figure out which table fits the best for the question. If you need help, please ask!

1. Retrieve the usernames and email addresses of users who joined before '2015-01-01' but after `2013-01-01`, try to figure out how to filter out `NULL` values

![Alt text](images\q1.png)

2. Find the total number of posts made by each user. Display the user's ID and the count of posts. BONUS: Try to order by `DESC` order.

![Alt text](images\q2.png)

3. Find the month with the highest number of new user sign-ups. Display the month and the count of new users. Show only the highest month.
Hint: You may need to use the EXTRACT() function. See the following for help: https://www.w3resource.com/PostgreSQL/extract-function.php 

The examples show specific TIMESTAMPS but assume you can replace those with your column.

![Alt text](images\q3.png)

4. Find the average number of likes by user. Show only the top 5. Hint: `id` in the likes table refers to each individual like

![Alt text](images\q4.png)

5. Find the users who have more than 8 posts. No hints on this one! Might be a bit of a challenge.

![Alt text](images\q5.png)