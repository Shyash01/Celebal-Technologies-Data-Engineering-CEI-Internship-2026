# Secure Retail Data Lakehouse

> A Python-based Data Engineering project that implements a secure layered ETL pipeline (Raw → Bronze → Silver → Gold) with data privacy techniques, cryptographic tokenization, PostgreSQL integration, automated validation, and reporting.

---

# Project Overview

Secure Retail Data Lakehouse is my final project for the **Celebal Technologies Data Engineering Internship 2026**.

The objective of this project is to simulate how a retail organization can securely process customer and transaction data before making it available for analytics.

The pipeline generates realistic synthetic retail data, validates it, applies multiple privacy-preserving transformations, organizes it using a Medallion Architecture (Raw, Bronze, Silver, and Gold), loads the final analytical datasets into PostgreSQL, and generates execution and data quality reports.

The project focuses on implementing practical Data Engineering concepts while keeping the design modular, readable, and suitable for an internship-level implementation.

---

# Problem Statement

Retail organizations collect large amounts of customer information every day, including names, email addresses, phone numbers, payment details, and transaction history.

Using this data directly for analytics creates privacy and security concerns because Personally Identifiable Information (PII) should not be exposed to analysts or downstream systems.

The goal of this project is to build a secure ETL pipeline that protects sensitive customer information while still producing datasets that are useful for business reporting and analysis.

---

# Project Objectives

The project was developed with the following objectives:

- Build a layered ETL pipeline following the Medallion Architecture
- Generate realistic synthetic retail datasets
- Validate generated datasets before processing
- Protect sensitive customer information using multiple privacy techniques
- Implement cryptographic tokenization for selected identifiers
- Create analytics-ready datasets
- Load processed data into PostgreSQL
- Generate automated reports for validation and pipeline execution
- Demonstrate good Data Engineering practices through a modular project structure

---

# Key Features

- Synthetic Retail Data Generation
- Automated Data Validation
- Raw, Bronze, Silver, and Gold Data Layers
- Hard Drop of highly sensitive information
- Data Masking
- Data Redaction
- SHA-256 Tokenization
- Feature Engineering
- Customer and Sales Aggregation
- PostgreSQL Integration
- Automated HTML and Text Reports
- Modular Python Codebase
- Environment Variable Based Configuration

---

# Project Architecture

```text
                 Product Master Generation
                            │
                            ▼
                 Customer Data Generation
                            │
                            ▼
               Transaction Data Generation
                            │
                            ▼
                   Data Validation
                            │
                            ▼
                      Raw Layer
                            │
                            ▼
                    Bronze Layer
          (Hard Drop + Metadata Addition)
                            │
                            ▼
                    Silver Layer
     (Masking + Redaction + Tokenization)
                            │
                            ▼
                     Gold Layer
(Feature Engineering + Generalization + Aggregation)
                            │
                            ▼
                  PostgreSQL Database
                            │
                            ▼
                 Automated Report Generation
```

---

# Technology Stack

| Category | Technologies |
|-----------|--------------|
| Programming Language | Python 3 |
| Data Processing | Pandas |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Synthetic Data | Faker |
| Security | hashlib (SHA-256), python-dotenv |
| Reporting | HTML Reports, Text Reports |
| Version Control | Git, GitHub |
| Development Environment | Visual Studio Code |

---

# Project Structure

```text
Secure-Retail-Data-Lakehouse/
│
├── data/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── master_data/
│
├── reports/
│
├── scripts/
│   ├── generators/
│   ├── bronze_layer.py
│   ├── silver_layer.py
│   ├── gold_layer.py
│   ├── database_loader.py
│   └── generate_reports.py
│
├── README.md
├── requirements.txt
├── run_pipeline.py
├── Software_Requirements_Specification.pdf
├── Final_Project_Report.pdf
└── .gitignore
```

---

# Pipeline Workflow

The complete pipeline follows a sequential ETL process.

```text
Generate Product Master
        │
        ▼
Generate Customers
        │
        ▼
Generate Transactions
        │
        ▼
Validate Generated Data
        │
        ▼
Raw Layer
        │
        ▼
Bronze Layer
        │
        ▼
Silver Layer
        │
        ▼
Gold Layer
        │
        ▼
Load into PostgreSQL
        │
        ▼
Generate Reports
```

The entire workflow can be executed automatically using:

