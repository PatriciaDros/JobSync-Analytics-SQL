# JobSync Analytics: Precision Financial Analysis of Job Contracts

**Unlocking fiscal insights through data-driven strategies**  
*Authored by Patricia Dros, March 27, 2025*

---

## Project Overview
JobSync Analytics delivers a robust financial dissection of job contract data, leveraging advanced SQL queries, Python analytics, and dynamic visualizations to empower stakeholders with actionable intelligence. This project aggregates and analyzes cost structures across 2,032 job contracts, spotlighting expenditure by project type, temporal cost trajectories, and priority-based resource allocation—key metrics for optimizing operational budgets and forecasting fiscal trends.

---

## Financial Objectives
- **Cost Aggregation:** Quantify total expenditures by project type to identify high-yield investment areas.
- **Trend Analysis:** Map cost trajectories over 161 months (2007–2025) for strategic forecasting and seasonality detection.
- **Priority Allocation:** Assess financial commitments across priority tiers to refine resource deployment and enhance ROI.

---

## Data Assets
- **Source:** Seven `.xlsx` files (e.g., `ALL CONTRACT JOBS.xlsx`), ingested into MySQL’s `jobsync` database.
- **Volume:** 2,032 job records in `contract_jobs`, enriched with auxiliary tables (`job_info`, `labs`, etc.).
- **Key Metrics:**
  - `building_id`: Job identifier—multiple jobs per building reflect real-world complexity (e.g., `K138`: 16 jobs).
  - `current_wa_total_amt`: Expenditure per job (in USD).
  - `project_type`: Investment categories (e.g., `CIP`, `CAPACITY`).
  - `service_initiation_date`: Temporal anchor for trend analysis.
  - `priority`: Resource prioritization flag.

---

## Technical Framework
- **Environment:** Ubuntu, MySQL, Python (Anaconda `jobsync` env), Git.
- **Pipeline:**
  1. **Data Ingestion:** `load_data.py`—seamless ETL from `.xlsx` to MySQL.
  2. **SQL Optimization:** Fixed socket issues (`/etc/mysql/my.cnf`), ensured data integrity (2,032 rows validated).
  3. **Python Analytics:** `query.py`—SQL queries via `mysql.connector`, processed with `pandas`, visualized with `seaborn`/`matplotlib` (Agg backend).
  4. **Version Control:** GitHub-hosted—clean commits, reproducible results.

---

## Financial Insights
### 1. Expenditure by Project Type
- **Query:** Aggregated `current_wa_total_amt` by `project_type`.
- **Output:** `project_costs.png`
  - `CIP`: $20,273,749.05—dominant capital investment.
  - `CAPACITY`: $950,798.94—targeted capacity expansion.
- **Takeaway:** `CIP` drives 95% of total spend—prime candidate for cost optimization.

### 2. Cost Trajectory Over Time
- **Query:** Monthly sums of `current_wa_total_amt` (2007–2025).
- **Output:** `cost_trends.png`
  - Span: 161 months—$9,601.25 (2007-09) to $20,075.00 (2025-02).
  - Peak: $84,446.56 (2024-12)—potential seasonal surge.
- **Takeaway:** Upward trend signals rising operational costs—forecasting needed.

### 3. Priority-Based Cost Allocation
- **Query:** Costs grouped by `priority`.
- **Output:** `priority_costs.png`
  - (Sample pending—e.g., “High”: $15M, “Low”: $5M—run `query.py` for exacts).
- **Takeaway:** High-priority jobs likely dominate—ROI analysis recommended.

---

## Key Deliverables
- **`query.py`:** Core script—SQL-to-visualization pipeline.
- **Visualizations:**
  - `project_costs.png`: Bar chart of project type expenditures.
  - `cost_trends.png`: Line chart of cost trends.
  - `priority_costs.png`: Bar chart of priority allocations.
- **GitHub:** [JobSync-Analytics-SQL](https://github.com/PatriciaDros/JobSync-Analytics-SQL)—live, employer-ready.

---

## Technical Highlights
- **Overcame:** MySQL `ERROR 2002`—socket fixed in `my.cnf`.
- **Validated:** 2,032 jobs with multi-job buildings (e.g., `K138`: 16 jobs)—real-world data integrity.
- **Skills Demonstrated:**
  - **SQL:** Complex aggregations, temporal formatting.
  - **Python:** Data processing (`pandas`), visualization (`seaborn`).
  - **Troubleshooting:** CLI mastery, environment management.

---

## Future Enhancements
- **Multi-Table Analysis:** Join `contract_jobs` with `job_info` for technician efficiency metrics.
- **Forecasting Models:** Predict future costs with time-series analysis.
- **Dashboard:** Tableau integration for interactive financial reporting.

---

## Why Hire Me?
This project showcases my ability to transform raw financial data into strategic insights—delivering cost visibility, trend detection, and priority optimization with precision and flair. I’m ready to drive your fiscal decision-making with data—let’s talk!

**Contact:** www.linkedin.com/in/tricia-dataanalyst
