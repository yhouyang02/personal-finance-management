from models.linear_regression import predict

EXPENSE_DATA_PATH = "./temp/results.csv"
CATEGORY_DATA_PATH = "./../data/csv/ExpenseCategory.csv"

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Fetch user data by user ID and save to CSV.")
parser.add_argument("-u", "--user_id", type=int, required=True, help="The user ID to fetch data for.")
args = parser.parse_args()

if __name__ == "__main__":
    predict(args.user_id, EXPENSE_DATA_PATH, CATEGORY_DATA_PATH)
    