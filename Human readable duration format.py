# Your task in order to complete this Kata is to write a function which formats a duration,
# given as a number of seconds, in a human-friendly way.
#
# The function must accept a non-negative integer. If it is zero, it just returns "now".
# Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.
#
# It is much easier to understand with an example:
#   For seconds = 62, your function should return
#     "1 minute and 2 seconds"
#   For seconds = 3662, your function should return
#     "1 hour, 1 minute and 2 seconds"
# For the purpose of this Kata, a year is 365 days and a day is 24 hours.
#
# Note that spaces are important.
def f(seconds):
    if seconds > 1:
        return 's'
    else:
        return ''


def point(i, x, c):
    if i == 0:
        return ''
    elif (i == 1 and x[0] != 0):
        return ' and '
    elif i > 1:
        return ', '
    else:
        return ''


def format_duration(seconds):
    k_and = 0
    if seconds == 0:
        return 'now'
    x = [0, 0, 0, 0, 0]
    i = 0
    while seconds > 0 and i != 2:
        x[i] = seconds % 60
        seconds = seconds // 60
        i += 1
    x[2] = seconds % 24
    seconds = seconds // 24
    x[3] = seconds % 365
    x[4] = seconds // 365
    print(x)
    d = {
        0: 'second',
        1: 'minute',
        2: 'hour',
        3: 'day',
        4: 'year',
    }
    count = 0
    for i in range(len(x)):
        if x[i] > 0:
            count += 1
    result = ''
    for i in range(len(x)):
        if count == 1 and x[i] > 0:
            result = str(x[i]) + ' ' + d.get(i) + f(x[i])
            break
        elif x[i] > 0 and count > 1:
            result = str(x[i]) + ' ' + d.get(i) + f(x[i]) + f"{point(i, x, count)}" + result
    ecoma = 0
    for i in range(len(result)):
        if result[i] == ',':
            ecoma += 1

    if ecoma > 1 and ('and' not in result):
        t = 0
        index = 0
        for i in range(len(result)):
            if result[i] == ',' and t + 1 == ecoma:
                index = i
                print(index)
                break
            elif result[i] == ',' and t != ecoma:
                t += 1
        h = result[index:].replace(',', ' and', 1)
        result = result[:index] + h
    print(result)