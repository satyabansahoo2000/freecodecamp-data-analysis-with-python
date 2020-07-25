import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True,index_col='date')

# Clean data
df = df.drop(df.value[:int(round(df.value.count()*0.025))].index)
df = df.drop(df.value[-int(round(df.value.count()*0.025)):].index)

def draw_line_plot():

  #Draw line plot
  fig,ax = plt.subplots(figsize=(12,9))
  ax.plot(color='red')

  #save image
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df.reset_index(inplace=True)
    df_bar = df.groupby([df['date'].dt.year.rename('Years'),
               df['date'].dt.month.rename('Months')]).agg('mean')['value'].unstack()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12,8))
    df_bar.plot(kind='bar', ax=ax)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2,figsize=(20,5))

    plt.ylim(10000,180000)
    plt.title("Year-Wise Box Plot (Trend)")
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.tight_layout()
    sns.boxplot(x='year',y='value', data=df_box, ax=ax[0])
    
    plt.ylim(10000,180000)
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.tight_layout()
    plt.title("Month-Year Box Plot (Seasonality)")
    sns.boxplot(x='month',y='value', data=df_box, ax=ax[1])
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig