import matplotlib.pyplot as plt
import seaborn as sns
from globals.functions import create_directory, join_directory_and_file



target_directory = "data/visualizations"


def generate_transfers_visualization(df, title, x_axis, y_axis_, hue=None):
    sns.set_theme(style='whitegrid', color_codes=True)
    sns_barplot = sns.barplot(data=df, x=x_axis, y=y_axis_, hue=hue, estimator=sum, errorbar=None)
    sns_barplot.set_title(title)
    create_directory(target_directory)
    png_file = join_directory_and_file(target_directory, f"{title}.png")
    plt.savefig(png_file)
    plt.show()
    plt.close()
