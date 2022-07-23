
HISTORY_FILE = 'history.log'

with open(HISTORY_FILE, 'r') as file:
    for line in file:
        line_list = line.split(',')
        print(line_list)
        datetime_stamp = line_list[0]
        print(f"Datetime is: {datetime_stamp}")
        datetime_stamp = datetime_stamp.split('.')[0]
        navigator = line_list[1]
        navigator = navigator.split(':')
        navigator = navigator[1]
        print(f"Navigator is {navigator}")




