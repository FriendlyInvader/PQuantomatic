"""Plotting utilities for PQuantomatic library."""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def setup_matplotlib_backend():
    """Set up matplotlib backend for non-interactive environments.
    
    This function should be called before any plotting operations
    to avoid the 'FigureCanvasAgg is non-interactive' warning.
    """
    matplotlib.use('Agg')


def create_sample_plot():
    """Create a sample plot demonstrating proper matplotlib usage.
    
    Returns:
        str: Path to the saved plot file.
    """
    setup_matplotlib_backend()
    
    # Create sample data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='sin(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Sample Plot - Sine Function')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save the plot instead of showing it
    plot_path = 'sample_plot.png'
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    plt.close()  # Important: close the figure to free memory
    
    return plot_path


def create_quantitative_plot(data, title="Quantitative Analysis", save_path=None):
    """Create a plot for quantitative analysis.
    
    Args:
        data: Array-like data to plot
        title: Title for the plot
        save_path: Path to save the plot (optional)
        
    Returns:
        str: Path to the saved plot file.
    """
    setup_matplotlib_backend()
    
    plt.figure(figsize=(12, 8))
    plt.plot(data, linewidth=2)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title(title)
    plt.grid(True, alpha=0.3)
    
    if save_path is None:
        save_path = f"{title.lower().replace(' ', '_')}.png"
    
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    return save_path


# Example usage
if __name__ == "__main__":
    # Create a sample plot
    plot_file = create_sample_plot()
    print(f"Plot saved as: {plot_file}")
    
    # Create a quantitative analysis plot
    sample_data = np.random.randn(100).cumsum()  # Random walk
    quant_plot = create_quantitative_plot(sample_data, "Random Walk Analysis")
    print(f"Quantitative plot saved as: {quant_plot}")

