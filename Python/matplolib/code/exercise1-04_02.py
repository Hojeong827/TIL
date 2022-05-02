import matplotlib.pyplot as plt

xticks = [i for i in range(7)]
xtick_labels = [" ", 
                "<vehichle, move along, street>",
                "<person, move along, sidewalk>",
                "<pet, move along, side walk>",
                "<person, stay, lawn>",
                "<person, move away (home), driveway>",
                " "]

yticks = [i/10 for i in range(11)]

fig, ax = plt.subplots(figsize=(20, 10))
ax.set_xticks(xticks)
ax.set_xticklabels(xtick_labels, ha='right')

ax.set_yticks(yticks)

ax.tick_params(axis='x', rotation=20, labelsize=15, colors='gray')
ax.tick_params(axis='y', labelsize=15, colors='gray')
fig.subplots_adjust(bottom=0.2, top=0.95, left=0.1, right=0.9)

plt.show()