import mysql.connector
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="greyson",
    database="jobsync"
)

# Check building_id repeats (not dupes—multiple jobs)
df_buildings = pd.read_sql("""
    SELECT building_id, COUNT(*) as job_count 
    FROM contract_jobs 
    GROUP BY building_id 
    HAVING job_count > 1 
    LIMIT 5
""", conn)
print("Buildings with Multiple Jobs:")
print(df_buildings)

# 1. Total Cost by Project Type
df_project = pd.read_sql("""
    SELECT project_type, SUM(current_wa_total_amt) AS total_cost
    FROM contract_jobs
    GROUP BY project_type
    ORDER BY total_cost DESC
""", conn)
print("\nTotal Cost by Project Type:")
print(df_project)
sns.barplot(x="project_type", y="total_cost", data=df_project)
plt.title("Total Cost by Project Type")
plt.xticks(rotation=45)
plt.savefig("project_costs.png")
plt.clf()

# 2. Cost Trends Over Time
df_time = pd.read_sql("""
    SELECT DATE_FORMAT(service_initiation_date, '%Y-%m') AS month, 
           SUM(current_wa_total_amt) AS monthly_cost
    FROM contract_jobs
    GROUP BY month
    ORDER BY month
""", conn)
print("\nCost Trends Over Time:")
print(df_time)
sns.lineplot(x="month", y="monthly_cost", data=df_time)  # Fixed typo
plt.title("Cost Trends Over Time")
plt.xticks(rotation=45)
plt.savefig("cost_trends.png")
plt.clf()

# 3. Cost by Priority
df_priority = pd.read_sql("""
    SELECT priority, SUM(current_wa_total_amt) AS total_cost
    FROM contract_jobs
    GROUP BY priority
    ORDER BY total_cost DESC
""", conn)
print("\nCost by Priority:")
print(df_priority)
sns.barplot(x="priority", y="total_cost", data=df_priority)
plt.title("Cost by Priority")
plt.savefig("priority_costs.png")

# Close connection
conn.close()
