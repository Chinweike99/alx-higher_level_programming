**What is a database?**
- It's a software tool that helps you store, manage, and access data efficiently. A database brings order to the chaos, keeping everything neatly organized and readily available when you need it.

**Relational database.**
- A relational database is a specific type of database that organizes data in a structured way using tables, records, and relationships.
**Examples of relational databases:**
- MySQL
- PostgreSQL
- Oracle
- Microsoft SQL Server

**SQL** - Structured Query Language

**MySQL:**
- MySQL is a popular open-source relational database management system (RDBMS). It allows you to store, manage, and access structured data efficiently.
- **Common uses of MySQL:**
- Web applications: Powering dynamic websites and online platforms.
- E-commerce: Managing customer information, orders, and products.
- Content management systems: Storing and retrieving website content.
- Financial systems: Tracking transactions, accounts, and financial data.
- Data analysis: Accessing and manipulating data for insights and reports.

**How to create a database in MySQL**
 - 1.Access the MySQL server: 
  If using a terminal, enter the following command: Sudo mysql 
 - 2.Create the database:
Once connected, use the CREATE DATABASE statement.
eg: CREATE DATABASE your_database_name

**What does DDL and DML stand for**
1.DDL means Data Definition Language
DDL commands focus on defining the structure of a database. This includes:
Creating tables: Defining the columns, data types, and constraints for each table.
Creating indexes: Enabling faster data retrieval by creating special look-up tables.
Defining relationships: Establishing connections between different tables.
Modifying existing database structure: Adding or removing columns, changing data types, etc
2.DML: Data Manipulation Language
DML commands deal with the actual data within the tables. This includes:
Inserting new data: Adding new rows (records) to existing tables.
Updating existing data: Modifying existing values within table rows.
Deleting data: Removing unwanted rows from tables.
Retrieving data: Selecting and fetching specific data from tables based on various criteria.


How to CREATE or ALTER a table
Creating a Table:
Use the CREATE TABLE statement with the following structure:
CREATE TABLE your_table_name.
Altering a Table:
Use the ALTER TABLE statement with various options depending on your goal:
example: ALTER TABLE [table_name] ADD [column_name] [data_type] [constraints];


How to SELECT data from a table
Basic structure for selecting data from a table:
SELECT [column_names] FROM [table_name] [WHERE conditions] [ORDER BY columns] [LIMIT rows];


How to INSERT, UPDATE or DELETE data
Insert: INSERT INTO [table_name] ([column_names]) VALUES ([column_values]);
Update: UPDATE [table_name] SET [column_name] = [new_value] WHERE [condition];
Delete: DELETE FROM [table_name] WHERE [condition];


Subqueries 
Subqueries are like mini-queries nested within a larger query. They operate independently but provide data that's used in the main query's results.


How to use MySQL functions


MySQL functions are powerful tools that can enhance your queries and data manipulation tasks. They come in a variety of flavors, each serving a specific purpose. Here's a breakdown to get you started:
1. Understanding Function Categories:


String functions: Manipulate text data like UPPER(), LOWER(), SUBSTRING(), etc.
Numeric functions: Perform calculations on numbers like ABS(), SQRT(), ROUND(), etc.
Date and time functions: Work with dates and times like CURDATE(), ADDDATE(), DATEDIFF(), etc.
Aggregate functions: Summarize data like COUNT(), AVG(), SUM(), MAX(), etc.
Other functions: Perform specific tasks like CONCAT(), INSTR(), FIND_IN_SET(), etc.
2. Basic Function Syntax:
The general format for using a function is:

MySQL functions are powerful tools that can enhance your queries and data manipulation tasks. They come in a variety of flavors, each serving a specific purpose. Here's a breakdown to get you started:
1. Understanding Function Categories:
String functions: Manipulate text data like UPPER(), LOWER(), SUBSTRING(), etc.
Numeric functions: Perform calculations on numbers like ABS(), SQRT(), ROUND(), etc.
Date and time functions: Work with dates and times like CURDATE(), ADDDATE(), DATEDIFF(), etc.
Aggregate functions: Summarize data like COUNT(), AVG(), SUM(), MAX(), etc.
Other functions: Perform specific tasks like CONCAT(), INSTR(), FIND_IN_SET(), etc.
2. Basic Function Syntax:
The general format for using a function is:
SELECT [function_name]([argument1], [argument2], ...) FROM [table_name];

