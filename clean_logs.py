def celsius_converter(f_temp):
    '''
    Convert a Fahrenheit temperature to Celsius.

    Accepts a Fahrenheit temperature as a string or float,
    converts it to Celsius, and rounds the result to two decimal places.
    Returns an error message if the input has an invalid type.
    '''
    if isinstance(f_temp, (str, float)):
        return round((float(f_temp) - 32) / 1.8, 2)
    else:
        return 'the variable is invalid type'


def parse_and_clean(line):
    '''
    Parse and clean a single sensor data line.

    Splits the string by the "|" delimiter and removes extra whitespace
    from each field. Returns None if the line contains missing or invalid
    data, or if the sensor status is not "ACTIVE".
    Otherwise, returns the cleaned data as a list.
    '''
    if isinstance(line, str):
        line = [i.strip() for i in line.split('|')]
        if len(line) != 5:
            return None

        if 'ERROR' in line or 'N/A' in line:
            return None

        if line[-1] != 'ACTIVE':
            return None
        return line
    else:
        return None


if __name__ == '__main__':
    with open('environmental_raw.txt', 'rt') as file:
        with open ('environmental_cleaned.csv', 'wt') as output:
            next(file)
            output.write('Timestamp,StationID,Temp(C),Humidity(%),Sensor_Status\n')
            corrupted_lines = 0
            for line in file:
                cleaned_line = parse_and_clean(line)
                if cleaned_line is None:
                    corrupted_lines += 1
                else:
                    cleaned_line[2] = str(celsius_converter(cleaned_line[2]))
                    new_line = ','.join(cleaned_line)
                    output.write(f'{new_line}\n')
            print(f'Cleaned data saved. There were {corrupted_lines} corrupted logs in the file')


