import matplotlib.pyplot as plt
import numpy as np

def visualize_skills(skills, skill_levels):
    # Set up the figure and axis
    fig, ax = plt.subplots()

    # Create a list of colors
    colors = ['blue', 'green', 'red', 'cyan', 'magenta']

    # Create a bar chart with different colors for each bar
    y_pos = np.arange(len(skills))
    ax.barh(y_pos, skill_levels, align='center', color=colors)

    # Customize the appearance
    ax.set_yticks(y_pos)
    ax.set_yticklabels(skills)
    ax.set_xlabel('Skill Level')
    ax.set_title('My Skills')

    # Display the chart
    plt.show()

skills = ['Python', 'SQL', 'Excel', 'Power BI', 'JS']
skill_levels = [9, 8, 7, 8, 6]

visualize_skills(skills, skill_levels)
