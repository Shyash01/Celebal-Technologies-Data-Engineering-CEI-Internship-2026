# E-Commerce Order Analytics System

> **Week 8 Mini Project**  
> **Celebal Technologies Summer Internship 2026**

---

## Project Overview

This project is an end-to-end E-Commerce Order Analytics System developed using Python, PostgreSQL and SQL.

The objective of the project is to simulate how raw business data is generated, cleaned, validated, stored in a database and finally analyzed using SQL. The project also includes a simple Python-based reporting tool that retrieves business insights directly from the PostgreSQL database.

Instead of using an existing dataset, realistic synthetic datasets were generated using Python and Faker to better understand the complete data engineering workflow.

---

## Project Objective

The main objective of this project is to build a complete analytics pipeline for an e-commerce order management system.

The project includes:

- Generate realistic synthetic datasets
- Introduce common data quality issues
- Clean and validate the datasets
- Load cleaned data into PostgreSQL
- Perform SQL-based business analysis
- Generate reports using Python
- Handle common edge cases

---

## Technologies Used

- Python
- Pandas
- Faker
- PostgreSQL
- SQL
- SQLAlchemy
- psycopg2
- Jupyter Notebook
- VS Code
- Git & GitHub

---

## Project Structure

```text
Week8_ECommerce_Order_Analytics_System
│
├── Data
│   ├── raw
│   ├── cleaned
│   └── reports
│
├── database
│   ├── create_tables.sql
│   ├── load_data.py
│   └── schema.sql
│
├── documentation
│
├── notebook
│   ├── Ecommerce_Analytics.ipynb
│   └── Ecommerce_Analytics_Final.ipynb
│
├── screenshots
│
├── scripts
│   ├── analytics.py
│   ├── data_generation.py
│   ├── data_cleaning.py
│   ├── data_validation.py
│   ├── reporting.py
│   └── utils.py
│
├── sql
│   ├── basic_queries.sql
│   ├── intermediate_queries.sql
│   └── advanced_queries.sql
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Project Workflow

The project follows the workflow shown below.

```text
Synthetic Data Generation
            ↓
Dirty Data Creation
            ↓
Data Cleaning
            ↓
Data Validation
            ↓
PostgreSQL Database
            ↓
SQL Analysis
            ↓
Python Reporting
```

---

# Dataset Information

Four synthetic datasets were generated for this project.

| Dataset | Records |
|----------|---------|
| Customers | 1000 |
| Products | 250 |
| Orders | 5000 |
| Order Items | 15000 |

---

## Dataset Columns

### Customers

- customer_id
- customer_name
- email
- registration_date
- customer_type

### Products

- product_id
- product_name
- category
- subcategory
- cost_price

### Orders

- order_id
- customer_id
- order_date
- status
- region_code

### Order Items

- item_id
- order_id
- product_id
- quantity
- unit_price
- discount_percent

---

# Data Quality Issues Introduced

To simulate real-world business data, intentional data quality issues were introduced.

### Customers

- Invalid email addresses
- Duplicate records

### Products

- Extra spaces
- Inconsistent capitalization

### Orders

- Missing customer IDs
- Incorrect date formats

### Order Items

- Negative quantities representing returned products

---

# Data Cleaning

The datasets were cleaned before loading them into PostgreSQL.

Cleaning performed:

- Removed duplicate customer records
- Replaced invalid emails with missing values
- Standardized product names
- Removed extra spaces
- Fixed missing customer IDs
- Corrected inconsistent date formats
- Preserved negative quantities because they represent returned products

---

# Data Validation

After cleaning, validation checks were performed to verify data quality.

Validation included:

- Missing IDs
- Duplicate IDs
- Missing emails
- Missing customer IDs
- Negative quantity count
- Unique key validation

Validation reports are available inside:

```text
Data/reports/
```

---

# PostgreSQL Integration

Instead of SQLite, PostgreSQL was used for this project.

The cleaned datasets were loaded into PostgreSQL using SQLAlchemy.

Database Tables:

- customers
- products
- orders
- order_items

Foreign key relationships were implemented between the tables.

---

# SQL Analysis

SQL analysis was divided into three separate files.

### Basic Queries

- Revenue by Category
- Top Customers
- Month-wise Orders

### Intermediate Queries

- Customers without Delivered Orders
- Products with More Returns than Purchases
- Return Rate by Category

### Advanced Queries

- Running Total
- DENSE_RANK()
- LAG()
- Multi-level CTE
- NTILE()
- Year-over-Year Comparison
- FIRST_VALUE()
- LAST_VALUE()
- Cumulative Distribution
- Cohort Analysis
- Self Join

---

# Python Reporting

A simple command-line reporting tool was developed using Python and PostgreSQL.

The reporting tool accepts:

- Report Type
- Start Date
- End Date

The generated report includes:

- Total Orders
- Total Revenue
- Unique Customers
- Top 3 Products
- Previous Period Comparison

Run the reporting tool using:

```bash
python scripts/reporting.py
```

---

# Edge Case Handling

The project also validates common edge cases.

Implemented validations:

- Invalid Order IDs
- Discount Percentage greater than 100
- Zero Quantity
- Future Order Dates

These checks help identify incorrect business data before analysis.

---

# Screenshots

Project screenshots are available in the **screenshots** folder.

The screenshots include:

- Dataset Generation
- Data Cleaning
- Data Validation
- PostgreSQL Tables
- SQL Query Outputs
- Reporting Tool Output

---

# Learning Outcomes

During this project, I learned how to:

- Generate synthetic business datasets
- Simulate real-world dirty data
- Clean and validate datasets
- Load data into PostgreSQL
- Write business-focused SQL queries
- Use Window Functions and CTEs
- Build a simple reporting tool using Python
- Organize a project using reusable Python scripts

---

# Future Improvements

Some possible improvements for this project are:

- Add Power BI dashboard for visualization
- Export reports in PDF format
- Schedule automated report generation
- Build a web interface using Flask
- Deploy the project on cloud services

---

# How to Run the Project

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create PostgreSQL database

```sql
CREATE DATABASE ecommerce_analytics_db;
```

### 4. Create tables

Execute:

```text
database/create_tables.sql
```

### 5. Generate datasets

```bash
python scripts/data_generation.py
```

### 6. Clean datasets

```bash
python scripts/data_cleaning.py
```

### 7. Validate datasets

```bash
python scripts/data_validation.py
```

### 8. Load data into PostgreSQL

```bash
python database/load_data.py
```

### 9. Execute SQL queries

Run the SQL files available inside:

```text
sql/
```

### 10. Generate report

```bash
python scripts/reporting.py
```

---

# Author

**Yash**  
B.Tech CSE (Data Science)  
Amity University Uttar Pradesh

**Project Completed as part of the Celebal Technologies Summer Internship 2026**

