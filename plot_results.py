import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
    # todo: load the "results.csv" file from the mia-results directory
    # todo: read the data into a list
    # todo: plot the Dice coefficients per label (i.e. white matter, gray matter, hippocampus, amygdala, thalamus)
    #  in a boxplot
    df = pd.read_csv('mia-results/results.csv')
    wm = df['white matter'].tolist()
    gm = df['gray matter'].tolist()
    hc = df['hippocampus'].tolist()
    am = df['amygdala'].tolist()
    th = df['thalamus'].tolist()

    fig = plt.figure(figsize=(10,7))
    plt.boxplot(wm)
    plt.boxplot(gm)
    plt.boxplot(hc)
    plt.boxplot(am)
    plt.boxplot(th)

    plt.show()

    # alternative: instead of manually loading/reading the csv file you could also use the pandas package
    # but you will need to install it first ('pip install pandas') and import it to this file ('import pandas as pd')
    pass  # pass is just a placeholder if there is no other code


if __name__ == '__main__':
    main()
