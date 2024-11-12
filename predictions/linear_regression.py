import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# Load the data
data = pd.read_csv("ExpenseData.csv")

# Assuming the CSV data has columns ['expense_id', 'user_id', 'category_id', 'month', 'year', 'amount']

# Step 1: Aggregate data to get monthly expense totals per user
# Convert 'month' to a numeric format to simplify sorting and calculations
month_mapping = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
data['month_num'] = data['month'].map(month_mapping)

# Sort data by user, year, and month
data = data.sort_values(by=['user_id', 'year', 'month_num'])

# Step 2: Aggregate the monthly expense per user by summing up all categories
monthly_expense = data.groupby(['user_id', 'year', 'month_num'])['amount'].sum().reset_index()

# Step 3: Select data for a single user for model training and testing
user_id = 1  # Replace with the desired user ID
user_data = monthly_expense[monthly_expense['user_id'] == user_id]

# Create the feature (X) and target (y) variables
# X is previous months' expenses, and y is the following month's expense
X = user_data[['year', 'month_num']]
y = user_data['amount']

# Step 4: Train/Test Split (using past data to predict the next month)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Step 5: Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Predict the next month's expense
y_pred = model.predict(X_test)

# Calculate Mean Squared Error for accuracy assessment
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Predict the next month after the last entry for this user
last_year = user_data['year'].iloc[-1]
last_month = user_data['month_num'].iloc[-1]
next_month = 1 if last_month == 12 else last_month + 1
next_year = last_year + 1 if next_month == 1 else last_year

# Create a DataFrame with column names matching those in the training data
next_input = pd.DataFrame([[next_year, next_month]], columns=['year', 'month_num'])

# Display the expense for the same month in previous years
previous_years_data = user_data[(user_data['month_num'] == next_month)].reset_index(drop=True)
print("Expenses for the same month in previous years:")
print(previous_years_data[['year', 'amount']])

# Predict the next month's expense using the existing code
next_expense = model.predict(next_input)
print(f"\nPredicted Expense for user {user_id} in the next month: {next_expense[0]:.2f}")

