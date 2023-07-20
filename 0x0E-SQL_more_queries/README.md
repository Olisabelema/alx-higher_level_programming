0x0E. SQL - More queries

"SQL - More queries" refers to a continuation or extension of SQL (Structured Query Language) queries beyond the basics. It suggests that there are additional or more advanced SQL queries to explore and learn about.

SQL is a powerful language used for managing relational databases. It allows users to interact with databases, retrieve data, modify data, create tables, and perform various operations on the data stored in a database.

"SQL - More queries" could encompass a wide range of topics, such as:

Advanced SELECT queries: Including the use of aggregate functions (SUM, COUNT, AVG, etc.), grouping data with GROUP BY, filtering data with HAVING, and using subqueries.

Joins: Understanding and using different types of joins like INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN to combine data from multiple tables.

Data modification queries: Learning how to INSERT, UPDATE, and DELETE data in the database.

Indexing and optimization: Using indexes to improve query performance and optimizing SQL queries for faster execution.

Transactions: Understanding the concept of transactions and how to manage them in SQL.

Views and Stored Procedures: Creating and using views and stored procedures to simplify complex queries and promote code reusability.

Working with dates and time: Handling date and time data in SQL queries.

Subqueries and Common Table Expressions (CTEs): Writing more complex queries using subqueries and CTEs.

Overall, "SQL - More queries" implies that there is a deeper level of SQL expertise to explore beyond the basic SQL commands, and it encourages users to learn and apply more advanced SQL concepts to handle complex data operations and database management tasks.

Learning Objectives

General How to create a new MySQL user How to manage privileges for a user to a database or table What’s a PRIMARY KEY What’s a FOREIGN KEY How to use NOT NULL and UNIQUE constraints How to retrieve datas from multiple tables in one request What are subqueries What are JOIN and UNION

Requirements General Allowed editors: vi, vim, emacs All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25) All your files should end with a new line All your SQL queries should have a comment just before (i.e. syntax above) All your files should start by a comment describing the task All SQL keywords should be in uppercase (SELECT, WHERE…) A README.md file, at the root of the folder of the project, is mandatory The length of your files will be tested using wc More Info Comments for your SQL file: $ cat my_script.sql -- 3 first students in the Batch ID=3 -- because Batch 3 is the best! SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3; $ Install MySQL 8.0 on Ubuntu 20.04 LTS $ sudo apt update $ sudo apt install mysql-server ... $ mysql --version mysql Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu)) $ Connect to your MySQL server:

$ sudo mysql Welcome to the MySQL monitor. Commands end with ; or \g. Your MySQL connection id is 11 Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its affiliates. Other names may be trademarks of their respective owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> mysql> quit Bye $ Use “container-on-demand” to run MySQL In the container, credentials are root/root

Ask for container Ubuntu 20.04 Connect via SSH OR connect via the Web terminal In the container, you should start MySQL before playing with it: $ service mysql start

Starting MySQL database server mysqld $ $ cat 0-list_databases.sql | mysql -uroot -p
Database
information_schema
mysql
performance_schema
sys
$ In the container, credentials are root/root
