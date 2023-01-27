from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline
from statistics import mean

def Average(results):
    myMean = mean(results)
    wholeNumMean = int(myMean)
    return wholeNumMean

# Create a D6 and a D10
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results into a list
results = []

for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='Results of rolling a D6 and D10 50,000 times',
    xaxis=x_axis_config, yaxis=y_axis_config)

# Need to downgrade to plotly 5.11.0 for this to work, on 5.12.0 unicode bug
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')