### Report on Development of Python Codes for Integration of Relational and NoSQL Databases

---

### Introduction

This report describes the development of Python codes for integrating relational and NoSQL databases, meeting the initial requirements of the proposed challenge. The main goal was to implement an application using SQLite with SQLAlchemy for the relational database and MongoDB with PyMongo for the NoSQL database. However, during development, it was not possible to establish the connection with MongoDB Atlas. This report will cover the methods used, the results obtained, and the issue faced during the attempt to connect to MongoDB Atlas.

### Methods

The development of the codes was divided into two main parts:

1. **Implementation of Relational Database with SQLAlchemy:**
   - Two classes, Cliente and Conta, representing the tables of the relational database, were defined.
   - Using SQLAlchemy, a schema was created for the SQLite database.
   - A minimal set of data was inserted for information manipulation.
   - Data retrieval methods were executed using SQLAlchemy.

2. **Implementation of NoSQL Database with PyMongo:**
   - Attempts were made to connect to MongoDB Atlas and create a database.
   - However, despite various efforts, it was not possible to establish the connection successfully.
   - The connection failure will be investigated and resolved in future iterations of the project.

### Results

The results obtained were as follows:

- **Relational Database with SQLAlchemy:**
  - The schema was correctly defined, and the Cliente and Conta classes were successfully implemented.
  - Data was inserted properly, and data retrieval methods were successfully executed.

- **NoSQL Database with PyMongo:**
  - It was not possible to establish a connection with MongoDB Atlas, and consequently, it was not possible to proceed with the implementation of the NoSQL database.
  - The connection failure will be addressed in future iterations of the project.

### Conclusion

While there was success in implementing the relational database with SQLAlchemy, the failure to connect to MongoDB Atlas represents a significant obstacle in integrating the NoSQL database. However, this issue will be investigated and resolved in future iterations of the project. Despite the challenges encountered, the progress made so far demonstrates the viability and effectiveness of the solutions developed.

### Case Study: Internet Banking System

Despite the failure to connect to MongoDB Atlas, the internet banking system remains a relevant use case for the integration of relational and NoSQL databases. With the relational database, it is possible to store information about customers and their accounts, while the NoSQL database can be used to record financial transactions. By integrating both databases, customers can access a wide range of financial information efficiently and securely.

---

This report provides an overview of the development of Python codes for integrating relational and NoSQL databases, highlighting the methods used, the results obtained, and the challenges faced during the process. The failure to connect to MongoDB Atlas represents a significant area for improvement, which will be addressed in future iterations of the project.



# Installation and Usage Guide

This is a step-by-step guide to set up and run the Proketo project, which consists of an application integrating SQLite using SQLAlchemy and a NoSQL database with MongoDB using PyMongo.

## Requirements

- Python 3.x installed
- Git installed

## Step 1: Clone the Repository

```
git clone https://github.com/Daniel-Gehlen/py-nosql-sqlalchemy-pymongo.git
cd py-nosql-sqlalchemy-pymongo
```

## Step 2: Set Up the Virtual Environment (optional but recommended)

```
python3 -m venv venv
source venv/bin/activate

```

## Step 3: Install Dependencies

```
pip install -r requirements.txt

```