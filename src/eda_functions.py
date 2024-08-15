"""
This module contains custom functions for data analysis and visualization,
including statistical summaries, revenue calculations, and plotting tools. 
These functions are designed for use in data science workflows, and are 
integrated with standard libraries such as NumPy, Pandas, Matplotlib, and Seaborn.

The module is structured as follows:

1. IMPORT LIBRARIES:
   - Data manipulation libraries (NumPy, Pandas)
   - Data visualization libraries (Matplotlib, Seaborn)

2. SET STANDARDIZED VARIABLES:
   - Standard color palette for plotting (Seaborn Set2)

3. FUNCTIONS:
   - feature_stats: Calculates counts and percentage distribution of unique values.
   - feature_filtered_stats: Filters DataFrame and calculates counts and percentages.
   - feature_grouped_stats: Calculates mean and standard deviation of features grouped by another feature.
   - get_total_revenue: Calculates total revenue based on order cost and take rate.
   - metrics_to_dataframe: Converts metrics into a formatted DataFrame.
   - top_and_bottom_restaurants: Styles and displays top and bottom 5 restaurants based on a specified feature.
   - plot_count: Displays the distribution of a categorical feature in a horizontal count plot.
   - plot_histbox: Displays the distribution and outliers of a numerical feature using histogram and boxplot.
   - plot_boxplot_and_pointplot: Visualizes the relationship between a categorical feature and a numerical feature using boxplots and point plots.
"""

# ---------------------------------------------------------
# 1. IMPORT LIBRARIES
# ---------------------------------------------------------

# Import libraries for data manipulation
import numpy as np
import pandas as pd

# Import libraries for data visualization
import matplotlib.pyplot as plt
import seaborn as sns


# ---------------------------------------------------------
# 2. SET STANDARDIZED VARIABLES
# ---------------------------------------------------------

# Set standard color palette for plotting
palette_color = sns.color_palette("Set2")


# ---------------------------------------------------------
# 3. FUNCTIONS
# ---------------------------------------------------------


# Function to calculate the counts and percentage distribution of unique values for any categorical feature
def feature_stats(data, feature, n=None):
    """
    Calculate the counts and percentage distribution of unique values in a specified feature.

    Parameters:
    - data (DataFrame): The input DataFrame.
    - feature (str): The column name for which the statistics are calculated.
    - n (int, optional): The number of top results to return. If None, return all results.

    Returns:
    - DataFrame: A DataFrame containing the counts and percentages of unique values.
    """
    counts = data[feature].value_counts()
    percentages = data[feature].value_counts(normalize=True).mul(100).round(2)

    fstats_df = pd.DataFrame(
        {
            feature: counts.index,
            "count": counts.values,
            "percentage": percentages.values,
        }
    ).reset_index(drop=True)

    return fstats_df.head(n)


# Function to filter DataFrame and calculate the counts and percentage distribution of unique values for any categorical feature
def feature_filtered_stats(
    data, feature, filter_column, filter_value, ascending_sort=False
):
    """
    Filter DataFrame and compute the counts and percentage distribution of unique values in a specified feature.

    Parameters:
    data (pd.DataFrame): The input DataFrame.
    feature (str): The categorical feature to analyze.
    filter_column (str): The column to filter by.
    filter_value (str): The value to filter on.
    ascending_sort (bool): Sort order for the counts. Default is False (descending).

    Returns:
    pd.DataFrame: A DataFrame with counts and percentages of the specified feature.
    """
    # Filter data by the specified column and value
    filtered_df = data[data[filter_column] == filter_value]

    # Compute counts
    counts = filtered_df[feature].value_counts(ascending=ascending_sort)

    # Compute percentages
    total_counts = counts.sum()
    percentages = (counts / total_counts * 100).round(2)

    # Combine counts and percentages into a DataFrame
    combined_counts = pd.DataFrame(
        {
            f"count_{filter_value.lower()}": counts,
            f"percentage_{filter_value.lower()}": percentages,
        }
    ).fillna(0)

    return combined_counts.reset_index()


