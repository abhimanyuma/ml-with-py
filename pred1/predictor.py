import scipy as sp
import matplotlib.pyplot as plt

def error(f, x, y):
    return sp.sum((f(x)-y)**2)

def formatdata(data):
    x = data[:,0]
    y = data[:,1]
    x = x[~sp.isnan(y)]
    y = y[~sp.isnan(y)]
    return x,y

def plot(xdata, ydata, fit_info):

    plt.title("Web Traffic")
    plt.xlabel("Time")
    plt.ylabel("Hits/Hour")
    plt.xticks([w * 7 * 24 for w in range(10)], ['week %i'%w for w in range(10)])
    plt.autoscale(tight = True)

    legend_points = []
    for degree, fit_line in fit_info.items():
        legend_points.append("d=%i"%fit_line["function"].order)
        fx = sp.linspace(0, xdata[-1], 1000)
        plt.plot(fx, fit_line["function"](fx), linewidth = 4)

    plt.legend(legend_points, loc="upper right")

    plt.scatter(xdata, ydata)

    plt.grid()
    plt.show()


def getdata(filename, delimiter = '\t'):
    return sp.genfromtxt(filename, delimiter = delimiter)

def main():
    data = getdata("web_traffic.tsv")
    x, y = formatdata(data)

    degrees = [1, 2, 3, 10, 100]

    fit_info = {}

    for degree in degrees:
        fit_info[degree] = {}
        fit_info[degree]["polynomial"] = sp.polyfit(x, y, degree)
        fit_info[degree]["function"] = sp.poly1d(fit_info[degree]["polynomial"])

    plot(x, y, fit_info)

main()
