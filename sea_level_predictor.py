import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c=df['Year'], cmap='viridis', label='Original Data')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = list(range(1880, 2051))
    y = [intercept + slope*year for year in x]
    plt.plot(x, y, 'r', label='Fit: 1880-2050')

    # Create second line of best fit (from year 2000)
    df_2000 = df[df['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x = list(range(2000, 2051))
    y = [intercept + slope*year for year in x]
    plt.plot(x, y, 'g', label='Fit: 2000-2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return the current axis for further inspection
    plt.savefig('sea_level_plot.png')
    plt.show()

draw_plot()
