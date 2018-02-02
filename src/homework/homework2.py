def get_time(hour, minutes, seconds, time_type, meridiem='AM'):
    '''
    Returns a time in 12 or 24 hour format

    :param hour: The hour of day-
                 when time_type 12 hr hour valid range 1 to 12 otherwise return 'Invalid hours(1-12)'****
                 when time_type 24 hr hour valid range 0 to 23 otherwise return 'Invalid hours(range 0-23)'****

    :param minutes: Minutes of an hour--minutes valid range 0 to 59 otherwise return 'Invalid minutes(range 0-59)'****
    :param seconds:  seconds of an hour--seconds valid range 0 to 59 otherwise 'Invalid seconds(range 0-59)'****
    :param time_type: Indicates the format of time to derive 12hr or 24hr****
                      Valid time_type values 12 or 24 otherwise return 'Invalid time_type(12 or 24 only)'
                      If time_type is 24 ignore meridiem value;

                      If time_type is 12hr time use meridiem parameter value(AM or PM)

    :param meridiem:  AM, PM

    :return: time in 12 or 24 hour format
      Example for 12 hour format 09:09:09 PM
      Example for 24 hour format 21:09:09
    ADD YOUR CODE AFTER THE THREE QUOTES BELOW (dont forget to include a return statement at the end
    '''
    #=============================================
    #Since minutes and seconds have to be in range 0-59 regardless of time type,
    #validate them first

    if minutes < 0 or minutes > 59:
        return 'Invalid minutes(range 0-59)'

    if seconds < 0 or seconds > 59:
        return 'Invalid seconds(range 0-59)'

    #now validate hours are in valid range for each time type
    #also let's validate that time type is 12 or 24; if not return error
    if time_type == 12:
        if hour < 1 or hour > 12:
            return 'Invalid hours(range 1-12)'
    elif time_type == 24:
        if hour < 0 or hour > 23:
            return 'Invalid hours(range 0-23)'
    else:#time type is not 12 or 24
        return 'Invalid time_type(12 or 24 only)'

    #we have good hour, minutes,and seconds prefix numbers less than 10 with a 0
    #this rule has to be applied regardless of time type
    if hour < 10:
        hour = '0' + str(hour)

    if minutes < 10:
        minutes = '0' + str(minutes)

    if seconds < 10:
        seconds = '0' + str(seconds)

    #now ready to create the time, assume time type is 24,
    #since hour, minutes, or seconds can be over 9 treat them as strings with str()
    time = str(hour) + ':' + str(minutes) + ':' + str(seconds)

    if time_type == 12:#if time type 12 append AM or PM
        time = time + ' ' + meridiem

    return time

def time_from_utc(utc_offset, utc_zero_time):
    '''
    Write code to calculate a time zone's time after applying utc_offset
    :param utc_offset:
    :param utc_zero_time:
    :return:
    DON NOT CHANGE ANYTHING IN THIS FUNCTION
    '''

    return (utc_zero_time + utc_offset) % 24
