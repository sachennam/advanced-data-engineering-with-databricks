# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Getting Started
# MAGIC 
# MAGIC In this lesson we will introduce our courseware, various conventions and finally review this course's agenda.
# MAGIC 
# MAGIC ## Learning Objectives
# MAGIC By the end of this notebook, students will be able to:
# MAGIC - Configure the learning environment by running the **`Classroom-Setup`** scripts.
# MAGIC - Identify Python and Hive variables provided by the courseware.
# MAGIC - Identify utility functions provided by the courseware
# MAGIC - Install the datasets used by this course
# MAGIC - Enumerate the modules and lessons covered by this course.

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Classroom-Setup
# MAGIC 
# MAGIC For each lesson to execute correctly, please make sure to run the **`Classroom-Setup`** cell at the start of each lesson.
# MAGIC 
# MAGIC These setup scripts configure different assets in the workspace as needed for each lesson

# COMMAND ----------

# MAGIC %run ./Includes/Classroom-Setup

# COMMAND ----------

# MAGIC %md
# MAGIC ## Courseware Conventions
# MAGIC 
# MAGIC While not a pattern that is generally recommended, these notebooks will use various Hive variables to substitute in various values.
# MAGIC 
# MAGIC In this example, we can see the database name, your prescribed working directory and the location of your database.
# MAGIC 
# MAGIC These and other values are designed to avoid collisions between each student when creating databases, tables and writing files.
# MAGIC 
# MAGIC The following cell demonstrates this pattern.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT '${da.db_name}' as db_name, 
# MAGIC        '${da.paths.working_dir}' as working_dir,
# MAGIC        '${da.paths.user_db}' as user_db_path

# COMMAND ----------

# MAGIC %md Simmilarly, these values are availble in python as we can see below.

# COMMAND ----------

print(f"User Database:     {DA.db_name}")
print(f"Working Directory: {DA.paths.working_dir}")
print(f"User DB Path:      {DA.paths.user_db}")

# COMMAND ----------

# MAGIC %md
# MAGIC There are two important things to note here:
# MAGIC 1. The difference in case between Python variables and Hive variables: upper vs lower case
# MAGIC 2. The subtile difference in how Python and Hive SQL implement string interpolation: **`{python_variable}`** vs **`${hive_variable}`**

# COMMAND ----------

# MAGIC %md
# MAGIC Throughout this course you will see various references to **`DA...`** and **`da...`**, all a reference to Databricks Academy.
# MAGIC 
# MAGIC In all cases, these values and functions are provided by this course for educational purposes and are not part of any core API.

# COMMAND ----------

# MAGIC %md ## Install Datasets
# MAGIC 
# MAGIC Next, we need to "install" the datasets this course uses by copying them from their current location in the cloud to a location relative to your workspace.
# MAGIC 
# MAGIC All that is required is to run the following cell. 
# MAGIC 
# MAGIC By default, the **`install_datasets()`** function will not reinstall the datasets upon <br/>subsequent invocation but this behavior can be adjusted by modifying the parameters below.

# COMMAND ----------

DA.install_datasets(reinstall=False)

# COMMAND ----------

