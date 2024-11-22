import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("../data/init_data.csv")

def bar_chart(data):
    # TODO 1: Connect script to SQL DB
    # TODO 2: Query for current USER ID and Prev Month Spendings
    #         a) Check for what is Prev Month
    #         b) Query for data corresponding
    #         c) Expect to return table with columns: category names | total cost | month | year
    # TODO 3: Return Bar Chart summarizing categorical spendings
    #         x-axis: categories, y-axis: spendings
    # category names | total cost | month | year
    # sql_query = 

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


def line_chart(data):
    # TODO 1: Connect script to SQL DB
    # TODO 2: Query for current USER ID and Prev Month Spendings
    # TODO 3: Return Line Chart for all historical spendings of current year
    #         x-axis: January - Current Month, y-axis: total spendings of month

    curr_year = 2024
    data = data[(data['year'] == curr_year)]
    month_totals = data.groupby('month')['amount'].sum().reset_index()
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_totals['month'] = pd.Categorical(month_totals['month'], categories=month_order, ordered=True)
    month_totals = month_totals.sort_values('month')

    plt.figure(figsize=(10, 6))
    plt.plot(month_totals['month'], month_totals['amount'], marker='o', linestyle='-', color='b')
    plt.title(f"Yearly Spendings for {curr_year}", fontsize=16)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Spending", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    print(data)

if __name__=="__main__":
    bar_chart(data)
    line_chart(data)