# Function to calculate and display the mean values of a feature grouped by another feature
def feature_grouped_stats(data, gbfeatures, features):
    """
    Calculate and display the mean and standard deviation of specified features
    grouped by another feature.

    Parameters:
    - data (pd.DataFrame): The input DataFrame containing the data.
    - gbfeatures (str or list): The feature(s) to group by.
    - features (str or list): The feature(s) for which to calculate the mean and standard deviation.

    Returns:
    - pd.DataFrame: A DataFrame with the grouped means and standard deviations, rounded to 2 decimal places.
    """
    filtered_df = data.groupby(gbfeatures)[features]

    fstats = filtered_df.agg(["mean", "std"]).round(2)
    return fstats.reset_index()


# Function to calculate total revenue based on order cost and take rate
def get_total_revenue(x, uL, lL):
    """
    Calculate total revenue based on order cost and take rate

    Parameters:
    x (float): Cost of the order.
    uL (float): Percentage for orders above $20.
    lL (float): Percentage for orders between $5 and $20.

    Returns:
    float: Calculated total revenue for the order.
    """
    if x > 20:
        return x * uL
    elif x > 5:
        return x * lL
    else:
        return 0


# Function to convert metrics into a DataFrame
def metrics_to_dataframe(**kwargs):
    """
    Converts metric names, their associcated values, and units into a formatted DataFrame.

    Args:
        kwargs: Variable number of keyword arguments where the key is the metric name
                and the value is a tuple containing the associated value and the unit symbol.

    Returns:
        pd.DataFrame: A DataFrame containing the metric names, their formatted values, and unit symbols.
    """
    # Create lists for metrics, values, and units
    metrics = []
    values = []
    units = []

    for metric, (value, symbol) in kwargs.items():
        metrics.append(metric)
        values.append(round(value, 2))
        units.append(symbol)

    # Create DataFrame
    dataframe = pd.DataFrame(
        {
            "metric": metrics,
            "unit": units,
            "value": values,
        }
    )

    return dataframe


# Function to calculate and style the top and bottom 5 restaurants based on a specified feature
def top_and_bottom_restaurants(data, filter_feature, delivery_threshold=10):
    """
    Generate a styled DataFrame showing the top 5 and bottom 5 restaurants
    based on the average of a specified feature, filtered by a minimum
    number of deliveries.

    Parameters:
    data (pd.DataFrame): The DataFrame containing restaurant data.
    filter_feature (str): The feature to calculate the average for (e.g., 'order_completion_time').
    delivery_threshold (int): The minimum number of deliveries required to be included (default is 10).

    Returns:
    styled_df (pd.io.formats.style.Styler): A styled DataFrame with top 5 and bottom 5 restaurants.
    """
    # Filter restaurants with more than the specified number of deliveries
    filtered_df = data.groupby("restaurant_name").filter(
        lambda x: len(x) > delivery_threshold
    )

    # Calculate the average order completion time
    average_time = (
        filtered_df.groupby("restaurant_name")[filter_feature]
        .mean()
        .sort_values()
        .round(2)
        .reset_index()
    )

    # Get the top 5 and last 5 restaurants
    top_5 = average_time.head(5)
    last_5 = average_time.tail(5)

    # Concatenate the top 5 and last 5 DataFrames
    average_time_df = pd.concat([top_5, last_5])

    # Rename columns
    average_time_df.rename(
        columns={filter_feature: f"average_{filter_feature}"}, inplace=True
    )

    # Function to add a border to the bottom edge of the 5th row
    def add_upper_border(row):
        return (
            ["border-bottom: 0.5px solid grey"] * len(row)
            if row.name == 4
            else [""] * len(row)
        )

    # Function to add a border to the bottom edge of the 5th row (index)
    def add_upper_border_index(val):
        return "border-bottom: 0.5px solid grey" if val == 4 else ""

    # Apply styles to the DataFrame
    styled_df = average_time_df.style.apply(add_upper_border, axis=1)
    styled_df = styled_df.applymap_index(add_upper_border_index, axis=0)
    styled_df = styled_df.format({f"average_{filter_feature}": "{:.2f}"})

    return styled_df


# Function to display the distribution of a categorical feature
def plot_count(data, feature, figsize=(14, 8)):
    """
    Display the distribution of a categorical feature in a horizontal count plot.

    Parameters:
    - data (DataFrame): The input DataFrame.
    - feature (str): The column name for which the distribution is plotted.
    - figsize (tuple, optional): The size of the figure. Default is (12, 7).

    Returns:
    - None: The function displays the plot.
    """
    # Sort the order
    sorted_count = data[feature].value_counts().sort_values(ascending=False)

    # Initiate figure
    plt.figure(figsize=figsize)

    # Plot countplot
    sns.countplot(
        data=data,
        y=feature,
        hue=feature,
        order=sorted_count.index,
        hue_order=sorted_count.index,
        palette=palette_color,
    )

    # Add title and grid
    formatted_title = feature.replace("_", " ").title()
    plt.title(f"Distribution of {formatted_title}s")
    plt.grid(axis="x", linestyle="--", linewidth=0.5)

    plt.tight_layout(pad=2.0)
    plt.show()