# MAGIC %md
# MAGIC # Agenda
# MAGIC 
# MAGIC While the install completes, we can review the Agenda and then start lesson #1.
# MAGIC 
# MAGIC By the time you are ready to start lesson #2, the "install" should have been completed.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 00 - Getting Started
# MAGIC * [Getting Started - Agenda]($./00 - Getting Started - Agenda)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 01 - OPTIONAL Review
# MAGIC * [ADE 1.1 - Setting Up Tables]($./01 - OPTIONAL Review/ADE 1.1 - Setting Up Tables)
# MAGIC * [ADE 1.2 - Optimizing Data Storage]($./01 - OPTIONAL Review/ADE 1.2 - Optimizing Data Storage)
# MAGIC * [ADE 1.3 - Understanding Delta Lake Transactions]($./01 - OPTIONAL Review/ADE 1.3 - Understanding Delta Lake Transactions)
# MAGIC * [ADE 1.4 - Using Clone with Delta Lake]($./01 - OPTIONAL Review/ADE 1.4 - Using Clone with Delta Lake)
# MAGIC * [ADE 1.5 - Auto Loader]($./01 - OPTIONAL Review/ADE 1.5 - Auto Loader)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 02 - Architecting for the Lakehouse
# MAGIC * [ADE 2.1 - Streaming Design Patterns]($./02 - Architecting for the Lakehouse/ADE 2.1 - Streaming Design Patterns)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 03 - Bronze Ingestion Patterns
# MAGIC * [ADE 3.1 - Auto Load to Multiplex Bronze]($./03 - Bronze Ingestion Patterns/ADE 3.1 - Auto Load to Multiplex Bronze)
# MAGIC * [ADE 3.2 - Streaming from Multiplex Bronze]($./03 - Bronze Ingestion Patterns/ADE 3.2 - Streaming from Multiplex Bronze)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 04 - Promoting to Silver
# MAGIC * [ADE 4.1 - Streaming Deduplication]($./04 - Promoting to Silver/ADE 4.1 - Streaming Deduplication)
# MAGIC * [ADE 4.2 - Quality Enforcement]($./04 - Promoting to Silver/ADE 4.2 - Quality Enforcement)
# MAGIC * [ADE 4.3 - Promoting to Silver]($./04 - Promoting to Silver/ADE 4.3 - Promoting to Silver)
# MAGIC * [ADE 4.4 - Type 2 SCD]($./04 - Promoting to Silver/ADE 4.4 - Type 2 SCD)
# MAGIC * [ADE 4.5 - Stream Static Join]($./04 - Promoting to Silver/ADE 4.5 - Stream Static Join)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 05 - Gold Query Layer
# MAGIC * [ADE 5.1 - Stored Views]($./05 - Gold Query Layer/ADE 5.1 - Stored Views)
# MAGIC * [ADE 5.2 - Materialized Gold Tables]($./05 - Gold Query Layer/ADE 5.2 - Materialized Gold Tables)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 06 - Storing Data Securely
# MAGIC * [ADE 6.1 - PII Lookup Table]($./06 - Storing Data Securely/ADE 6.1 - PII Lookup Table)
# MAGIC * [ADE 6.2 - Storing PII Securely]($./06 - Storing Data Securely/ADE 6.2 - Storing PII Securely)
# MAGIC * [ADE 6.3 - Deidentified PII Access]($./06 - Storing Data Securely/ADE 6.3 - Deidentified PII Access)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 07 - Propagating Updates and Deletes
# MAGIC * [ADE 7.1 - Processing Records from Change Data Feed]($./07 - Propagating Updates and Deletes/ADE 7.1 - Processing Records from Change Data Feed)
# MAGIC * [ADE 7.2 - Propagating Deletes with CDF]($./07 - Propagating Updates and Deletes/ADE 7.2 - Propagating Deletes with CDF)
# MAGIC * [ADE 7.3 - Deleting at Partition Boundaries]($./07 - Propagating Updates and Deletes/ADE 7.3 - Deleting at Partition Boundaries)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 08 - Orchestration and Scheduling
# MAGIC 
# MAGIC * ADE 4.01 - Multi-Task Jobs
# MAGIC   * [Task_1, Create Database]($./08 - Orchestration and Scheduling/ADE 8.1 - Multi-Task Jobs/Task_1, Create Database)
# MAGIC   * [Task_2, From Task 2]($./08 - Orchestration and Scheduling/ADE 8.1 - Multi-Task Jobs/Task_2, From Task 2)
# MAGIC   * [Task_3, From Task 3]($./08 - Orchestration and Scheduling/ADE 8.1 - Multi-Task Jobs/Task_3, From Task 3)
# MAGIC   * [Task_4, Key-Param]($./08 - Orchestration and Scheduling/ADE 8.1 - Multi-Task Jobs/Task_4, Key-Param)
# MAGIC   * [Task_5, Create task_5]($./08 - Orchestration and Scheduling/ADE 8.1 - Multi-Task Jobs/Task_5, Create task_5)
# MAGIC   * [Task_6, Errors]($./08 - Orchestration and Scheduling/ADE 8.1 - Multi-Task Jobs/Task_6, Errors)
# MAGIC   * [Task_7, Cleanup]($./08 - Orchestration and Scheduling/ADE 8.1 - Multi-Task Jobs/Task_7, Cleanup)
# MAGIC * [ADE 8.2 - OPTIONAL Error Prone]($./08 - Orchestration and Scheduling/ADE 8.2 - OPTIONAL Error Prone)
# MAGIC * ADE 8.3 - Deploying Workloads
# MAGIC   * [1 - Reset Pipelines]($./08 - Orchestration and Scheduling/ADE 8.3 - Deploying Workloads/1 - Reset Pipelines)
# MAGIC   * [2 - Schedule Streaming Jobs]($./08 - Orchestration and Scheduling/ADE 8.3 - Deploying Workloads/2 - Schedule Streaming Jobs)
# MAGIC   * [3 - Schedule Batch Jobs]($./08 - Orchestration and Scheduling/ADE 8.3 - Deploying Workloads/3 - Schedule Batch Jobs)
# MAGIC   * [4 - Streaming Progress]($./08 - Orchestration and Scheduling/ADE 8.3 - Deploying Workloads/4 - Streaming Progress)

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