```bash
python run_pipeline.py
```

---

# ETL Pipeline

## Raw Layer

The Raw Layer stores the generated datasets exactly as they are created.

### Files

- customers.csv
- transactions.csv

### Purpose

- Preserve the original generated data
- Act as the source of truth
- Serve as the input for downstream processing

---

## Bronze Layer

The Bronze Layer performs the first stage of data processing.

### Transformations

- Removes CVV using the Hard Drop technique
- Adds ingestion timestamp
- Adds pipeline run identifier
- Preserves the remaining business data without modification

### Output

- customers_bronze.csv
- transactions_bronze.csv

---

## Silver Layer

The Silver Layer focuses on protecting Personally Identifiable Information (PII).

### Transformations

- Customer Name Masking
- Email Address Masking
- Phone Number Masking
- Address Redaction
- Card Number Masking

### Tokenization

Along with masking, the Silver Layer creates secure surrogate tokens for selected customer identifiers using **salted SHA-256 hashing**.

Generated columns include:

- email_token
- phone_token

These tokens are deterministic, meaning the same input always generates the same output. This allows secure joins and analytics while making it computationally infeasible to recover the original values without the secret salt stored in the `.env` file.

### Output

- customers_silver.csv
- transactions_silver.csv

---

## Gold Layer

The Gold Layer prepares datasets for reporting and business analysis.

### Transformations

- Customer Age Calculation
- Age Group Generation
- Transaction Amount Bucketing
- Customer Summary
- Sales Summary

### Privacy Improvements

After calculating customer age and age groups, the exact `date_of_birth` column is removed from the final dataset.

Customer postal codes are also generalized by keeping only the first three digits (for example, `560103` becomes `560XXX`).

These transformations reduce the possibility of re-identifying an individual while preserving the usefulness of the data for analytics.

### Output

- customers_gold.csv
- transactions_gold.csv
- customer_summary.csv
- sales_summary.csv

---

# Data Privacy Strategy

The project applies multiple privacy-preserving techniques at different stages of the pipeline.

| Technique | Purpose | Status |
|-----------|---------|--------|
| Hard Drop | Remove highly sensitive information (CVV) | Implemented |
| Data Masking | Hide customer identity | Implemented |
| Data Redaction | Remove complete address information | Implemented |
| SHA-256 Tokenization | Create irreversible surrogate identifiers | Implemented |
| Generalization | Remove exact DOB and generalize postal codes | Implemented |
| Aggregation | Generate business insights without exposing individual records | Implemented |

These transformations ensure that the datasets used for analytics do not expose sensitive customer information while still supporting meaningful business analysis.

---

# PostgreSQL Integration

The final Gold Layer datasets are automatically loaded into PostgreSQL using SQLAlchemy.

### Database

```
secure_retail_lakehouse
```

### Tables

| Table | Description |
|--------|-------------|
| customers_gold | Processed customer dataset |
| transactions_gold | Processed transaction dataset |
| customer_summary | Customer summary by loyalty tier |
| sales_summary | Sales summary by product category |

This demonstrates how processed analytical datasets can be stored inside a relational database for reporting and querying.

---

# Automated Reports

The pipeline automatically generates reports after successful execution.

| Report | Purpose |
|---------|---------|
| validation_report.txt | Dataset validation results |
| data_quality_report.txt | Missing values, duplicates, and quality checks |
| pipeline_metrics_report.txt | Pipeline execution statistics |
| pipeline_summary.html | HTML summary of the complete pipeline |

These reports help verify pipeline execution and provide a quick overview of data quality.

---

# Installation

## Clone the Repository

```bash
git clone <repository-url>
cd Secure-Retail-Data-Lakehouse
```

---

## Create a Virtual Environment

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

# Configure Environment Variables

Create a `.env` file in the project root.

```text
DB_HOST=localhost
DB_PORT=5433
DB_NAME=secure_retail_lakehouse
DB_USER=postgres
DB_PASSWORD=your_password_here
HASH_SALT=your_random_secret_salt_here
```

The project uses environment variables to manage database credentials and the cryptographic hashing salt. The `.env` file is excluded from version control through `.gitignore` and should never be committed to GitHub.

# Running the Project

The complete pipeline can be executed either step-by-step or through a single automation script.

## Option 1: Run the Complete Pipeline

```bash
python run_pipeline.py
```