# Function to display the distribution, potential outliers and statistical summary of a numerical feature
def plot_histbox(data, feature, figsize=(14, 8)):
    """
    Display the distribution and outliers of a numerical feature using a histogram and boxplot.

    Parameters:
    - data (DataFrame): The input DataFrame.
    - feature (str): The column name for which the distribution and outliers are plotted.
    - figsize (tuple, optional): The size of the figure. Default is (12, 7).

    Returns:
    - None: The function displays the plots and prints key statistics.
    """
    # Obtain summary statistic of feature
    fstats = data[feature].describe().T
    fstats = fstats.loc[["mean", "50%", "std", "min", "max"]].to_dict()
    fstats["median"] = fstats.pop("50%")  # Rename the '50%' key to 'median'

    # Initiate figure
    fig, (ax1, ax2) = plt.subplots(
        2, 1, sharex=True, figsize=figsize, gridspec_kw={"height_ratios": [2, 1]}
    )

    # Plot histogram and boxplot
    sns.histplot(
        data,
        x=feature,
        kde=True,
        color=palette_color[0],
        edgecolor="darkgreen",
        linewidth=1.0,
        ax=ax1,
    )
    sns.boxplot(
        data,
        x=feature,
        color=palette_color[1],
        medianprops=dict(visible=True, color="black"),
        flierprops=dict(marker="o", markersize=3),
        ax=ax2,
    )

    # Add lines for max, mean, and median values
    ax1.axvline(
        fstats["mean"],
        color="red",
        linestyle="-",
        linewidth=1.5,
        label=f"Mean: {fstats['mean']:.2f}",
    )
    ax1.axvline(
        fstats["median"],
        color="black",
        linestyle="-",
        linewidth=1.5,
        label=f"Median: {fstats['median']:.2f}",
    )

    # Add legend, title and label
    ax1.legend(loc="upper right")
    formatted_title = feature.replace("_", " ").title()
    ax1.set_title(f"Distribution of {formatted_title}s")
    ax1.set_ylabel("count")

    plt.tight_layout(pad=2.0)
    plt.show()

    # Print the key statistics
    formatted_stats = ", ".join(
        [f"{key.capitalize()}: {value:.2f}" for key, value in fstats.items()]
    )
    print(formatted_stats)


# Function to visualize the relationship between a categorical feature and a numerical feature using boxplots and point plots
def plot_boxplot_and_pointplot(data, cat_feature, num_feature, scale_factor=0.5):
    """
    Visualize the relationship between a categorical feature and a numerical feature using boxplots and point plots.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing the data.
    - categorical_feature (str): The categorical feature to be plotted on the x-axis.
    - numerical_feature (str): The numerical feature to be plotted on the y-axis.
    - scale_factor (float): The scale factor for the point plot markers.

    Returns:
    - None: The function displays the plots and prints key statistics.
    """
    # Initiate figure
    plt.figure(figsize=(14, 8))

    # Plot boxplot
    sns.boxplot(
        data=data,
        x=cat_feature,
        y=num_feature,
        hue=cat_feature,
        palette=palette_color,
    )

    # Plot point plot
    sns.pointplot(
        data=data,
        x=cat_feature,
        y=num_feature,
        color="black",
        markers="D",
        linestyles="",
        scale=scale_factor,
        ci=None,
        estimator=np.mean,
    )

    # Plot an invisible scatter plot for the legend with the calculated size
    plt.scatter([], [], color="black", marker="D", s=scale_factor * 100, label="Mean")

    # Add legend
    plt.legend(loc="upper right")

    # Add title and grid
    plt.title(
        f"Relationship Between {cat_feature.replace('_', ' ').title()} and {num_feature.replace('_', ' ').title()}"
    )
    plt.grid(axis="y", linestyle="--", linewidth=0.5)

    plt.tight_layout(pad=2.0)
    plt.show()


# ---------------------------------------------------------
# ---------------------------------------------------------
