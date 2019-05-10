from matplotlib import style
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def makeGraph(count_list, score_list):
    style.use('classic')

    ax1.plot(count_list, score_list)

    plt.title('Prestatie hillclimber')
    plt.xlabel('Counter')
    plt.ylabel('Score')
    plt.show()
