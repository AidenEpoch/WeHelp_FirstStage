<h2> WeHelp assignment week5 </h2>

<h3>task2</h3>

```sql
CREATE DATABASE website;
```

```sql
CREATE TABLE member(
id INT PRIMARY KEY AUTO INCREMENT CHECK(id >= 0),
name VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL,
password VARCHAR(255), NOT NULL,
follower_count INT NOT NULL DEFAULT 0 CHAECK(follower_count >= 0),
time DATE NOT NULL DEFAULT GETDATE()
);
```
