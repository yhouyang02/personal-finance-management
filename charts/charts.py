import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("../data/init_data.csv")

"""
Query for Bar Chart Data
SELECT 
    u.user_id, 
    u.name, 
    u.age, 
    u.gender, 
    ec.category_name, 
    SUM(e.amount) AS total_amount, 
    e.month, 
    e.year
FROM 
    User u
JOIN 
    Expense e ON u.user_id = e.user_id
JOIN 
    ExpenseCategory ec ON e.category_id = ec.category_id
WHERE 
    u.user_id = 1 
    AND e.month = DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH), '%b')
    AND e.year = YEAR(CURDATE())
GROUP BY 
    u.user_id, 
    u.name, 
    u.age, 
    u.gender, 
    ec.category_name, 
    e.month, 
    e.year;
+---------+-------+------+--------+----------------+--------------+-------+------+
| user_id | name  | age  | gender | category_name  | total_amount | month | year |
+---------+-------+------+--------+----------------+--------------+-------+------+
|       1 | Alice |   25 | F      | Housing        |      2089.70 | Oct   | 2024 |
|       1 | Alice |   25 | F      | Dining         |       366.24 | Oct   | 2024 |
|       1 | Alice |   25 | F      | Transportation |       433.55 | Oct   | 2024 |
|       1 | Alice |   25 | F      | Utilities      |      2616.95 | Oct   | 2024 |
|       1 | Alice |   25 | F      | Health         |      1426.47 | Oct   | 2024 |
|       1 | Alice |   25 | F      | Entertainment  |      1156.07 | Oct   | 2024 |
+---------+-------+------+--------+----------------+--------------+-------+------+
"""
def bar_chart(data):
    # TODO 1: Connect script to SQL DB
    # TODO 2: Query for current USER ID and Prev Month Spendings
    #         a) Check for what is Prev Month
    #         b) Query for data corresponding
    #         c) Expect to return table with columns: category names | total cost | month | year
    # TODO 3: Return Bar Chart summarizing categorical spendings
    #         x-axis: categories, y-axis: spendings
    category names | total cost | month | year
    curr_month = 'Oct'
    curr_year = 2024
    data = data[(data['month'] == curr_month) & (data['year'] == curr_year)]
    category_totals = data.groupby('category_id')['amount'].sum().reset_index()

    # Plot the bar chart
    plt.bar(category_totals['category_id'], category_totals['amount'], color='skyblue')
    plt.xlabel('Category ID')
    plt.ylabel('Total Cost')
    plt.title(f'Total Cost by Category for {curr_month} {curr_year}')
    plt.xticks(category_totals['category_id'])  # Set x-axis ticks to match category IDs
    plt.tight_layout()
    plt.show()

    print(data)

"""
Query for Line Chart Data
SELECT 
    e.month, 
    SUM(e.amount) AS total_spendings
FROM 
    Expense e
WHERE 
    e.user_id = @user_id
    AND e.year = YEAR(CURDATE())
GROUP BY 
    e.month
ORDER BY 
    STR_TO_DATE(e.month, '%b');

+-------+-----------------+
| month | total_spendings |
+-------+-----------------+
| Jan   |         4368.27 |
| Feb   |         7907.13 |
| Mar   |         3475.05 |
| Apr   |         5396.50 |
| May   |         9956.74 |
| Jun   |         3220.29 |
| Jul   |         5174.31 |
| Aug   |         6366.75 |
| Sep   |         5494.84 |
| Oct   |         8088.98 |
| Nov   |         3046.99 |
| Dec   |         3803.97 |
+-------+-----------------+
"""

def line_chart():
    # TODO 1: Connect script to SQL DB
    # TODO 2: Query for current USER ID and Prev Month Spendings
    # TODO 3: Return Line Chart for all historical spendings of current year
    #         x-axis: January - Current Month, y-axis: total spendings of month
    print("hi")

if __name__=="__main__":
    bar_chart(data)
