"""
Shared matplotlib style for all plotting scripts.
Import this at the top of every plot script:
    import sys; sys.path.insert(0, '../../..'); from SHARED_PLOT_STYLE import setup_style
"""
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import numpy as np

def setup_style():
    """Set publication-quality matplotlib defaults."""
    plt.rcParams.update({
        'figure.figsize': (8, 5),
        'figure.dpi': 150,
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
        'font.size': 12,
        'font.family': 'serif',
        'font.serif': ['Computer Modern Roman', 'DejaVu Serif'],
        'text.usetex': False,  # Set True if LaTeX is available
        'axes.labelsize': 14,
        'axes.titlesize': 14,
        'legend.fontsize': 11,
        'xtick.labelsize': 11,
        'ytick.labelsize': 11,
        'lines.linewidth': 1.8,
        'axes.linewidth': 1.0,
        'axes.grid': True,
        'grid.alpha': 0.3,
        'legend.framealpha': 0.9,
        'legend.edgecolor': '0.8',
    })

# Physical constants (CGS)
c_cgs = 2.998e10       # cm/s
G_cgs = 6.674e-8       # cm^3/(g s^2)
M_sun = 1.989e33       # g
R_sun = 6.957e10       # cm
k_B = 1.381e-16        # erg/K
m_p = 1.673e-24        # g
hbar = 1.055e-27        # erg s
sigma_SB = 5.670e-5    # erg/(cm^2 s K^4)

# Dimensionless
pi = np.pi

# Color palette for consistent styling
COLORS = {
    'classical': '#2196F3',     # Blue
    'relativistic': '#F44336',  # Red
    'bdnk': '#4CAF50',         # Green
    'is': '#FF9800',           # Orange
    'data': '#9C27B0',         # Purple
    'neutron_star': '#E91E63', # Pink
    'accretion': '#00BCD4',    # Cyan
    'jet': '#FF5722',          # Deep Orange
    'qgp': '#795548',          # Brown
}

LINE_STYLES = ['-', '--', '-.', ':', (0, (3, 1, 1, 1))]
