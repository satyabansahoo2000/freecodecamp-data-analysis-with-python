import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.plot(x,y,'.')

    # Create first line of best fit    
    slope, intercept, r_value, p_value, std_err = linregress(x,y)
    predict_dates = np.arange(1880,2050,1)
    model = np.polyfit(x, y, 1)
    predicted = np.polyval(model, predict_dates)
    plt.plot(x, y,'.', label='original data')
    plt.plot(predict_dates, predicted, label='fitted line')

    # Create second line of best fit
    x1 = df['Year'][df['Year']>=2000]
    y1= df['CSIRO Adjusted Sea Level'][df['Year']>=2000]
    slope, intercept, r_value, p_value, std_err = linregress(x1,y1)
    predict_dates = np.arange(2000,2050,1)
    model1 = np.polyfit(x1, y1, 1)
    predicted = np.polyval(model1, predict_dates)
    plt.plot(x, y,'.', label='original data')
    plt.plot(predict_dates, predicted, label='fitted line')


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()