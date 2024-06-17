import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def create_shape_transition(ax):
    ax.set_title('Keselarasan Unsur Raut')
    ax.set_aspect('equal')

    # Menggambar transisi dari kotak ke lingkaran
    for i in range(5):
        size = 0.3 - i * 0.05
        rect = patches.Rectangle((i * 0.4, 0.6), size, size, color='blue')
        circle = patches.Circle((i * 0.4 + 0.15, 0.3), size / 2, color='blue')
        ax.add_patch(rect)
        ax.add_patch(circle)

    # Menggambar transisi dari kotak ke segitiga
    for i in range(5):
        size = 0.3 - i * 0.05
        rect = patches.Rectangle((i * 0.4 + 2.0, 0.6), size, size, color='red')
        triangle = patches.RegularPolygon((i * 0.4 + 2.15, 0.3), numVertices=3, radius=size / 2, orientation=np.pi / 2, edgecolor='red', facecolor='red')
        ax.add_patch(rect)
        ax.add_patch(triangle)

    ax.set_xlim(0, 4)
    ax.set_ylim(0, 1)
    ax.axis('off')

def create_color_transition(ax):
    ax.set_title('Keselarasan Unsur Warna')
    ax.set_aspect('equal')

    # Menggambar transisi warna dari merah ke hijau
    colors = ['red', 'orange', 'yellow', 'green', 'blue']
    for i, color in enumerate(colors):
        rect = patches.Rectangle((i * 0.4, 0.6), 0.3, 0.3, color=color)
        ax.add_patch(rect)

    # Menggambar transisi warna dari merah ke hijau (dengan lingkaran)
    for i, color in enumerate(colors):
        circle = patches.Circle((i * 0.4 + 2.0, 0.3), 0.15, color=color)
        ax.add_patch(circle)

    ax.set_xlim(0, 4)
    ax.set_ylim(0, 1)
    ax.axis('off')

# Membuat figure dan subplot untuk keselarasan unsur raut dan warna
fig, axs = plt.subplots(1, 2, figsize=(15, 5))

create_shape_transition(axs[0])
create_color_transition(axs[1])

plt.tight_layout(pad=5.0)
plt.savefig('harmony_elements_transition.png')
plt.show()
