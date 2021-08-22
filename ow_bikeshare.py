import time
import pandas as pd
import numpy as np
CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
#Use of an empty city variable to store city choice from user

    city = ''
    # while loop for correct user input gets otherwise repeat
    while city not in CITY_DATA.keys():
        print("\n Select choose your city:")
        print("\n1. Chicago 2. New York City 3. Washington")
        print("\nAccepted input:\nFull name of city; not case sensitive (e.g. chicago or CHICAGO).\nFull name in title case (e.g. Chicago).")
        #Taking user input and converting into lower to standardize them
        #You will find this happening at every stage of input throughout this
        city = input().lower()
        if city not in CITY_DATA.keys():
            print("\nPlease check your input.")
            print("\nRestarting...")
    print(f"\nYou have chosen {city.title()} as your city.")

# Creating dictionary to store potential months plus a select 'all' option
    SELECT_MONTH = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in SELECT_MONTH.keys():
        print ("\n Enter a month, between January and June, that you would like to see:")
        print ("\nAccepted input:\nFull month name; not case sensitive")
        print("\n(You may also opt to view data for all months, please type 'all' or 'All' or 'ALL' for that.)")
        month = input().lower()

    if month not in SELECT_MONTH.keys():
           print ("Invalid input. Try again in the correct format")
           print ("Restarting.....")
           print (f"\nYou have selected {month.title()}.")
#Creating list to store potential days plus a select 'all' option
    SELECT_DAY = ['all','monday','tuesday','wednesday','thursday','friday']
    day = ''
    while day not in SELECT_DAY:
        print("\n Enter a day which you would like to view:")
        print("\nAccepted input:\nDay name; not case sensitive (e.g. monday or MONDAY).\nDay name in title case (e.g. Monday).")
        print("\n(You may also opt to view data for all days, please type 'all' or 'All' or 'ALL' for that.)")
        day = input().lower()
        if day not in SELECT_DAY:
         print("\nPlease check your input.")
         print("\nRestarting...")
    print("You have chosen {day.title()} as your day.")
    print(f"\nYou have chosen to view data for city: {city.upper()}, month/s: {month.upper()} and day/s: {day.upper()}.")
    print('-'*80)
    return city, month, day
    print('-'*40)
    return city, month, day
def load_data(city, month, day):


    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print("Loading data")
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # pull month & day from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    # filter by month
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month)+1
        df = df[df['day'] == day.title()]

    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
   #displays stats on the most frequent travel times
    print ("Calculating The Most Frequent Travel Times")
    start_time = time.time()
    #Use mode to find the most popular month
    mode_month = df['month'].mode()[0]
    print(f"Most popular month : {mode_month} ")
    # Use mode to find the most popular day
    mode_day = df['day'].mode()[0]
    print(f"Most popular day : {mode_day} ")
    #Extract hour from Start Time Column to create hour column
    df['hour']=df['Start Time'].dt.hour
    #Use mode to find the most popular hour
    mode_hour = df['hour'].mode()[0]
    print(f"Most popular hour : {mode_hour} ")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    mode_start_station =df['Start Station'].mode()[0]
    print(f"The most common start station:{mode_start_station}")

    mode_end_station = df['End Station'].mode()[0]
    print(f"The most common end station:{mode_end_station}")
    df['mode_route'] = df['Start Station']+ " " + df['End Station']
    print("The most common route is : {}".format(df['mode_route'].mode().values[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    #Uses sum to caulcate trip duration and format into hour and minutes
    sum_duration = df['Trip Duration'].sum()
    hour, minute = divmod(sum_duration,60)
    print(f"Total trip duration is {hour} hours and {minute} minutes")
    #Uses mean to calculate average duration and format into minutes and hours
    mean_duration = round(df['Trip Duration'].mean())
    mins, sec = divmod(mean_duration,60)
    print(f"\nThe mean trip duration is {mins} minutes and {sec} seconds")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    #Displays users by their type
    rider_type = df['User Type'].value_counts()
    print (f"\nDifferent rider types are displayed below:\n\n{rider_type}")
    #Display counts of gender
    try:
        count_gender = df['Gender'].value_counts()
        print(f"\nThe types of users by gender are displayed below:\n\n{count_gender}")

    except : print("There is no gender data to display")
    #Displays summary statistics of ages
    try:
        minimum_by = int(df['Birth Year'].min())
        maximum_by = int(df['Birth Year'].max())
        mode_by = int(df['Birth Year'].mode()[0])
        print (f"\nThe oldest birth year is :{minimum_by}\n\nThe youngest birth year is :{maximum_by}\n\nThe most frequently occuring age is : {mode_by}")
    except:
        print("There are not birth year details in file")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    # displays raw data on user request

    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\Do you want to display another 5 rows of data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])


def main():
    while True:

        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        while True:
            view_raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":


  main()