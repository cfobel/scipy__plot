import itertools

from numpy import *
import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3


if __name__ == '__main__':
    x, y = [array(l) for l in zip(*list(itertools.permutations(range(10), 2)))]
    z = x * y

    fig = p.figure()
    ax = p3.Axes3D(fig)
    ax.plot3D(x, y, z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    fig.add_axes(ax)
    p.show()

    x = r_[0:10]
    y = r_[10:0:-1]
    X, Y = p.meshgrid(x, y)
    Z = X * Y
    fig = p.figure()
    ax = p3.Axes3D(fig)
    ax.contour3D(X, Y, Z)
    ax.set_zlabel('Z')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    p.show()

    fig=p.figure()
    ax = p3.Axes3D(fig)
    # x, y, and z are 100x100 arrays
    ax.plot_surface(X, Y, Z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    p.show()
