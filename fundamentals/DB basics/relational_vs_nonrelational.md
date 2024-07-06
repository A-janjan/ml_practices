# Relational vs non-relational databases

## What is a relational database?

**Answer:** A relational database is a type of database that stores and provides access to data points that are related to one another. Data is organized into tables (or relations) with rows and columns. Each table has a primary key, and tables can be linked using foreign keys.

**Explanation:** Emphasize the tabular structure and the importance of relationships and constraints.

---
## Explain the concept of normalization.
Database normalization is a process used to organize a database into tables and columns in such a way as to reduce data redundancy and improve data integrity. The main goals of normalization are to eliminate redundant data (for example, storing the same data in more than one table) and ensure data dependencies make sense (only storing related data in a table). This helps to avoid issues such as update anomalies, insertion anomalies, and deletion anomalies.

Normalization typically involves dividing large tables into smaller, more manageable tables and defining relationships between them. The process follows a series of rules or "normal forms" which are applied one by one. Each subsequent normal form addresses a specific type of redundancy or dependency problem and builds on the previous one. The most commonly used normal forms are:

### 1. First Normal Form (1NF)

A table is in 1NF if:

+ All columns contain atomic (indivisible) values.
+ Each column contains only one value per row.
+ Each row is unique.


### 2. Second Normal Form (2NF)

A table is in 2NF if:

+ It is in 1NF.
+ All non-key columns are fully functionally dependent on the primary key. This means that non-key columns must depend on the entire primary key, not just a part of it.

### 3. Third Normal Form (3NF)
A table is in 3NF if:

+ It is in 2NF.
+ All the columns are not only dependent on the primary key but also non-transitively dependent. This means that non-key columns must not depend on other non-key columns.

### 4. Boyce-Codd Normal Form (BCNF)
A table is in BCNF if:

+ It is in 3NF.
+ Every determinant is a candidate key. A determinant is any attribute on which some other attribute is fully functionally dependent.

### 5. Fourth Normal Form (4NF)
A table is in 4NF if:

+ It is in BCNF.
+ It has no multi-valued dependencies, meaning no column can have multiple independent values for a single primary key.

### 6. Fifth Normal Form (5NF)
A table is in 5NF if:

+ It is in 4NF.
+ It has no join dependencies, meaning it cannot be decomposed into any smaller tables without losing information.

---

## What are the ACID properties in the context of databases?

**Answer:** ACID stands for Atomicity, Consistency, Isolation, and Durability. These properties ensure reliable processing of database transactions.

+ **Atomicity:** Transactions are all-or-nothing.
+ **Consistency:** Transactions bring the database from one valid state to another.
+ **Isolation:** Transactions are isolated from each other.
+ **Durability:** Once a transaction is committed, it remains so.

---

## What is a JOIN in SQL? Explain the different types of JOINs.
**Answer:** A JOIN clause is used to combine rows from two or more tables based on a related column between them. Types of JOINs include:
+ **INNER JOIN:** Returns records with matching values in both tables.
+ **LEFT JOIN (or LEFT OUTER JOIN):** Returns all records from the left table, and the matched records from the right table.
+ **RIGHT JOIN (or RIGHT OUTER JOIN):** Returns all records from the right table, and the matched records from the left table.
+ **FULL JOIN (or FULL OUTER JOIN):** Returns all records when there is a match in either left or right table.
---

## What is a primary key and a foreign key?
**Answer:** A primary key is a column (or a set of columns) that uniquely identifies each row in a table. A foreign key is a column (or a set of columns) that establishes a link between the data in two tables.

---
## What is a non-relational (NoSQL) database?
**Answer:** A non-relational database, or NoSQL database, is a database that does not use the tabular schema of rows and columns found in most traditional database systems. NoSQL databases can store unstructured data and are often used for large-scale data storage.

---
## Explain the different types of NoSQL databases.

+ **Document Store:** Stores data as documents (e.g., MongoDB).
+ **Key-Value Store:** Stores data as key-value pairs (e.g., Redis).
+ **Wide-Column Store:** Uses tables, rows, and dynamic columns (e.g., Cassandra).
+ **Graph Database:** Stores data in graph structures with nodes, edges, and properties (e.g., Neo4j).

---

## What are the CAP theorem and its implications?
**Answer:** The CAP theorem states that it is impossible for a distributed data store to simultaneously provide all three of the following guarantees:

+ **Consistency:** Every read receives the most recent write or an error.
+ **Availability:** Every request receives a (non-error) response, without the guarantee that it contains the most recent write.
+ **Partition Tolerance:** The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network.

---
## What are the advantages and disadvantages of using NoSQL databases?

Answer:
+ **Advantages:** Scalability, flexibility in data models, schema-less design, and ability to handle large volumes of unstructured data.
+ **Disadvantages:** Potential lack of ACID compliance, eventual consistency, and fewer tools for complex queries compared to SQL databases.

---

## How do consistency models differ between relational and NoSQL databases?

**Answer:** Relational databases typically follow strong consistency models with ACID properties. NoSQL databases often follow eventual consistency models to ensure availability and partition tolerance as per the CAP theorem.


## Describe a use case where a graph database would be more appropriate than a relational database.

**Answer:** A graph database is ideal for applications involving complex relationships and interconnected data, such as social networks, recommendation systems, and fraud detection.