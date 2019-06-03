import swagger_client
import pandas as pd
import matplotlib.pyplot as plt

# Configure authorization to strava API
api_instance = swagger_client.SegmentsApi()
access_token = '2f33100d5ef7f5ac979967256b281e574cde7a88' #this needs to be updated
api_instance.api_client.configuration.access_token = access_token

#---loads leaderboard into pandas dataframe
def get_segment_leaderboard(segment_id, lb_length):
    entries = []
    
    for i in range(1, round(1+lb_length/200)):
        api_response = api_instance.get_leaderboard_by_segment_id(
                id=olh_id,
                per_page = 200,
                page = i)
        entries.extend(api_response.entries)
      
    df = pd.DataFrame.from_dict(entries[i].to_dict() for i in range(len(entries)))
    
    df = df.drop_duplicates().sort_values(by='start_date_local')
    
    df['year'] = df.start_date_local.dt.year
    df['month'] = df.start_date_local.dt.month
    df['dow'] = df.start_date_local.dt.day_name()
    df['hour'] = df.start_date_local.dt.hour
    df.elapsed_time = df.elapsed_time/60
    
    return df

#used to create plots of counts (bar chart) and time (line graph)
def double_plot(df, x, y_bar, y_line,title):    
    fig, ax1 = plt.subplots()
    
    color = 'tab:green'
    ax1.set_title(title)
    ax1.set_xlabel(x)
    ax1.set_ylabel('Count', color=color)
    ax1.bar(df[x], df[y_bar], color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx() 
    
    color = 'tab:blue'
    ax2.set_ylabel('Minutes', color=color)
    ax2.plot(df[x], df[y_line], color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    
    fig.tight_layout()
    plt.show()
    
    
#---get OLH data
olh_id = 8109834 #https://www.strava.com/segments/8109834
df = get_segment_leaderboard(olh_id, lb_length=24012)


#---plot 2019 times
df[df.year == 2019].plot(x='start_date_local', y='elapsed_time', kind='bar')

#---summarize by day of week and hour for 2019
x=(df[df.year >= 2019].groupby(['dow','hour'])
        .agg({'elapsed_time':['count','mean']})
        .reset_index())
x.columns = [''.join(x) for x in x.columns.ravel()]

for day in x.dow.unique():
    double_plot(x[x.dow == day], x='hour', 
                y_bar = 'elapsed_timecount', 
                y_line = 'elapsed_timemean',
                title = day)

 

#---average time by year
x2 = df.groupby('year').agg({'elapsed_time':['mean','count']}).reset_index()
x2.columns = [''.join(c) for c in x2.columns.ravel()]
double_plot(x2, x='year', 
            y_bar = 'elapsed_timecount', 
            y_line = 'elapsed_timemean',
            title = 'Tiem by Year')



#---average by name
df['first_name'] = df.athlete_name.str.split(' ').str[0]
dfx = (df[df.first_name.isin(['Jordan','Carlos','Holly','Tommy'])]
            .groupby('first_name')
            .agg({'elapsed_time':['count','mean']})
            .reset_index())
dfx.columns = ['name','count','time']

double_plot(dfx, x='name', y_bar = 'count', y_line = 'time', title = 'Time by Name')
