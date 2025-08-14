# 📈 FinViz: Financial Data Visualization and AI Insights

**FinViz** is a web application built with Flask that transforms raw financial data from CSV files into interactive visualizations and provides automated insights using AI-powered analysis. Users can upload a CSV file and get a comprehensive dashboard with charts and key financial metrics.

---

## ✨ Features

- **Interactive Charts** – Dynamic charts for visualizing financial data, including:
  - Line charts for revenue and profit over time
  - Bar charts for monthly trends
  - Pie charts for expense categories
- **AI-Powered Insights** – Automatically generates key financial insights such as:
  - Total revenue
  - Average profit
  - Top expense categories
  - Month with highest revenue

- **Responsive Design** – Built with Bootstrap 5 for compatibility across devices.
- **Modern Aesthetics** – Dark theme, subtle animations via tsparticles, and a custom cursor.

---

## ⚙️ Technologies Used

- **Flask** – Backend framework
- **Pandas** – Data manipulation and preprocessing
- **Plotly** – Interactive charts and graphs
- **Bootstrap 5** – Responsive UI


---

## 🚀 How to Run Locally

### **Prerequisites**
- Python 3.x
- `pip` (Python package installer)

### **Installation**
1. **Clone the repository**
   ```bash
   git clone https://your-repository-url.git
   cd FinViz
Install dependencies

bash
Copy
Edit
pip install Flask pandas plotly 


Run the Flask application
bash
Copy
Edit
python app.py
Visit: http://127.0.0.1:5000

## 📈 Usage

1. Navigate to the home page of the app.
2. Upload a CSV file containing financial data (e.g., `Date`, `Revenue`, `Expense`, `Profit`, `Category`).
3. View generated **interactive charts** and **AI-powered insights**.



## 📂 Project Structure

```plaintext
FinViz/
├── app.py                  # Main Flask application file
├── insights.py             # AI-powered insights logic
├── templates/
│   ├── dashboard.html      # Dashboard page with charts & insights
│   ├── index.html          # Homepage with file upload form
│   └── layout.html         # Base HTML template
├── static/
│   ├── css/
│   │   └── style.css       # Custom styles
│   ├── img/
│   │   ├── 1.jpg           # Homepage background image
│   │   ├── 2.jpg           # Hero section background
│   │   └── logo.png        # App logo
│   └── js/
│       └── scripts.js      # Frontend JavaScript
└── uploads/                # Uploaded CSVs 


