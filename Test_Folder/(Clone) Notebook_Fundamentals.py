# Databricks notebook source
# MAGIC %md
# MAGIC SELECT "Hello"

# COMMAND ----------

# MAGIC %run ./Notebook_Fundamentals_2

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls 'databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.ls('databricks-datasets')

# COMMAND ----------

files = dbutils.fs.ls('databricks-datasets')
print(files)

# COMMAND ----------

display(files)
