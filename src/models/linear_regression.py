import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def predict(user_id, expense_data_path, category_data_path):
    # Load the data from CSV files
    expense_data = pd.read_csv(expense_data_path)
    category_data = pd.read_csv(category_data_path)

    # Mapping category names to their IDs
    category_mapping = dict(zip(category_data['category_id'], category_data['category_name']))

    # Step 1: Preprocessing (convert months to numeric and sort by user_id, year, and month)
    expense_data['month_num'] = expense_data['month'].map({
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
        'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
    })
    expense_data = expense_data.sort_values(by=['user_id', 'year', 'month_num'])

    # Filter data for a specific user
    user_data = expense_data[expense_data['user_id'] == user_id]

    # Aggregate monthly expenses by category
    monthly_expense = user_data.groupby(['year', 'month_num', 'category_id'])['amount'].sum().reset_index()

    # Step 2: Create features and targets
    X = monthly_expense[['year', 'month_num', 'category_id']]
    y = monthly_expense['amount']

    # Step 3: Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # Train Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict next month's expenses for all categories
    last_year = monthly_expense['year'].max()
    last_month = monthly_expense[monthly_expense['year'] == last_year]['month_num'].max()
    next_month = 1 if last_month == 12 else last_month + 1
    next_year = last_year + 1 if next_month == 1 else last_year

    # Create DataFrame for next month's prediction
    categories = user_data['category_id'].unique()
    next_month_data = pd.DataFrame({
        'year': [next_year] * len(categories),
        'month_num': [next_month] * len(categories),
        'category_id': categories
    })

    # Predict spending
    next_month_data['predicted_amount'] = model.predict(next_month_data)

    # Map category names and sort by category_id
    next_month_data['category_name'] = next_month_data['category_id'].map(category_mapping)
    next_month_data = next_month_data.sort_values(by='category_id')
    
    # Format output columns
    output = next_month_data[['category_id', 'category_name', 'predicted_amount']]

    # Display results
    print("Predicted spending (next month) for User %d:" % user_id)
    print(output)
    
    # Save to file if output_file_path is provided
    if output_file_path:
        try:
            with open(output_file_path, 'w') as f:
                f.write(output)
            print(f"\nPredictions saved to: {output_file_path}")
        except Exception as e:
            print(f"\nError saving to file: {str(e)}")
    
    return next_month_data