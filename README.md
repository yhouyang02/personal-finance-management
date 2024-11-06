# Team 14: Personal Finance Management App

> Please record all environments, tools, libraries used any each of the project. They will be included in the final report!

## Environments

- Cloud platform: Amazon Web Services (AWS)
  - Storage: Amazon S3
  - Computing: Amazon EC2, AWS Lambda
  - Database: Amazon RDS for MySQL
- Machine learning: TensorFlow
- Data processing & analysis: pandas
- Data visualization:

## How-To's

> Please record detailed steps (including researched and used) of building each part of the project. They will be included in the final report!

### How to set up each AWS service unit

### How to establish connections between AWS services

### How to design an efficient relational database schema

#### `User` Table

| Column Name | Data Type | Description                                     |
|-------------|-----------|-------------------------------------------------|
| `user_id`   | INT       | Primary Key, unique identifier for each user    |
| `name`      | VARCHAR   | Name of the user                                |
| `age`       | INT       | Age of the user                                 |
| `gender`    | CHAR(1)   | Gender of the user (`M` for Male, `F` for Female, `X` for Other) |

#### `ExpenseCategory` Table

| Column Name     | Data Type | Description                                   |
|-----------------|-----------|-----------------------------------------------|
| `category_id`   | INT       | Primary Key, unique identifier for each category |
| `category_name` | VARCHAR   | Name of the expense category (e.g., Housing, Food) |

#### `Expense` Table

| Column Name      | Data Type | Description                                                    |
|------------------|-----------|----------------------------------------------------------------|
| `expense_id`     | INT       | Primary Key, unique identifier for each expense record         |
| `user_id`        | INT       | Foreign Key linking to `User` table, identifies the user       |
| `category_id`    | INT       | Foreign Key linking to `ExpenseCategory` table, specifies the expense category |
| `month`          | ENUM      | Month of the expense (`Jan`, `Feb`, ..., `Dec`)                |
| `year`           | INT       | Year of the expense                                           |
| `amount`         | DECIMAL   | The monetary amount of the expense                             |

#### Benefits of the schema design

1. **Flexibility**: Adding or removing categories only requires changes in `ExpenseCategory`.
2. **Scalability**: Supports multiple quarters if adding a `quarter` column in `MonthlyExpenditure`.
3. **Efficiency**: Using IDs as primary and foreign keys simplifies joins and speeds up queries.
4. **Analysis-Ready**: Easy to query monthly, annual, or category-based spending trends for each person.
   1. The data types of `year` and `month` are designed to be aggregated easily.

### How to initialize tables and data in Amazon RDS for MySQL

> Amazon Relational Database Service (Amazon RDS) is a managed database service that helps you run relational database management systems (RDBMS) in the cloud, such as PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, and Db2. However, RDS is not a DBMS itself.

#### Option 1: Construct database schema using MySQL DDL/DML statements

1. Run `./data/init_schema.sql` on RDS to create the tables.
2. Run `./data/init_data.sql` on RDS to infuse some data rows into the tables.

#### Option 2: Load S3 data into Amazon RDS MySQL tables

> <https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-template-copys3tords.html>

### How to configure security features of AWS services

### How to manage costs of AWS services

### How to ...
