# DieRollSim.py updated as script
"""Dynamically graphing frequencies of die rolls not using numpy."""
import matplotlib.pyplot as plt
import random
import seaborn as sns

# set number of rolls in simulation
number_of_rolls = 1000000

# generate patches (a list indicating each die face), and the results of
# the number of rolls in simulation

frequencies = [0] * 11  # eleven-element list of two die frequencies
for i in range(number_of_rolls):
    frequencies[random.randrange(0, 11) - 1] += 1
values = [x for x in range(2, 13)]  # of your could also use list(range(1, 7))

# create plot figure
sns.set_style('whitegrid')  # white background with gray grid lines
figure = plt.figure('Rolling two Six-Sided Die')  # Figure to hold bar plot

# set axes
axes = sns.barplot(x=values, y=frequencies, palette='bright')  # new bars
axes.set_title(f'Die Frequencies for {number_of_rolls:,} Rolls')
axes.set(xlabel='Die Value', ylabel='Frequency')
axes.set_ylim(top=max(frequencies) * 1.10)  # scale y-axis by 10% to leave room at top of bars

# display frequency & percentage above each patch (bar)
for bar, frequency in zip(axes.patches, frequencies):  # see page 186 for more on zip
    text_x = bar.get_x() + bar.get_width() / 2.0  # center the text above bar
    text_y = bar.get_height()  # place text just above bar
    text = f'{frequency:,}\n{frequency / sum(frequencies):.2%}'  # we'll cover string formatting in ch08
    axes.text(text_x, text_y, text, ha='center',
              va='bottom')  # see here https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html

plt.show()  # display window
