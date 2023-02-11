import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


month_list = ['january','february','march','april','may','june','all']
weekday_list = ['sunday','monday','tuseday','wednesday','thursday','friday','saturday','all']


def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    #get user input for city, and check user input validity
    city = check_input('chicago, new york or washington?', 1)
    #get user input for month, and check user input validity
    month = check_input('Enter month:', 2)
    #get user input for day, and check user input validity
    day = check_input('Enter day:', 3)

    print('-'*40)
    return city, month, day

def check_input(user_input,input_type):
    while True:
        input_read = input(user_input).lower()
        try:
            if input_read in ['chicago','new york','washington' ] and input_type==1:
                break
            elif input_read in month_list and input_type==2:
                break
            elif input_read in weekday_list and input_type==3:
                break
            else:

                if input_type==1:
                    print('This city dose not exist! please choose chicago, new york or washington')
                if input_type==2:
                    print('wrong month! please try again')
                if input_type==3:
                    print('wrong day! please try agin')
        except ValueError:
            print('Sorry Error Input')
    return input_read


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #extract month, day and hour from start time to creat new coluns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month!= 'all':

        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':

        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):

    print('\nCalculating The Most Frequent Times of travel..\n')
    start_time = time.time()
    # TO DO: display the most common month
    most_commen_month = df['month'].mode()[0]
    print ('Most Commen Month is:' , most_commen_month)
    # TO DO: display the most common day of week
    most_commen_day = df['day_of_week'].mode()[0]
    print ('Most Commen Day is:' , most_commen_day)
    # TO DO: display the most common start hour
    most_commen_hour = df['hour'].mode()[0]
    print ('Most Commen Start Hour is:' , most_commen_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    most_commen_start_station = df['Start Station'].mode()[0]
    print('Most Commen Start Station is:',most_commen_start_station)
    # TO DO: display most commonly used end station
    most_comment_end_station = df['End Station'].mode()[0]
    print('Most Commen End Station is:',most_comment_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    group_filed = df.groupby(['Start Station','End Station'])
    popular_combination_station = group_filed.size().sort_values(ascending=False).head(1)
    print('Most frequent comination of Start Station and End Station trip:\n', popular_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
     # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time is:', total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time is:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    print('User Type in Data are:', df['User Type'].value_counts())
     # TO DO: Display counts of gender
    if city != 'washington':
        print('Count of Gender:' , df['Gender'].value_counts())
        # TO DO: Display earliest, most recent, and most common year of birth
        most_commen_year = df['Birth Year'].mode()[0]
        print('Most Commen Year is:',most_commen_year)

        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year is:', most_recent_year)

        earlist_year = df['Birth Year'].min()
        print('Earlist year is:',earlist_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#view raw data to user
def show_row_data(df):
    row=0
    while True:
        view_raw_data = input('would you like to see the raw data? Enter "Yes" or "No"\n').lower()

        if viwe_raw_data == 'Yes':
            print(df.iloc[row : row + 6])
            row+=6
        elif view_raw_data == 'No':
            break
        else:
            print('Sorry! Wrong Input , Pleas Try Agin.')
def bye():
    print("bye!")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_row_data(df)

        restart = input('\nwould you like to restart? Enter "Yes" or "No"\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	 main()
