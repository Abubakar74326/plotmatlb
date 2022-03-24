from matplotlib import pyplot as plt
from matplotlib import style
plt.rcParams["figure.figsize"] = [7, 3]
plt.rcParams["figure.autolayout"] = True

#style.use("ggplot")

def translation(x,y,Tx,Ty):
    xnew = x + Tx
    ynew = y + Ty
    return xnew, ynew


x=3
y=3
xnew,ynew = translation(x,y,4,5)
plt.xlim(0, 10)
plt.ylim(0, 10)

plt.grid()
plt.title("Translation")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
xpoints = [x,xnew]
ypoints = [y,ynew]

plt.plot(xpoints,ypoints,"o")
#myplot = plt.plot(xpoints,ypoints, marker="o", markersize=10, markeredgecolor="blue", markerfacecolor="red")
#plt.plot(xnew, ynew,"o")
#plt.plot(x, y,"o")
#plt.plot(xnew, ynew, marker="o", markersize=10, markeredgecolor="blue", markerfacecolor="red")
plt.show()


'''def abc(x,y,Tx, Ty):
    xnew,ynew = translation(x,y,Tx,Ty)
    plt.xlim(0, 10)
    plt.ylim(0, 10)

    plt.grid()
    xpoints = [x, xnew, 8]
    ypoints = [y, ynew, 9]

    plt.plot(xpoints, ypoints, "o")
'''    # myplot = plt.plot(xpoints,ypoints, marker="o", markersize=10, markeredgecolor="blue", markerfacecolor="red")
    # plt.plot(xnew, ynew,"o")
    # plt.plot(x, y,"o")
    # plt.plot(xnew, ynew, marker="o", markersize=10, markeredgecolor="blue", markerfacecolor="red")
plt.show()
'''plt.figimage()'''