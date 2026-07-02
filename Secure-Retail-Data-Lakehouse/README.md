# 🔐 Secure Retail Data Lakehouse

> **A Python-based Secure Retail Data Engineering Pipeline implementing layered ETL architecture (Raw → Bronze → Silver → Gold) with PII protection, PostgreSQL integration, automated validation, and reporting.**

---

##  Project Overview

Secure Retail Data Lakehouse is a Data Engineering project developed as part of the **Celebal Technologies Data Engineering Internship**.

The project demonstrates how raw retail transaction data containing Personally Identifiable Information (PII) can be securely processed through a layered ETL pipeline before being made available for analytical workloads.

The implementation follows the concepts described in the internship problem statement by applying:

- Hard Drop of highly sensitive information
- Data Masking
- Data Privacy
- Data Transformation
- Data Aggregation
- Layered Data Lakehouse Architecture
- Automated Reporting
- PostgreSQL Integration

---

##  Problem Statement

Retail organizations continuously collect sensitive customer information such as:

- Customer Names
- Email Addresses
- Phone Numbers
- Home Addresses
- Payment Card Information

Directly exposing this information to downstream analytical systems creates serious security and compliance risks.

This project implements a secure batch ETL pipeline that sanitizes customer data before it reaches analytical storage.

---

## Project Objectives

The primary objectives of this project are:

- Build a layered ETL Data Lakehouse
- Generate realistic synthetic retail datasets
- Validate generated datasets
- Protect Personally Identifiable Information (PII)
- Implement Hard Drop strategy
- Apply masking techniques
- Create analytics-ready Gold datasets
- Store processed datasets inside PostgreSQL
- Generate automated project reports
- Demonstrate Data Engineering best practices

---

##  Key Features

- Synthetic Retail Data Generation
- Automated Data Validation
- Bronze Layer (Hard Drop)
- Silver Layer (PII Masking)
- Gold Layer (Feature Engineering & Aggregation)
- PostgreSQL Integration
- Automated Pipeline Reports
- Modular Python Architecture
- Config Driven Design
- Internship-Oriented Project Structure

---

##  Project Architecture

```text
                    Raw Layer
          customers.csv | transactions.csv
                     │
                     ▼
              Data Validation
                     │
                     ▼
              Bronze Layer
          (Hard Drop Sensitive Data)
                     │
                     ▼
              Silver Layer
           (PII Masking & Privacy)
                     │
                     ▼
               Gold Layer
      (Binning & Aggregation)
                     │
                     ▼
              PostgreSQL Database
                     │
                     ▼
           Automated Project Reports
```

---

##  Technology Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python 3 |
| Data Processing | Pandas |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Fake Data Generation | Faker |
| Reporting | HTML + Text Reports |
| Version Control | Git & GitHub |
| IDE | Visual Studio Code |

---

## 📂 Project Structure

```text
Secure-Retail-Data-Lakehouse/
│
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   └── transactions.csv
│   │
│   ├── bronze/
│   │   ├── customers_bronze.csv
│   │   └── transactions_bronze.csv
│   │
│   ├── silver/
│   │   ├── customers_silver.csv
│   │   └── transactions_silver.csv
│   │
│   └── gold/
│       ├── customers_gold.csv
│       ├── transactions_gold.csv
│       ├── customer_summary.csv
│       └── sales_summary.csv
│
├── master_data/
│   └── product_master.csv
│
├── reports/
│   ├── validation_report.txt
│   ├── data_quality_report.txt
│   ├── pipeline_metrics_report.txt
│   └── pipeline_summary.html
│
├── scripts/
│   ├── generators/
│   │   ├── config.py
│   │   ├── data_loader.py
│   │   ├── generate_customers.py
│   │   ├── generate_product_master.py
│   │   ├── generate_transactions.py
│   │   ├── transaction_allocator.py
│   │   └── validate_generated_data.py
│   │
│   ├── bronze_layer.py
│   ├── silver_layer.py
│   ├── gold_layer.py
│   ├── database_loader.py
│   └── generate_reports.py
│
├── README.md
├── requirements.txt
├── run_pipeline.py
└── .gitignore
```

---

#  Data Pipeline Workflow

The project follows a layered ETL (Extract → Transform → Load) architecture inspired by modern Data Lakehouse principles.

```text
Synthetic Data Generation
            │
            ▼
     Data Validation
            │
            ▼
         Raw Layer
            │
            ▼
      Bronze Layer
     (Hard Drop)
            │
            ▼
      Silver Layer
   (Mask & Protect PII)
            │
            ▼
       Gold Layer
(Binning & Aggregation)
            │
            ▼
     PostgreSQL Storage
            │
            ▼
   Automated Report Generation
```

---

#  Data Sources

The project generates realistic synthetic retail datasets using the **Faker** library and custom business logic.

### Generated Datasets

| Dataset | Description |
|----------|-------------|
| customers.csv | Customer master data containing PII and demographic information |
| transactions.csv | Retail transaction records |
| product_master.csv | Product catalog containing categories and pricing |

---

# 🔄 ETL Pipeline Overview

The pipeline processes retail data through four logical stages.

## 1️⃣ Raw Layer

The Raw Layer stores generated retail datasets exactly as they are produced.

### Files

- customers.csv
- transactions.csv

### Purpose

- Preserve original data
- Act as the source of truth
- Maintain complete customer information before transformations

---

## 2️⃣ Bronze Layer

The Bronze Layer performs the first security transformation.

### Transformation Performed

