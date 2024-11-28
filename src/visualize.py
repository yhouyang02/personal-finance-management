import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

data = pd.read_csv("./temp/results.csv")

category_mapping = {
    1: "Housing",
    2: "Utilities",
    3: "Dining",
    4: "Entertainment",
    5: "Transportation",
    6: "Health",
    7: "Insurance",
    8: "Education",
    9: "Miscellaneous"
}

today = datetime.today()
curr_month = today.strftime('%b') 
last_month = today.replace(day=1) - timedelta(days=1)
curr_year = int(last_month.year)
last_month = last_month.strftime('%b')

def bar_chart(data):
    save_path = "./temp/figure_barchart.jpg"

    # Filter data
    line_data = data[(data['month'] == last_month) & (data['year'] == curr_year)]
    category_totals = line_data.groupby('category_id')['amount'].sum().reset_index()
    category_totals['category_name'] = category_totals['category_id'].map(category_mapping)

    # Plot the bar chart
    plt.bar(category_totals['category_name'], category_totals['amount'], color='skyblue')
    plt.xlabel('Category Name')
    plt.ylabel('Total Cost')
    plt.title(f'Total Cost by Category for {last_month} {curr_year}')
    plt.xticks(category_totals['category_name'])
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(save_path, format="jpg")
    plt.close()


def line_chart(data):
    save_path = "./temp/figure_linechart.jpg"
    bar_data = data[(data['year'] == curr_year)]
    month_totals = bar_data.groupby('month')['amount'].sum().reset_index()
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_totals['month'] = pd.Categorical(month_totals['month'], categories=month_order, ordered=True)
    month_totals = month_totals.set_index('month').reindex(month_order, fill_value=0).reset_index()
    month_totals = month_totals[month_totals['month'] <= curr_month]

    plt.figure(figsize=(10, 6))
    plt.plot(month_totals['month'], month_totals['amount'], marker='o', linestyle='-', color='b')
    plt.title(f"Yearly Spendings for {curr_year}", fontsize=16)
    plt.xlabel("Month", fontsize=12)
    plt.xticks(rotation=45)
    plt.ylabel("Spending", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.savefig(save_path, format="jpg")
    plt.close()

if __name__=="__main__":
    bar_chart(data)
    line_chart(data)
    print("Data saved to ./temp/figure_barchart.jpg")
    print("Data saved to ./temp/figure_linechart.jpg")
    print("Visualization completed successfully")
