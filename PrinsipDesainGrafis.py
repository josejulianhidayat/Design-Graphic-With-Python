import matplotlib.pyplot as plt
import numpy as np

def create_proportion(ax):
    ax.set_title('Proporsi')
    ax.set_aspect('equal')

    # Menggambar beberapa kotak dengan ukuran yang berbeda
    for i in range(1, 6):
        rect = plt.Rectangle((i*0.2, i*0.2), i*0.2, i*0.2, color=f'C{i}')
        ax.add_patch(rect)

    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    ax.axis('off')

def create_emphasis(ax):
    ax.set_title('Penekanan')
    ax.set_aspect('equal')

    # Menggambar beberapa lingkaran dengan satu lingkaran yang lebih besar untuk penekanan
    for i in range(1, 6):
        circle = plt.Circle((i*0.2, 1), 0.1, color='gray')
        ax.add_patch(circle)
    emphasis_circle = plt.Circle((1, 1), 0.3, color='red')
    ax.add_patch(emphasis_circle)

    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    ax.axis('off')

def create_rhythm(ax):
    ax.set_title('Irama')
    ax.set_aspect('equal')

    # Menggambar pola berulang
    for i in range(10):
        ax.plot([i, i], [0, 1], color='black', linewidth=2)
        ax.plot([i+0.5, i+0.5], [0, 1], color='gray', linewidth=2, linestyle='--')

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1)
    ax.axis('off')

def create_simplicity(ax):
    ax.set_title('Kesederhanaan')
    ax.set_aspect('equal')

    # Menggambar kotak sederhana
    rect = plt.Rectangle((0.5, 0.5), 1, 1, color='blue')
    ax.add_patch(rect)

    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    ax.axis('off')

def create_clarity(ax):
    ax.set_title('Kejelasan')
    ax.set_aspect('equal')

    # Menggambar teks dengan latar belakang yang jelas
    ax.text(0.5, 0.5, 'Kejelasan', fontsize=24, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black'))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

# Membuat figure dan subplot untuk semua prinsip desain
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

create_proportion(axs[0, 0])
create_emphasis(axs[0, 1])
create_rhythm(axs[0, 2])
create_simplicity(axs[1, 0])
create_clarity(axs[1, 1])

# Menghapus subplot kosong yang tersisa
fig.delaxes(axs[1, 2])

plt.tight_layout(pad=5.0)
plt.savefig('design_principles.png')
plt.show()
