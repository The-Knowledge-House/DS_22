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

1. Retrieve the usernames and email addresses of users who joined before '2023-01-01', try to figure out how to filter out `NULL` values

![Alt text](images\q1.png)
