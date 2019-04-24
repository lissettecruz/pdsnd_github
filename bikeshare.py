import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('Would you like to see data for Chicago, New York City, or Washington?\n').lower()
            if city in ['chicago', 'new york city', 'washington']:
                break
        except:
            print('That\'s not a valid input!')

    print ("Great! We will proceed with analysis of {}, if this is not desired city, restart the program \n".format(city.title()))

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Choose a month (All, January, February, March, April, May, June):\n').lower()
            if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
                break
        except:
            print('That\'s not a valid input!')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Choose a day of the week (All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday):\n').lower()
            if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                break
        except:
            print('That\'s not a valid input')

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month:\n', popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("Most Common Day of the Week:\n", popular_day)

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:\n', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:\n', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:\n', popular_end_station)

    # display most frequent combination of start station and end station trip
    df['start_end_station'] = df['Start Station'] + 'to' + df['End Station']
    popular_start_end_station = df['start_end_station'].mode()[0]
    print('Most Frequent Combination of Start and End Station Trip:\n', popular_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Type Counts: \n {}'.format(user_types))

    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('Genter Counts: \n {}'.format(gender))
    except:
        pass

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_yr = df['Birth Year'].min()
        print('Earliest year of birth: {}'.format(earliest_birth_yr))
        recent_birth_yr = df['Birth Year'].max()
        print('Most recent year of birth: {}'.format(recent_birth_yr))
        common_birth_yr = df['Birth Year'].mode()[0]
        print('Most common year of birth: {}'.format(common_birth_yr))
    except:
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
