# Importing pandas for data manipulation
import pandas as pd

# Defining a function to generate insights from the dataframe
def generate_insights(df):
    insights = []

    if 'Revenue' in df.columns:
        # Calculating total revenue
        total_revenue = df['Revenue'].sum()
        # Calculating average revenue
        avg_revenue = df['Revenue'].mean()
        # Finding maximum revenue
        max_revenue = df['Revenue'].max()
        # Finding minimum revenue
        min_revenue = df['Revenue'].min()
        # Appending revenue insights to the list
        insights.append(f"Total Revenue: ₹{total_revenue:,.2f}")
        insights.append(f"Average Revenue: ₹{avg_revenue:,.2f}")
        insights.append(f"Max Revenue: ₹{max_revenue:,.2f}")
        insights.append(f"Min Revenue: ₹{min_revenue:,.2f}")

        if 'Date' in df.columns:
            # Sorting the dataframe by date
            df_sorted = df.sort_values('Date')
            # Calculating revenue growth from start to end
            revenue_growth = df_sorted['Revenue'].iloc[-1] - df_sorted['Revenue'].iloc[0]
            # Appending revenue growth insight to the list
            insights.append(f"Revenue Growth (Start to End): ₹{revenue_growth:,.2f}")

    if 'Expense' in df.columns:
        # Calculating total expenses
        total_expense = df['Expense'].sum()
        # Calculating average expenses
        avg_expense = df['Expense'].mean()
        # Finding maximum expense
        max_expense = df['Expense'].max()
        # Finding minimum expense
        min_expense = df['Expense'].min()
        # Appending expense insights to the list
        insights.append(f"Total Expenses: ₹{total_expense:,.2f}")
        insights.append(f"Average Expense: ₹{avg_expense:,.2f}")
        insights.append(f"Max Expense: ₹{max_expense:,.2f}")
        insights.append(f"Min Expense: ₹{min_expense:,.2f}")

        if 'Category' in df.columns:
            # Finding the top expense category
            top_expense_category = df.groupby('Category')['Expense'].sum().idxmax()
            # Appending top expense category insight to the list
            insights.append(f"Top Expense Category: {top_expense_category}")

    if 'Profit' in df.columns:
        # Calculating total profit
        total_profit = df['Profit'].sum()
        # Calculating average profit
        avg_profit = df['Profit'].mean()
        # Calculating profit margin
        profit_margin = (total_profit / total_revenue) * 100 if 'Revenue' in df.columns and total_revenue != 0 else 0
        # Appending profit insights to the list
        insights.append(f"Total Profit: ₹{total_profit:,.2f}")
        insights.append(f"Average Profit: ₹{avg_profit:,.2f}")
        insights.append(f"Profit Margin: {profit_margin:.2f}%")

    if 'Date' in df.columns:
        # Extracting month from the date
        df['Month'] = df['Date'].dt.to_period('M')
        # Calculating monthly revenue
        monthly_revenue = df.groupby('Month')['Revenue'].sum()
        # Finding the month with the highest revenue
        highest_month = monthly_revenue.idxmax()
        # Appending highest revenue month insight to the list
        insights.append(f"Month with Highest Revenue: {highest_month}")

    return insights