This executes the following stages in sequence:

1. Generate Product Master
2. Generate Customers
3. Generate Transactions
4. Validate Generated Data
5. Execute Bronze Layer
6. Execute Silver Layer
7. Execute Gold Layer
8. Load Data into PostgreSQL
9. Generate Reports

---

## Option 2: Run Each Stage Individually

### Generate Product Master

```bash
python scripts/generators/generate_product_master.py
```

### Generate Customers

```bash
python scripts/generators/generate_customers.py
```

### Generate Transactions

```bash
python scripts/generators/generate_transactions.py
```

### Validate Generated Data

```bash
python scripts/generators/validate_generated_data.py
```

### Execute Bronze Layer

```bash
python scripts/bronze_layer.py
```

### Execute Silver Layer

```bash
python scripts/silver_layer.py
```

### Execute Gold Layer

```bash
python scripts/gold_layer.py
```

### Load Data into PostgreSQL

```bash
python scripts/database_loader.py
```

### Generate Reports

```bash
python scripts/generate_reports.py
```

---

# Pipeline Outputs

After successful execution, the following outputs are generated.

## Raw Layer

```
customers.csv

transactions.csv
```

---

## Bronze Layer

```
customers_bronze.csv

transactions_bronze.csv
```

---

## Silver Layer

```
customers_silver.csv

transactions_silver.csv
```

---

## Gold Layer

```
customers_gold.csv

transactions_gold.csv

customer_summary.csv

sales_summary.csv
```

---

# PostgreSQL Outputs

The following tables are automatically created inside the PostgreSQL database.

```
customers_gold

transactions_gold

customer_summary

sales_summary
```

These tables can be queried directly for reporting and analytics.

---

# Generated Reports

The project generates several reports automatically after pipeline execution.

| Report | Description |
|---------|-------------|
| validation_report.txt | Summary of dataset validation |
| data_quality_report.txt | Missing values, duplicates, and quality assessment |
| pipeline_metrics_report.txt | Pipeline execution statistics |
| pipeline_summary.html | HTML summary of the complete pipeline |

These reports help verify successful execution and provide quick insight into the generated datasets.

---

# Security Notes

This project follows a privacy-first approach while remaining suitable for an internship-level implementation.

Some important security practices followed are:

- Database credentials are managed using environment variables (`.env`) instead of being hardcoded.
- The cryptographic hashing salt used for tokenization is also stored in `.env`.
- Personally Identifiable Information (PII) is protected using masking, redaction, tokenization, hard drop, and generalization techniques.
- Sensitive files such as `.env` are excluded from version control through `.gitignore`.
- Project dependencies are managed using `requirements.txt`, while the virtual environment (`venv`) is excluded from GitHub.

---

# Learning Outcomes

Working on this project helped me gain practical experience in:

- Designing layered ETL pipelines
- Implementing the Medallion Architecture
- Generating realistic synthetic datasets
- Data validation and quality assessment
- Applying privacy-preserving techniques
- Hard Drop, Masking, Redaction, and Generalization
- Cryptographic tokenization using SHA-256
- Feature engineering for analytics
- Building reusable and modular Python scripts
- Loading analytical datasets into PostgreSQL
- Using SQLAlchemy for database operations
- Managing application configuration using environment variables
- Automating report generation
- Organizing a Data Engineering project using a clean folder structure

---

# Future Scope

This project can be extended further by implementing features such as:

- Incremental data loading
- Additional business KPIs and dashboards
- More advanced data quality validation rules
- Support for multiple input data sources
- Data versioning for historical analysis
- Interactive visualization using Power BI or Tableau

These enhancements can further improve the project while building upon the current architecture.

---

# Author

**Yash Sharma**

B.Tech Computer Science & Engineering (Data Science)

Amity University Uttar Pradesh

Celebal Technologies Data Engineering Internship (2026)

---

# Acknowledgements

I would like to thank:

- Celebal Technologies for providing the internship opportunity and project statement.
- My internship mentors for their guidance throughout the program.
- The open-source community behind Python, Pandas, SQLAlchemy, Faker, and PostgreSQL for providing the tools used in this project.

---

# License

This project has been developed for educational and internship purposes.

Feel free to explore, learn from, and adapt the implementation for academic use.

---

If you found this project useful or interesting, consider giving the repository a ⭐.