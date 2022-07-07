# BUILDING DATA WAREHOUSE

Project Description

The objective of the project is to build a data warehouse. Starting with ETL, which stands for extract, transform, and load, 
is the process data engineers use to extract data from different sources, and transform the data into a usable and trusted 
resource. After that load the data into the systems end-users can access and use downstream to solve business problems.

•	Cleaned The Data

First, I have to start by cleaning our data. which is detecting and removing errors and inconsistencies from data to improve 
the quality of data. And in order to provide access to accurate and consistent data, consolidation of different data representations and 
elimination of duplicate information become necessary. To clean a raw data I used Pandas which is a Python library and Jupyter notebook as a tool.

•	Constructing ETL Data Pipelines 

In the process of constructing a data pipeline, I consider Setting up a secure and reliable data flow. An ETL pipeline is the set of 
processes used to move data from a source or multiple sources into a database such as a data warehouse. ETL stands for “extract, transform, 
load,” the three interdependent processes of data integration used to pull data from one database and move it to another. Once loaded, data can be
used for reporting, analysis, and deriving actionable business insights.

•	Stored Data To Warehouse

A data warehouse is a large collection of business data used to help an organization make decisions. a data warehouse periodically pulls 
data from those apps and systems; then, the data goes through formatting and import processes to match the data already in the warehouse. 
The data warehouse stores this processed data so it’s ready for decision makers to access. How frequently data pulls occur, or how data is 
formatted, etc., will vary depending on the needs of the organization.

A Data Mart is focused on a single functional area of an organization and contains a subset of data stored in a Data Warehouse. A Data Mart is 
a condensed version of Data Warehouse and is designed for use by a specific department, unit or set of users in an organization. 
After cleaned the data I used postgresql to transform it into different tables or data marts. To make the tables I used SQL querys with primary 
and foreign keys. By selecting the relevant views and filtering out unnecessary columns from the Data Warehouse, I build out each Data Mart.


