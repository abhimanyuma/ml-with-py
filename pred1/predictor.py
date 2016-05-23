import scipy as sp
import matplotlib.pyplot as plt

def formatdata(data):
    x = data[:,0]
    y = data[:,1]
    x = x[~sp.isnan(y)]
    y = y[~sp.isnan(y)]
    return x,y

def plot(xdata, ydata):
    plt.scatter(xdata, ydata)
    plt.title("Web Traffic")
    plt.xlabel("Time")
    plt.ylabel("Hits/Hour")
    plt.xticks([w * 7 * 24 for w in range(10)], ['week %i'%w for w in range(10)])
    plt.autoscale(tight = True)
    plt.grid()
    plt.show()

def getdata(filename, delimiter = '\t'):
    return sp.genfromtxt(filename, delimiter = delimiter)

def main():
    data = getdata("web_traffic.tsv")
    x, y = formatdata(data)
    plot(x, y)

main()
