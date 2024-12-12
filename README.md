# Team 14: Personal Finance Management App

## 1. Environments

- Cloud platform: Amazon Web Services (AWS)
  - Storage: Amazon S3
  - Computing: Amazon EC2 (Amazon Linux 2023), AWS Lambda
  - Database: Amazon RDS for MySQL
- Machine learning: scikit-learn
- Data processing & analysis: NumPy, pandas
- Data visualization: Matplotlib

## 2. Dependencies

```text
# <package>=<version>
boto3=1.35.68
matplotlib=3.9.2
mysql-connector-python=9.1.0
numpy=2.0.2
pandas=2.2.3
scikit-learn=1.5.2
```

## 3. Usage

The below actions can only be executed in the same VPC as the RDS instance locates. They are tested in an EC2 instance of Amazon Linux 2023.

```text
personal-finance-management/
├── data/
├── doc/
├── src/
│   ├── models/
│   ├── temp/
│   ├── cleanup.sh
│   ├── load.py
│   ├── predict.py
│   ├── query.py
│   └── visualize.py
├── .gitignore
├── README.md
└── run
```

### 3.1 Run each action on a user separately

```bash
cd src/
```

The `src` folder contains some executables:

- (Q) To query user data from database: `python3 query.py -u <user_id>`
- (P) To predict user's next month spending in each category: `python3 predict.py -u <user_id>`
- (V) To visualize user's spending data: `python3 visualize.py`
- (C) To clean up queried results: `./cleanup.sh`

### 3.2 Run all actions on a user through a single script

The root folder contains the amazing script Q-Pick, which run each executable in sequence.
> Q-Pick (QPVC) performs the series of actions Query-Predict-Visualize-Cleanup in order. 

```bash
./run -u <user_id>
```

## 4. Data Schema

### 4.1 `User` Table

| Column Name | Data Type | Description                                     |
|-------------|-----------|-------------------------------------------------|
| `user_id`   | INT       | Primary Key, unique identifier for each user    |
| `name`      | VARCHAR   | Name of the user                                |
| `age`       | INT       | Age of the user                                 |
| `gender`    | CHAR(1)   | Gender of the user (`M` for Male, `F` for Female, `X` for Other) |

### 4.2 `ExpenseCategory` Table

| Column Name     | Data Type | Description                                   |
|-----------------|-----------|-----------------------------------------------|
| `category_id`   | INT       | Primary Key, unique identifier for each category |
| `category_name` | VARCHAR   | Name of the expense category (e.g., Housing, Food) |

### 4.3 `Expense` Table

| Column Name      | Data Type | Description                                                    |
|------------------|-----------|----------------------------------------------------------------|
| `expense_id`     | INT       | Primary Key, unique identifier for each expense record         |
| `user_id`        | INT       | Foreign Key linking to `User` table, identifies the user       |
| `category_id`    | INT       | Foreign Key linking to `ExpenseCategory` table, specifies the expense category |
| `month`          | ENUM      | Month of the expense (`Jan`, `Feb`, ..., `Dec`)                |
| `year`           | INT       | Year of the expense                                           |
| `amount`         | DECIMAL   | The monetary amount of the expense                             |

### 4.4 Benefits of the schema design

1. **Flexibility**: Adding or removing categories only requires changes in `ExpenseCategory`.
2. **Scalability**: Supports multiple quarters if adding a `quarter` column in `Expense`.
3. **Efficiency**: Using IDs as primary and foreign keys simplifies joins and speeds up queries.
4. **Analysis-Ready**: Easy to query monthly, annual, or category-based spending trends for each person.
   1. The data types of `year` and `month` are designed to be aggregated easily.

## 5. How to initialize tables and data in Amazon RDS for MySQL

> Amazon Relational Database Service (Amazon RDS) is a managed database service that helps you run relational database management systems (RDBMS) in the cloud, such as PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, and Db2. However, RDS is not a DBMS itself.

### 5.1 (Option 1) Construct database schema using MySQL DDL/DML statements

1. Run `./data/init_schema.sql` on RDS to create the tables.
2. Run `./data/init_data.sql` on RDS to infuse some data rows into the tables.

### 5.2 (Option 2) Load S3 data into Amazon RDS MySQL tables

> <https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-template-copys3tords.html>
