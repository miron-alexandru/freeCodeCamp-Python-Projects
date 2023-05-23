import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    sns.scatterplot(x=df['Year'], y=df['CSIRO Adjusted Sea Level']);
    df_filtered = df[df['Year'] >= 2000]

    # Perform linear regression on the original dataset
    slope_original, intercept_original, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
      
    # Perform linear regression on the filtered dataset
    slope_filtered, intercept_filtered, _, _, _ = linregress(df_filtered['Year'], df_filtered['CSIRO Adjusted Sea Level'])
      
    # Create the line of best fit for the original dataset
    years_original = range(1880, 2051)  # Years from 1880 to 2050
    line_original = slope_original * years_original + intercept_original
      
    # Create the line of best fit for the filtered dataset
    years_filtered = range(2000, 2051)  # Years from 2000 to 2050
    line_filtered = slope_filtered * years_filtered + intercept_filtered
      
    # Plotting the scatter plot and lines of best fit
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', label='Sea Level')
    ax.plot(years_original, line_original, color='r', label='Original Best Fit Line')
    ax.plot(years_filtered, line_filtered, color='g', label='Filtered Best Fit Line')
      
    # Customize the chart
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
      
    # Add prediction for 2050 based on filtered dataset
    predicted_2050_filtered = slope_filtered * 2050 + intercept_filtered
    ax.text(2050, predicted_2050_filtered, f'2050(filtered): {predicted_2050_filtered:.2f} inches')
      
    # Add prediction for 2050 based on original dataset
    predicted_2050_original = slope_original * 2050 + intercept_original
    ax.text(2050, predicted_2050_original, f'2050 (original): {predicted_2050_original:.2f} inches')
      
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
  
  