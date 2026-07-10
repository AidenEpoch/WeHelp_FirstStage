# WeHelp assignment week5 

## task2

**Create a new database named website**

```sql
CREATE DATABASE website;
```

![image](https://github.com/AidenEpoch/WeHelp_FirstStage/blob/main/week5/image/task2_1.png)

**Create a new table named member, in the website database**

```sql
CREATE TABLE member(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL,
password VARCHAR(255) NOT NULL,
follower_count INT NOT NULL DEFAULT 0 CHECK(follower_count >= 0),
time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

![image](https://github.com/AidenEpoch/WeHelp_FirstStage/blob/main/week5/image/task2_2.png)

***

## task3

**INSERT a new row to the member table where name, email and password must be
set to test, test@test.com, and test. INSERT additional 4 rows with arbitrary data**

```sql
INSERT INTO member(name, email, password)VALUES('test', 'test@test.com', 'test');
INSERT INTO member(name, email, password)VALUES('member1', 'member1@google.com', 'first');
INSERT INTO member(name, email, password)VALUES('member2', 'member2@google.com', 'second');
INSERT INTO member(name, email, password)VALUES('member3', 'member3@google.com', 'third');
INSERT INTO member(name, email, password)VALUES('member4', 'member4@google.com', 'forth');
```

![image](https://github.com/AidenEpoch/WeHelp_FirstStage/blob/main/week5/image/task3_1.png)

**SELECT all rows from the member table**

```sql
SELECT *FROM member;
```

![image](https://github.com/AidenEpoch/WeHelp_FirstStage/blob/main/week5/image/task3_2.png)

**SELECT all rows from the member table, in descending order of time**

```sql
SELECT *FROM member ORDER BY time DESC;
```

![image](https://github.com/AidenEpoch/WeHelp_FirstStage/blob/main/week5/image/task3_3.png)

**SELECT total 3 rows, second to fourth, from the member table, in descending order
of time. Note: it does not mean SELECT rows where id are 2, 3, or 4**

```sql
SELECT *FROM member ORDER BY time DESC LIMIT 1, 3;
```

![image](https://github.com/AidenEpoch/WeHelp_FirstStage/blob/main/week5/image/task3_4.png)

**SELECT rows where email equals to test@test.com**

```sql
SELECT *FROM member WHERE email = 'test@test.com';
```

![image](https://github.com/AidenEpoch/WeHelp_FirstStage/blob/main/week5/image/task3_5.png)

**SELECT rows where name includes the es keyword**

```sql
SELECT *FROM member WHERE name LIKE '%es%';
```

![image](https://github.com/AidenEpoch/WeHelp_FirstStage/blob/main/week5/image/task3_6.png)


**SELECT rows where email equals to test@test.com and password equals to test**

```sql
SELECT *FROM member WHERE email = 'test@test.com' AND password = 'test';
```

![image](https://github.com/AidenEpoch/WeHelp_FirstStage/blob/main/week5/image/task3_7.png)

**UPDATE data in name column to test2 where email equals to test@test.com**

```sql
UPDATE member SET name = 'test2' WHERE email = 'test@test.com';
```

![image](https://github.com/AidenEpoch/WeHelp_FirstStage/blob/main/week5/image/task3_8.png)

***

## task4
為了配合**task4**的操作，故將id 2 ~ id 5的follower_count之值修改如下:
![image](https://github.com/AidenEpoch/WeHelp_FirstStage/blob/main/week5/image/task4_1.png)

**SELECT how many rows from the member table**

```sql
SELECT COUNT(*) FROM member;
```

![image](https://github.com/AidenEpoch/WeHelp_FirstStage/blob/main/week5/image/task4_2.png)

**SELECT the sum of follower_count of all the rows from the member table**

```sql
SELECT SUM(follower_count) FROM member;
```

![image](https://github.com/AidenEpoch/WeHelp_FirstStage/blob/main/week5/image/task4_3.png)

**SELECT the average of follower_count of all the rows from the member table**

```sql
SELECT AVG(follower_count) FROM member;
```

![image](https://github.com/AidenEpoch/WeHelp_FirstStage/blob/main/week5/image/task4_4.png)

**SELECT the average of follower_count of the first 2 rows, in descending order of
follower_count, from the member table**

```sql
SELECT AVG(t.follower_count) FROM (SELECT follower_count FROM member ORDER BY follower_count DESC LIMIT 2) AS t;
```

![image](https://github.com/AidenEpoch/WeHelp_FirstStage/blob/main/week5/image/task4_5.png)

***

## task5

**Create a new table named message, in the website database. designed as below**

```sql
CREATE TABLE message(
id INT PRIMARY KEY AUTO_INCREMENT,
member_id INT NOT NULL,
content TEXT(65535) NOT NULL,
like_count INT CHECK(like_count >= 0) NOT NULL DEFAULT 0,
time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(member_id) REFERENCES member(id)
);
```

為了完成**task5**的操作，故創建message表格如下:
![image](https://github.com/AidenEpoch/WeHelp_FirstStage/blob/main/week5/image/task5_2.png)

![image](https://github.com/AidenEpoch/WeHelp_FirstStage/blob/main/week5/image/task5_1.png)

**SELECT all messages, including sender names. We have to JOIN the member table
to get that**

```sql
SELECT member.name, message.* FROM member INNER JOIN message ON member.id = message.member_id; 
```

![image](https://github.com/AidenEpoch/WeHelp_FirstStage/blob/main/week5/image/task5_3.png)

**SELECT all messages, including sender names, where sender email equals to
test@test.com. We have to JOIN the member table to filter and get that**

```sql
SELECT member.name, message.* FROM member INNER JOIN message ON member.id = message.member_id WHERE member.email = 'test@test.com';
```

![image](https://github.com/AidenEpoch/WeHelp_FirstStage/blob/main/week5/image/task5_4.png)

**Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like
count of messages where sender email equals to test@test.com**

```sql
SELECT AVG(message.like_count) FROM message INNER JOIN member ON message.member_id = member.id WHERE member.email = 'test@test.com';
```

![image](https://github.com/AidenEpoch/WeHelp_FirstStage/blob/main/week5/image/task5_5.png)

**Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like
count of messages GROUP BY sender email**

```sql
SELECT member.email, AVG(message.like_count) FROM message INNER JOIN member ON message.member_id = member.id GROUP BY member.email;
```

![image](https://github.com/AidenEpoch/WeHelp_FirstStage/blob/main/week5/image/task5_6.png)
