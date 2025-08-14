# Importing Flask for web application framework
from flask import Flask, render_template, request, redirect, url_for, send_file  # Flask imports

# Importing os for operating system interactions
import os  # OS module

# Importing pandas for data manipulation
import pandas as pd  # Data handling

# Importing plotly.express for data visualization
import plotly.express as px  # Plotly express

# Importing plotly.graph_objects for advanced data visualization
import plotly.graph_objects as go  # Plotly graph objects

# Importing uuid for generating unique identifiers
import uuid  # Unique ID generation

# Importing pdfkit for generating PDF files
import pdfkit  # PDF generation

# Importing custom insights generation function
from insights import generate_insights  # Custom insights

# Initializing the Flask application
app = Flask(__name__)  # Flask app instance

# Setting the upload folder configuration
app.config['UPLOAD_FOLDER'] = 'uploads'  # Upload folder path

# Creating the upload folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):  # Check folder
    os.makedirs(app.config['UPLOAD_FOLDER'])  # Create folder

# Defining a function to preprocess the data
def preprocess_data(filepath):  # Preprocess function
    df = pd.read_csv(filepath)  # Read CSV
    print("\n--- EDA Report ---")  # EDA start
    print(f"Shape of data: {df.shape}")  # Shape
    print(f"Size of data: {df.size}")  # Size
    print(f"Missing values:\n{df.isnull().sum()}")  # Missing values
    print("--- End of EDA Report ---\n")  # EDA end
    df.dropna(inplace=True)  # Drop NA
    if 'Date' in df.columns:  # Check Date
        df['Date'] = pd.to_datetime(df['Date'])  # Convert to datetime
        df.sort_values('Date', inplace=True)  # Sort by date
    return df  # Return dataframe

# Defining a function to generate charts from the data
def generate_charts(df):  # Chart generation
    charts = {}  # Chart dictionary
    if 'Date' in df.columns:  # Check Date
        if 'Revenue' in df.columns:  # Revenue line chart
            fig = px.line(df, x='Date', y='Revenue', title='Revenue Over Time')  # Line chart
            charts['revenue_line'] = fig.to_html(full_html=False)  # Save chart
            fig = px.area(df, x='Date', y='Revenue', title='Cumulative Revenue Growth')  # Area chart
            charts['revenue_area'] = fig.to_html(full_html=False)  # Save chart
        if 'Profit' in df.columns:  # Profit line chart
            fig = px.line(df, x='Date', y='Profit', title='Profit Over Time', line_shape='spline')  # Profit chart
            charts['profit_line'] = fig.to_html(full_html=False)  # Save chart
        if 'Revenue' in df.columns and 'Expense' in df.columns:  # Revenue vs Expense
            fig = go.Figure()  # Create figure
            fig.add_trace(go.Scatter(x=df['Date'], y=df['Revenue'], mode='lines', name='Revenue'))  # Revenue trace
            fig.add_trace(go.Scatter(x=df['Date'], y=df['Expense'], mode='lines', name='Expense'))  # Expense trace
            fig.update_layout(title='Revenue vs Expense Over Time')  # Layout
            charts['rev_vs_exp'] = fig.to_html(full_html=False)  # Save chart
    if 'Category' in df.columns and 'Expense' in df.columns:  # Category pie/bar
        pie_df = df.groupby('Category')['Expense'].sum().reset_index()  # Group by category
        fig = px.pie(pie_df, names='Category', values='Expense', title='Expenses by Category')  # Pie chart
        charts['expenses_pie'] = fig.to_html(full_html=False)  # Save chart
        fig = px.bar(pie_df, x='Category', y='Expense', title='Top Expense Categories')  # Bar chart
        charts['expenses_bar'] = fig.to_html(full_html=False)  # Save chart
    if df.select_dtypes(include='number').shape[1] > 1:  # Correlation heatmap
        corr = df.select_dtypes(include='number').corr()  # Correlation matrix
        fig = px.imshow(corr, text_auto=True, title='Correlation Heatmap')  # Heatmap
        charts['heatmap'] = fig.to_html(full_html=False)  # Save chart
    if 'Date' in df.columns and 'Revenue' in df.columns:  # Monthly revenue
        df['Month'] = df['Date'].dt.to_period('M').astype(str)  # Extract month
        monthly_rev = df.groupby('Month')['Revenue'].sum().reset_index()  # Group by month
        fig = px.bar(monthly_rev, x='Month', y='Revenue', title='Monthly Revenue Trend')  # Bar chart
        charts['monthly_revenue'] = fig.to_html(full_html=False)  # Save chart
    return charts  # Return charts

# Defining the route for the index page
@app.route('/')  # Home route
def index():  # Index function
    return render_template('index.html')  # Render index

# Defining the route for file upload
@app.route('/upload', methods=['POST'])  # Upload route
def upload():  # Upload function
    if 'file' not in request.files:  # Check file
        return redirect(url_for('index'))  # Redirect
    file = request.files['file']  # Get file
    if file.filename == '':  # Empty filename
        return redirect(url_for('index'))  # Redirect
    file_id = str(uuid.uuid4())  # Generate ID
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], f"{file_id}.csv")  # File path
    file.save(filepath)  # Save file
    return redirect(url_for('dashboard', file_id=file_id))  # Redirect to dashboard

# Defining the route for the dashboard
@app.route('/dashboard/<file_id>')  # Dashboard route
def dashboard(file_id):  # Dashboard function
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], f"{file_id}.csv")  # File path
    df = preprocess_data(filepath)  # Preprocess
    charts = generate_charts(df)  # Generate charts
    insights = generate_insights(df)  # Generate insights
    return render_template('dashboard.html', charts=charts, insights=insights, file_id=file_id)  # Render dashboard

# Defining the route for downloading the PDF report
@app.route('/download/<file_id>')  # Download route
def download(file_id):  # Download function
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], f"{file_id}.csv")  # File path
    df = preprocess_data(filepath)  # Preprocess
    charts = generate_charts(df)  # Generate charts
    insights = generate_insights(df)  # Generate insights
    rendered = render_template('pdf_report.html', charts=charts, insights=insights)  # Render PDF
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{file_id}.pdf")  # PDF path
    pdfkit.from_string(rendered, pdf_path)  # Generate PDF
    return send_file(pdf_path, as_attachment=True)  # Send file

# Running the Flask application
if __name__ == '__main__':  # Main check
    app.run(debug=False)  # Run app
