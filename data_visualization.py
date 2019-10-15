import matplotlib.pyplot as plt
import numpy as np

def plot_categorical_log(counts_per_feature, feature_name="feature"):
#     plt.figure()
    ax=plt.plot(np.arange(len(counts_per_feature)), counts_per_feature, 'xk')
    plt.gca().set_yscale('log')
    plt.title(feature_name + ' distribution')
    plt.ylabel('log10 counts per %s' % (feature_name))
    plt.grid('on')
    plt.show()