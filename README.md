![FoodHub Banner](references/customer_demand_analysis_banner.png)

# Customer Demand Analysis For Online Delivery App

![Status](https://img.shields.io/badge/-Completed-34A853?style=flat&label=Project&labelColor=23555555)

## Table of Contents

- [Introduction](#introduction)
- [Key Business Metrics](#key-business-metrics)
- [Exploratory Data Analysis and Visualization](#exploratory-data-analysis-and-visualization)
- [Data Insights](#data-insights)
- [Business Recommendations](#business-recommendations)
- [Repository Structure](#repository-structure)
- [Requirements](#requirements)
- [Installation](#installation)

## Introduction

The Customer Demand Analysis project involves a comprehensive exploratory data analysis (EDA) of sample data from an online food ordering and delivery app used by New York restaurants. The primary objective is to uncover key business metrics that will optimize operations, enhance customer satisfaction, and drive sustainable long-term growth. 

Through data-driven insights, this project demonstrates the transformation of raw data into strategic business metrics, providing actionable recommendations that align with business goals and long-term success.

## Key Business Metrics

1. **Gross Merchandise Value (GMV)**: The total value of all orders processed through the platform, indicating overall sales performance.
2. **Total Revenue**: The total income generated from all orders after applying commission rates, reflecting the platform's gross earnings.
3. **Net Revenue**: The income remaining after deducting operating costs from total revenue, indicating profitability.
4. **Profit Margin**: The percentage of revenue that remains as profit after all expenses, showing the platform's financial efficiency.
5. **Average Order Value (AOV)**: The average amount spent per order, indicating customer spending behavior.
6. **Order Volume**: The total number of orders placed on the platform, reflecting demand and platform usage.
7. **Order Completion Time**: The average time taken from order placement to delivery, indicating the platform’s operational efficiency.
8. **Delivery Times**: The average time taken for orders to be delivered, indicating the platform’s delivery efficiency.
9. **Customer Retention Rate**: The percentage of customers who return to place additional orders, indicating customer loyalty.
10. **Net Promoter Score (NPS)**: A measure of customer satisfaction based on their likelihood to recommend the service, reflecting overall customer sentiment.
11. **Customer Rating Participation Rate**: The percentage of orders that receive customer ratings, indicating engagement and feedback quality.

## Exploratory Data Analysis and Visualization

The following data analysis and visualization techniques were employed:

1. **Data Cleaning and Preprocessing**: Addressing missing values, correcting data inconsistencies, and engineering new features to enhance analysis.
2. **Descriptive Statistics**: Descriptive Statistics: Summarizing the data to understand the distribution of key features and investigating key business metrics.
3. **Univariate Analysis**: Analyzing the distribution of individual features to identify trends, outliers, and patterns within the dataset.
4. **Multivariate Analysis**: Examining relationships between multiple features, to uncover interactions and correlations.
5. **Visualizations**: Utilizing various plots and heatmaps to visually explore data and uncover insights.


## Data Insights

These insights, supported by key metrics, offer a comprehensive evaluation of performance, covering operational efficiency, financial health, customer preferences, restaurant performance, and overall customer satisfaction, providing a well-rounded understanding of the business landscape and opportunities for growth.

1. **Order Volume**
   - Weekends see a 71.18% spike in orders, indicating higher demand during leisure periods.
   - A small, highly active group of customers (less than 1%) contributes over 5% of total orders.

2. **Cuisine Popularity and Rating**
   - American, Japanese, and Italian cuisines dominate over 70% of orders on both weekends and weekdays, with stable customer preferences.
   - Average **Order Ratings** for these cuisines range from 4.30 to 4.37, with Spanish and Thai cuisines rated higher but based on fewer reviews.

3. **Menu Cost**
   - The **Average Order Value (AOV)** is \$16.50, reflecting typical spending on moderately priced purchases.
   - 29.24% of orders exceed \$20, showing a significant demand for premium or larger-sized orders.

4. **Restaurant Performance**
   - The top 5 restaurants account for 33.4% of total orders, with Shake Shack leading in **GMV** at \$3,579.53.
   - Nearly 80% of restaurants have fewer than 10 orders, indicating concentrated demand among a few venues.

5. **Financial Metrics**
   - The **Gross Merchandise Value (GMV)** totals \$31,314.82, highlighting strong overall sales performance.
   - The **Profit Margin** is robust at 62.5%, with **Net Revenue** after costs standing at \$3,853.06.

6. **Operational Efficiency**
   - **Order Completion Times** average 51.53 minutes, with 10.54% of orders taking over 60 minutes.
   - Weekday **Delivery Times** are 26.1% longer than weekend deliveries, likely due to increased traffic and reduced staffing.

7. **Customer Satisfaction**
   - The **Net Promoter Score (NPS)** is 34.42%, indicating generally positive customer sentiment.
   - The **Customer Retention Rate** is 21.92%, with a **Customer Rating Participation Rate** of 61.22%, leaving a significant portion of orders unrated.


## Business Recommendations

The following recommendations are strategically designed to optimize key business metrics across customer engagement, operational efficiency, revenue generation, and market expansion, ensuring sustained growth and competitive advantage in the food delivery market.

1. **Target Promotions and Rewards Programs**
   - **Insight**: A small, highly active customer, less than 1%, base disproportionately influences order volume.
   - **Strategy**: Implement targeted loyalty programs and personalized promotions to retain high-activity customers and attract new ones.
   - **Business Metrics**: Customer Retention, New Customer Acquisition, Customer Conversion, Revenue Growth.

2. **Improve Weekday Delivery Efficiency**
   - **Insight**: Weekday delivery times are significantly longer and more variable than weekends.
   - **Strategy**: Optimize routes, adjust staffing during peak hours, and streamline restaurant operations.
   - **Business Metrics**: Driver Utilization, Average Delivery Distance, Delivery Times, Cost per Delivery.

3. **Enhance Weekend Operations**
   - **Insight**: Order volume surges over weekends, creating high demand periods.
   - **Strategy**: Optimize staffing and logistics to maintain operational efficiency and low delivery times during peak order periods, preparing for future growth.
   - **Business Metrics**: Order Completion Time, Driver Utilization.

4. **Address Rating Gaps**
   - **Insight**: Nearly 40% of rating scores are missing, affecting customer satisfaction metrics.
   - **Strategy**: Encourage customer feedback through follow-up prompts, push notifications and incentives.
   - **Business Metrics**: Customer Rating Participation Rate, Net Promoter Score (NPS).

5. **Leverage High-Performing Cuisines**
   - **Insight**: American, Japanese, and Italian cuisines dominate orders on both weekends and weekdays, reflecting strong customer preferences.
   - **Strategy**: Focus marketing efforts on these popular cuisines, offering exclusive deals to increase engagement.
   - **Business Metrics**: Order Volume, Customer Retention, Revenue Growth.

6. **Expand Revenue Opportunities**
   - **Insight**: Top-performing restaurants generate a significant portion of total orders and revenue.
   - **Strategy**: Expand partnerships with these restaurants and explore new revenue streams like premium memberships and targeted advertising.
   - **Business Metrics**: Gross Merchandise Value, Revenue Growth, Order Volume, Profit Margin.

7. **Restaurant Development**
   - **Insight**: Most restaurants have fewer than 10 orders, struggling to attract customers.
   - **Strategy**: Provide tailored support and promotional partnerships to low-activity restaurants.
   - **Business Metrics**: Customer Retention, New Customer Acquisition, Order Volume, Market Share.

8. **Optimize Menu Pricing and Offerings**
   - **Insight**: A significant portion of orders exceeds \$20, showing a demand for premium options.
   - **Strategy**: Implement tiered pricing and bundled offers, while monitoring customer satisfaction.
   - **Business Metrics**: Average Order Value, Revenue Growth, Customer Retention.

9. **Explore Additional Metrics for Market Expansion**
   - **Insight**: Additional data is needed to optimize performance across key business areas.
   - **Strategy**: Collect and analyze new data to refine business strategies and accelerate market expansion.
   - **Business Metrics**: Active User Growth, Customer Churn, Cost Per Acquisition (CPA), Order Accuracy and Fulfillment, Market Share.


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

Python 3.11.6 or higher is required. The latest version of Python can be downloaded from the official website [python.org](https://www.python.org).

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

Note: Python 3.11.6 or higher is required.

Using `conda`:
```bash
conda env create -f environment.yml
conda activate customer-demand-analysis-env
```

Using `venv`:
```bash
python3.11.6 -m venv customer-demand-analysis-env
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