import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']

months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city. HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Enter name of city, Chicago, New York City or Washington to analyze: \n> ').lower()
        if city in cities:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter month to filter by, or 'all' to apply no month filter:  \n> ")
        if month in months:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter the day of the week to filter by, or 'all' to apply no day filter: \n> ")
        if day in days:
            break

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

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable (used the mentor to figure out how to do this)
    if month != "all":
     
    # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
    # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != "all":

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    """
    (used StackOverflow to figure out how to do this)
    """
    print ('\nSELECTIONS:\nCity: {} \nMonth: {} \nDay: {}'.format(city, month, day))
    return df

def time_stats(df):
    """Displays statistics on the most frequent months, days and hour of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print("The most common month is: \n>", common_month)
    print("The most common day of the week is: \n>", common_day_of_week)
    print("The most common hour is: \n>", common_hour)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip (used StackOverflow to figure out how to do this)
    frequent_station = df.groupby(['Start Station','End Station']).size().nlargest(1)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print("The most common start station is: \n>", common_start_station)
    print("The most common end station is: \n>", common_end_station)
    print("The most frequent combination is: \n>", frequent_station)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    average = df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print("Total travel time is: \n>", total)
    print("Average travel time is: \n>", average)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()

    # TO DO: Display earliest, most recent, and most common year of birth
    oldest = df.min(axis=0)['Birth Year']
    youngest = df.max(axis=0)['Birth Year']
    common_birth_year = df['Birth Year'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print(user_types)
    print(gender)
    print("Earliest birth year is: \n>", oldest)
    print("Most recent birth year is: \n>", youngest)
    print("Most common birth year is: \n>", common_birth_year)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

    """
    Asks user if they would like to see lines of raw data to analyze.

    Returns:
        5 lines of raw data for each yes response.
        Loop breaks when no is entered.
    """         
        A=0
        B=5
        while True:
            a = input(('\nWould you like to see rows {} to {} of raw data? Please enter yes/no to continue. \n').format(A,B))
            if a=="yes":
                print (df.iloc[A:B])
                A=A+5
                B=B+5
                continue
            elif a=="no":
                break
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()