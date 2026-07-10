## WeHelp assignment week5 

### task2

**Create a new database named website**

```sql
CREATE DATABASE website;
```

**Create a new table named member, in the website database**

```sql
CREATE TABLE member(
id INT PRIMARY KEY AUTO INCREMENT CHECK(id >= 0),
name VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL,
password VARCHAR(255), NOT NULL,
follower_count INT NOT NULL DEFAULT 0 CHECK(follower_count >= 0),
time DATE NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

### task3

```sql
INSERT INTO member(name, email, password)VALUES(test, test@test.com, test);
```

