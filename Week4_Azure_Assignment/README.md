# Week 4 - Azure Data Factory Assignment

## Objective

Build a complete Azure Data Factory pipeline to read a CSV file from Azure Blob Storage, validate metadata, and copy the file to a new destination.

## Services Used

- Azure Data Factory
- Azure Blob Storage
- Azure IAM

## Tasks Performed

### Task 1
Created Azure Resource Group

### Task 2
Created Azure Storage Account

### Task 3
Created Blob Container and uploaded CSV file

### Task 4
Configured:
- Linked Service
- Source Dataset
- Sink Dataset

### Task 5
Built ADF Pipeline:
- Get Metadata Activity
- Copy Data Activity

### Task 6
Configured IAM Roles:
- Reader
- Contributor

### Mini Project

Implemented end-to-end pipeline:

Source:
- CSV file stored in Blob Storage

Process:
- Metadata Validation
- Data Copy

Destination:
- New output file in Blob Storage

## Results

- Metadata validation successful
- Pipeline executed successfully
- Data copied successfully
- Output file generated in Blob Storage

## Learning Outcomes

- Azure Storage Management
- Azure Data Factory Pipelines
- Metadata Validation
- IAM Role Management
- Data Movement using Copy Activity