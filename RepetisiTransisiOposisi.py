import matplotlib.pyplot as plt
import numpy as np

def create_repetition_line(ax):
    ax.set_title('Repetisi pada Garis')
    ax.set_aspect('equal')
    for i in range(10):
        linewidth = 1 if i % 2 == 0 else 3
        ax.plot([i, i], [0, 1], color='black', linewidth=linewidth)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1)
    ax.axis('off')

def create_transition_line(ax):
    ax.set_title('Transisi pada Garis')
    ax.set_aspect('equal')
    for i in range(10):
        linewidth = 1 + i * 0.3
        ax.plot([0, 10], [i/10, i/10], color='black', linewidth=linewidth)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1)
    ax.axis('off')

def create_opposition_line(ax):
    ax.set_title('Oposisi pada Garis')
    ax.set_aspect('equal')
    ax.plot([0, 10], [0, 1], color='black', linewidth=2)
    ax.plot([0, 10], [1, 0], color='red', linewidth=5)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1)
    ax.axis('off')

def create_repetition_shape(ax):
    ax.set_title('Repetisi pada Bidang')
    ax.set_aspect('equal')
    for i in range(5):
        size = 0.1 if i % 2 == 0 else 0.3
        rect = plt.Rectangle((i*0.4, 0.4), size, size, color='blue')
        ax.add_patch(rect)
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 1)
    ax.axis('off')

def create_transition_shape(ax):
    ax.set_title('Transisi pada Bidang')
    ax.set_aspect('equal')
    for i in range(5):
        size = 0.1 + i * 0.05
        rect = plt.Rectangle((i*0.4, 0.4), size, size, color='green')
        ax.add_patch(rect)
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 1)
    ax.axis('off')

def create_opposition_shape(ax):
    ax.set_title('Oposisi pada Bidang')
    ax.set_aspect('equal')
    rect1 = plt.Rectangle((0.2, 0.4), 0.2, 0.2, color='blue')
    rect2 = plt.Rectangle((1.0, 0.4), 0.4, 0.4, color='red')
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 1)
    ax.axis('off')

def create_repetition_mass(ax):
    ax.set_title('Repetisi pada Gempal')
    ax.set_aspect('equal')
    for i in range(5):
        size = 0.05 if i % 2 == 0 else 0.15
        circle = plt.Circle((i*0.4, 0.5), size, color='purple')
        ax.add_patch(circle)
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 1)
    ax.axis('off')

def create_transition_mass(ax):
    ax.set_title('Transisi pada Gempal')
    ax.set_aspect('equal')
    for i in range(5):
        size = 0.05 + i * 0.03
        circle = plt.Circle((i*0.4, 0.5), size, color='orange')
        ax.add_patch(circle)
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 1)
    ax.axis('off')

def create_opposition_mass(ax):
    ax.set_title('Oposisi pada Gempal')
    ax.set_aspect('equal')
    circle1 = plt.Circle((0.5, 0.5), 0.1, color='purple')
    circle2 = plt.Circle((1.5, 0.5), 0.3, color='yellow')
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 1)
    ax.axis('off')

# Membuat figure dan subplot untuk semua prinsip desain
fig, axs = plt.subplots(3, 3, figsize=(15, 15))

create_repetition_line(axs[0, 0])
create_transition_line(axs[0, 1])
create_opposition_line(axs[0, 2])

create_repetition_shape(axs[1, 0])
create_transition_shape(axs[1, 1])
create_opposition_shape(axs[1, 2])

create_repetition_mass(axs[2, 0])
create_transition_mass(axs[2, 1])
create_opposition_mass(axs[2, 2])

plt.tight_layout(pad=5.0)
plt.savefig('design_principles_repetition_transition_opposition.png')
plt.show()
