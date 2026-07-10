## WeHelp assignment week5 

### task2

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

### task3

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
