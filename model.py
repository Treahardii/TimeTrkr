# Import the necessary modules
from datetime import datetime
import requests

# Get the form data from the request
client = requests.form['client']
project = requests.form['project']
date = requests.form['date']
time_in = requests.form['time-in']
time_out = requests.form['time-out']

# Parse the date string into a datetime object
date = datetime.strptime(date, '%Y-%m-%d')

# Get the day of the week from the date
day = date.strftime('%A')

# Calculate the time worked
time_worked = datetime.strptime(time_out, '%H:%M') - datetime.strptime(time_in, '%H:%M')

# Open the HTML file for writing
with open('table.html', 'w') as html_file:
    # Write the HTML table header
    html_file.write('<table>\n')
    html_file.write('  <tr>\n')
    html_file.write('    <th>Project</th>\n')
    html_file.write('    <th>Time worked</th>\n')
    html_file.write('  </tr>\n')

    # Write the data as a table row
    html_file.write('  <tr>\n')
    html_file.write(f'    <td>{project}</td>\n')
    html_file.write(f'    <td>{time_worked}</td>\n')
    html_file.write('  </tr>\n')

    # Write the HTML table footer
    html_file.write('</table>\n')
