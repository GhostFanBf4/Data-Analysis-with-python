import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('../Data/epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    x_prediction = pd.Series([i for i in range(1880, 2051)])
    y_prediction = res.intercept + res.slope*x_prediction

    plt.plot(x_prediction, y_prediction, color='red', linewidth=3)
    # Create second line of best fit
    df_2000 = df.loc[df['Year'] >= 2000]

    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])

    x_prediction_2000 = pd.Series([i for i in range(2000, 2051)])
    y_prediction_2000 = res_2000.intercept + res_2000.slope * x_prediction_2000

    plt.plot(x_prediction_2000, y_prediction_2000, color='green', linewidth=3)
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    plt.show()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()