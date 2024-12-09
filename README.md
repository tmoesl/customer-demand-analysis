![FoodHub Banner](references/customer_demand_analysis_banner.png)

# Customer Demand Analysis For Online Delivery App

![Status](https://img.shields.io/badge/-Completed-34A853?style=flat&label=Project&labelColor=23555555)

## Executive Summary

FoodHub, an online food delivery app, faces the challenge of optimizing operations and enhancing customer satisfaction in a competitive market.
By leveraging exploratory data analysis (EDA) and key business metrics, this project provides actionable insights that address these challenges,
focusing on improving customer engagement, operational efficiency, and revenue growth.

**Key Outcomes**
- **Revenue**: Strong profitability with a 62.5% profit margin, GMV of $31,314.82, and net revenue of $3,853.06, providing a solid foundation for investment in growth initiatives. Top five restaurants drive 33.4% of orders, with an AOV of $16.50 and 29.24% of orders exceeding $20, showing demand for premium options.
- **Operational Efficiency**: Weekday delivery times are 26.1% longer than weekends, revealing bottlenecks impacting customer satisfaction and retention.
- **Customer Engagement**: Over 70% of orders come from American, Japanese, and Italian cuisines. NPS is 34.42%, and CRR is 21.92%, with opportunities to boost customer loyalty and satisfaction.

**Actionable Recommendations**
- **Revenue**: Expand top restaurant partnerships, optimize menu pricing with tiered and bundled offers, and target high-demand cuisines (American, Japanese, and Italian) to align with customer preferences, boosting GMV and driving order growth.
- **Operational Efficiency**: Optimize weekday deliveries with better routes and staffing during peak hours to reduce delays and improve efficiency.
- **Customer Engagement**: Launch loyalty programs to retain top customers and attract new ones, boosting revenue, customer retention and acquisition. Encourage feedback with incentives to improve customer satisfaction metrics (NPS, CSAT and CRR).

## Table of Contents

- [Introduction](#introduction)
- [Objective](#objective)
- [Key Business Metrics](#key-business-metrics)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Data Insights](#data-insights)
- [Business Recommendations](#business-recommendations)
- [Repository Structure](#repository-structure)
- [Requirements](#requirements)
- [Installation](#installation)

## Introduction

The Customer Demand Analysis project involves an exploratory data analysis (EDA) of transactional data from an online food ordering and delivery app serving New York restaurants. In the highly competitive food delivery market, data-driven insights are critical for optimizing operations, improving customer satisfaction, and achieving sustainable long-term growth.

## Objective

This project aims to transform raw data into strategic metrics, offering actionable recommendations that align with business objectives. By identifying these key metrics, the analysis provides a foundation for enhancing platform performance and customer loyalty.

## Key Business Metrics

**Revenue Metrics**
- **Gross Merchandise Value (GMV)**: Total value of all orders processed, reflecting overall sales performance.
- **Total Revenue**: Income generated after applying commission rates, representing gross earnings.
- **Net Revenue**: Profit after deducting operating costs, indicating overall profitability.
- **Profit Margin**: Percentage of revenue retained as profit after expenses, showing financial efficiency.
- **Average Order Value (AOV)**: Average spend per order, highlighting customer spending behavior.

**Operational Efficiency Metrics**
- **Order Volume**: Total number of orders placed, indicating platform demand and usage.
- **Order Completion Time**: Average time from order placement to delivery, reflecting operational efficiency.
- **Delivery Times**: Average delivery duration, highlighting delivery performance and efficiency.

**Customer Engagement Metrics**
- **Customer Retention Rate (CRR)**: Percentage of repeat customers, indicating loyalty.
- **Net Promoter Score (NPS)**: Customer satisfaction and likelihood to recommend the service.
- **Customer Satisfaction Score (CSAT)**: A direct measure of customer satisfaction based on post-order feedback.
- **Customer Rating Participation Rate (CRPR)**: Percentage of orders with customer ratings, reflecting engagement and feedback quality.

## Exploratory Data Analysis

The following data analysis and visualization techniques were employed:

1. **Data Cleaning and Preprocessing**: Addressing missing values, correcting data inconsistencies, and engineering new features to enhance analysis.
2. **Descriptive Statistics**: Summarizing the data to understand the distribution of key features and investigating key business metrics.
3. **Univariate Analysis**: Analyzing the distribution of individual features to identify trends, outliers, and patterns within the dataset.
4. **Multivariate Analysis**: Examining relationships between multiple features, to uncover interactions and correlations.
5. **Visualizations**: Utilizing various plots and heatmaps to visually explore data and uncover insights.


## Data Insights

These insights, supported by key metrics, offer a comprehensive evaluation of performance, covering operational efficiency, financial health, customer preferences, restaurant performance, and overall customer satisfaction, providing a well-rounded understanding of the business landscape and opportunities for growth.

1. **Revenue Insights**
   - **Cuisine Popularity**: American, Japanese, and Italian cuisines dominate over 70% of orders on both weekends and weekdays, with stable customer preferences. Average order ratings for these cuisines range from 4.30 to 4.37, with Spanish and Thai cuisines rated higher but based on fewer reviews.
   - **Menu Cost**: The AOV is $16.50, with 29.24% of orders exceeding $20, showing strong demand for premium options.
   - **Restaurant Performance**: The top five restaurants generate 33.4% of orders, with Shake Shack leading in GMV at $3,579.53, while nearly 80% of restaurants struggle with fewer than 10 orders.
   - **Financial Metrics**: The GMV is $31,314.82, with a profit margin of 62.5% and net revenue of $3,853.06, showcasing strong financial performance.

2. **Operational Efficiency**
   - **Delivery Times**: Weekday delivery times are 26.1% longer than weekends, indicating inefficiencies during non-leisure periods.
   - **Order Completion**: Average order completion time is 51.53 minutes, with 10.54% of orders exceeding 60 minutes, highlighting potential bottlenecks.

3. **Customer Engagement**
   - **Customer Activity**: A small, highly active group of customers (less than 1%) contributes over 5% of total orders, reflecting the importance of retaining these top customers. Weekends see a 71.18% spike in orders, indicating higher demand during leisure periods.
   - **Customer Satisfaction**: The NPS is 34.42%, showing positive customer sentiment, while the CRR is 21.92%, indicating room for improved retention. 
   - **Feedback Participation**: With a CRPR of 61.22%, a significant portion of orders remain unrated, limiting the depth of customer feedback.

***Note**: The current dataset lacks timestamped information, limiting the ability to analyze changes over time in key business areas.*

## Business Recommendations

The following recommendations are strategically designed to optimize key business metrics across customer engagement, operational efficiency, revenue generation, and market expansion, ensuring sustained growth and competitive advantage in the food delivery market.

1. **Revenue Optimization**
   - **Expand Partnerships with Top Restaurants**: Collaborate with top-performing venues and explore premium memberships and targeted advertising to boost GMV and revenue growth.
   - **Promote High-Demand Cuisines**: Focus marketing efforts on American, Japanese, and Italian cuisines to increase order volume and revenue.
   - **Support Low-Performing Restaurants**: Provide tailored support and promotional partnerships to low-performing venues, driving order volume and market share.
   - **Optimize Menu Pricing**: Introduce tiered pricing and bundle offers to increase AOV and maximize revenue from high-value orders.

2. **Operational Efficiency**
   - **Optimize Weekday Deliveries**: Streamline routes and staffing during peak hours to reduce weekday delivery times, improving driver utilization, order completion, and customer satisfaction.
   - **Scale Weekend Operations**: Expand staffing and logistics to manage high weekend demand, reducing order completion times and maintaining service quality.
   - **Enhance Data Collection**: Implement timestamp tracking to analyze trends, seasonality, supporting long-term growth strategies by driving active user growth, reducing customer churn, and improving order accuracy and fulfillment.

3. **Customer Engagement**
   - **Launch Loyalty Programs**: Introduce targeted promotions and rewards to retain top customers and attract new ones, boosting revenue, customer retention and acquisition. 
   - **Boost Feedback Participation**: Use prompts, notifications, and incentives to increase customer feedback rates, improving NPS and retention metrics.

## Repository Structure
```
├── LICENSE            <- Project's open-source license details.
├── README.md          <- Top-level README for developers.
│
├── requirements.txt   <- Python dependencies for replicating the environment.
├── environment.yml    <- Conda environment configuration with dependencies.
│
├── data
│   ├── processed      <- The final, processed data sets for modeling.
│   └── raw            <- The original, immutable data.
│
├── notebooks          <- Jupyter notebooks for data exploration and analysis.
│
├── references         <- Documentation, data dictionaries, and manuals.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Graphics and figures for reports.
│
├── src                <- Source code for the project.
```

## Requirements

`Python 3.11.6` or higher is required. Download the latest version here: [python.org](https://www.python.org)

## Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/tmoesl/customer-demand-analysis.git
```

#### 2. Navigate to the Project Directory
```bash
cd customer-demand-analysis
```

#### 3. Create a Virtual Environment and Install the Required Dependencies

Using `conda`:
```bash
conda env create -f environment.yml
conda activate customer-demand-analysis-env
```

Using `venv`:
```bash
python3.12.3 -m venv customer-demand-analysis-env
source customer-demand-analysis-env/bin/activate  # On Windows: .\customer-demand-analysis-env\Scripts\activate
pip install -r requirements.txt
```

#### 4. Set up the Environment Variables
- Create a `.env` file in the project root directory.
- Add the following variables to the file:

```
PYTHONPATH=../src
DATA_DIR=../data/raw
```
---