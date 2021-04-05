import matplotlib.pyplot as plt


def plot(s):
    plt.plot(s.unsigned(10000), color="black", marker='o', linestyle='dashed', linewidth=1,
             markerfacecolor='tab:green', markersize=6)
    plt.title(", ".join([str(i) for i in s.unsigned(10)])+"\n")
    plt.savefig('static/img/' + s.id + '.png', transparent=True)
    plt.clf()
