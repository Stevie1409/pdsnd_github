# Explore US bikeshare data 

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

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = 'city'
    while city not in CITY_DATA:
        city = str(input('Enter name of the city to filter by: ')).lower()
        if city not in CITY_DATA:
            print('Sorry, but it seems like the given city is not in the list or there was a spelling error.')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = 'month'
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while month not in months:
        month = str(input('Enter name of the month to filter by, or "all" to apply no month filter: ')).lower()
        if month not in months:
            print('Sorry, but it seems like the given month is not in the list or there was a spelling error.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = 'day'
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while day not in days:
        day = str(input('Enter name of the weekday to filter by, or "all" to apply no weekday filter: ')).lower()
        if day not in days:
            print('Sorry, but it seems like the given month is not in the list or there was a spelling error.')

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

    # TO DO: display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    most_common_month = months[df['month'].mode()[0]-1]
    print('{} is the most common month.'.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].value_counts().idxmax()
    print('{} is the most common day of week.'.format(most_common_day))

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['start_hour'].value_counts().idxmax()
    print('{} is the most common start hour.'.format(most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print('{} is the most common Start Station.'.format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print('{} is the most common End Station.'.format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    most_common_combination = df['combination'].value_counts().idxmax()
    print('{} is the most common start and end station trip.'.format(most_common_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = int(df['Trip Duration'].sum())
    print('The total travel time is {} seconds.'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = int(df['Trip Duration'].mean())
    print('The mean travel time is {} seconds.'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print(user_type_counts)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
    else:
        print('Unfortunately the used .csv-file does not include Gender data.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = str(df['Birth Year'].min())[0:4]
        recent = str(df['Birth Year'].max())[0:4]
        common = str(df['Birth Year'].value_counts().idxmax())[0:4]
        print('{} is the earliest, {} the most recent and {} the most common year of birth'.format(earliest, recent, common))
    else:
        print('Unfortunately the used .csv-file does not include Birth Year data.')

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

        row = 0
        while True:
            viewData = input('\nWould you like to see the raw data? Enter yes or no.\n').lower()
            if viewData == 'yes':
                print(df.iloc[row:row+5,:])
                row += 5
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