- Hard Drop of highly sensitive payment information (CVV)
- Addition of ingestion metadata
- Preservation of original business data

### Output

- customers_bronze.csv
- transactions_bronze.csv

---

## 3️⃣ Silver Layer

The Silver Layer focuses on protecting Personally Identifiable Information (PII).

### Transformations Performed

- Customer Name Masking
- Email Address Masking
- Phone Number Masking
- Address Redaction
- Payment Card Number Masking

### Output

- customers_silver.csv
- transactions_silver.csv

---

## 4️⃣ Gold Layer

The Gold Layer prepares analytics-ready datasets.

### Transformations Performed

- Customer Age Calculation
- Age Group Generation
- Transaction Amount Bucketing
- Customer Aggregation
- Sales Aggregation

### Output

- customers_gold.csv
- transactions_gold.csv
- customer_summary.csv
- sales_summary.csv

---

#  Data Privacy Strategy

The project implements multiple data privacy techniques.

| Technique | Purpose | Implemented |
|-----------|----------|-------------|
| Hard Drop | Remove highly sensitive information | ✅ |
| Data Masking | Hide customer identity | ✅ |
| Data Redaction | Remove sensitive addresses | ✅ |
| Aggregation | Analytics without exposing individuals | ✅ |

These transformations ensure that downstream analytical users never access sensitive customer information directly.

# 🗄 PostgreSQL Integration

The final analytics-ready datasets generated by the Gold Layer are automatically loaded into PostgreSQL using **SQLAlchemy**.

## Database

```text
secure_retail_lakehouse
```

## Tables

| Table | Description |
|--------|-------------|
| customers_gold | Analytics-ready customer dataset |
| transactions_gold | Analytics-ready transaction dataset |
| customer_summary | Customer aggregation by loyalty tier |
| sales_summary | Sales aggregation by product category |

This integration demonstrates how processed data can be loaded into a relational database for querying and business analytics.

---

#  Automated Reports

The project automatically generates reports after successful pipeline execution.

| Report | Description |
|---------|-------------|
| validation_report.txt | Validation results for generated datasets |
| data_quality_report.txt | Missing values, duplicates, and data quality checks |
| pipeline_metrics_report.txt | Pipeline execution metrics and record counts |
| pipeline_summary.html | HTML summary of the complete pipeline |

These reports provide visibility into pipeline execution and help verify data quality before downstream consumption.

---

#  Installation

## Clone the Repository

```bash
git clone <repository-url>
cd Secure-Retail-Data-Lakehouse
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure PostgreSQL

Update the database credentials inside:

```text
scripts/generators/config.py
```

```python
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "secure_retail_lakehouse"
DB_USER = "postgres"
DB_PASSWORD = "your_password"
```

---

#  Running the Project

Run each stage of the pipeline in the following order:

### 1. Generate Product Master

```bash
python scripts/generators/generate_product_master.py
```

### 2. Generate Customers

```bash
python scripts/generators/generate_customers.py
```

### 3. Generate Transactions

```bash
python scripts/generators/generate_transactions.py
```

### 4. Validate Generated Data

```bash
python scripts/generators/validate_generated_data.py
```

### 5. Execute Bronze Layer

```bash
python scripts/bronze_layer.py
```

### 6. Execute Silver Layer

```bash
python scripts/silver_layer.py
```

### 7. Execute Gold Layer

```bash
python scripts/gold_layer.py
```

### 8. Load Data into PostgreSQL

```bash
python scripts/database_loader.py
```

### 9. Generate Reports

```bash
python scripts/generate_reports.py
```

---

# 📈 Pipeline Outputs

## Data Layer Outputs

```text
Raw Layer
│
├── customers.csv
└── transactions.csv

Bronze Layer
│
├── customers_bronze.csv
└── transactions_bronze.csv

Silver Layer
│
├── customers_silver.csv
└── transactions_silver.csv

Gold Layer
│
├── customers_gold.csv
├── transactions_gold.csv
├── customer_summary.csv
└── sales_summary.csv
```

---

## Database Outputs

```text
customers_gold

transactions_gold

customer_summary

sales_summary
```

---

## Report Outputs

```text
validation_report.txt

data_quality_report.txt

pipeline_metrics_report.txt

pipeline_summary.html
```

---

#  Learning Outcomes

This project demonstrates practical implementation of:

- Layered ETL Pipeline Design
- Data Lakehouse Architecture
- Data Privacy Techniques
- Personally Identifiable Information (PII) Protection
- Data Validation
- Data Quality Assessment
- Feature Engineering
- Data Aggregation
- PostgreSQL Integration
- SQLAlchemy
- Automated Reporting
- Modular Python Project Structure
- Configuration Driven Development

---

#  Future Enhancements

Potential improvements include:

- Apache Spark implementation
- Azure Data Lake integration
- Azure Data Factory orchestration
- Apache Airflow scheduling
- Incremental data loading
- Docker containerization
- CI/CD pipeline integration
- Cloud deployment
- Monitoring and alerting
- Interactive analytics dashboard

---

#  Author

**Yash Sharma**

B.Tech Computer Science & Engineering (Data Science)

Amity University Uttar Pradesh

Celebal Technologies Data Engineering Internship Project

---

# Acknowledgements

- Celebal Technologies
- Internship Mentors
- PostgreSQL
- SQLAlchemy
- Pandas
- Faker
- Python Community

---

#  License

This project has been developed for educational and internship purposes.

---

##  If you found this project useful, consider giving it a star.