from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np



def modular_plot_func(func, bounds="circle", func_str="f(z)", **kwargs):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = "3d")
    if "res" in kwargs:
        res = kwargs["res"]
    else: res = 20
    if bounds=="square":
        if "ranges" in kwargs:
            r = kwargs["ranges"]
            X = np.arange(r[0],r[1],(r[1]-r[0])/res)
            Y = np.arange(r[2],r[3],(r[3]-r[2])/res)
            X,Y = np.meshgrid(X,Y)
        else:
            raise ValueError("""Missing required kwarg (xmin,xmax,ymin,ymax)
                             for square plot""")
    elif bounds=="circle":
        if all(args in kwargs for args in ["r"]):
            u = np.linspace(0, 2 * np.pi, res)
            v = np.linspace(0, np.pi, res)
            X = kwargs["r"] * np.outer(np.cos(u), np.sin(v))
            Y = kwargs["r"] * np.outer(np.sin(u), np.sin(v))
        else:
            raise ValueError("""Missing required kwarg (r, centre)
                             for circular plot""")
    Z = func(X + 1j*Y)
    ax.set_xlabel("Re[Z]")
    ax.set_ylabel("Im[Z]")
    ax.set_zlabel("|%s|"%func_str)
    Z = np.abs(Z)
    if "max_z" in kwargs:
        Z = np.minimum(Z,kwargs["max_z"]*np.ones(Z.shape))
    surf = ax.plot_surface(X,Y,Z, cmap = cm.coolwarm)
    plt.show()

modular_plot_func(lambda z:1/(1+z**2),bounds="square",ranges=[-2,2,-2,2],
                  func_str="1/(1+Z**2)", max_z = 3, res = 1000)
