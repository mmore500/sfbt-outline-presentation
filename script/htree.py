import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullLocator

def drawHTree(order, x_center, y_center, length,lwfn=lambda o: 1):

    if order < 0:
        return

    plt.plot([x_center - length, x_center + length] , [y_center, y_center],c='b',linewidth=lwfn(order))
    plt.plot([x_center - length, x_center - length] , [y_center+length, y_center-length],c='b',linewidth=lwfn(order))
    plt.plot([x_center + length, x_center + length] , [y_center+length, y_center-length],c='b',linewidth=lwfn(order))

    drawHTree(order - 1, x_center - length, y_center - length, length / 2,lwfn=lwfn)
    drawHTree(order - 1, x_center + length, y_center - length, length / 2,lwfn=lwfn)
    drawHTree(order - 1, x_center - length, y_center + length, length / 2,lwfn=lwfn)
    drawHTree(order - 1, x_center + length, y_center + length, length / 2,lwfn=lwfn)

def drawHTreeWalk(order, x_center, y_center, length,restrict=[]):

    if order < 0:
        return

    if('down' not in restrict):
        plt.plot([x_center + length, x_center] , [y_center, y_center],c='r',linewidth=8)
        plt.plot([x_center + length, x_center + length] , [y_center, y_center+length],c='r',linewidth=8)
        drawHTreeWalk(order - 1, x_center + length, y_center + length, length / 2,restrict=['up'])

    if('up' not in restrict):
        plt.plot([x_center, x_center - length] , [y_center, y_center],c='r',linewidth=8)
        plt.plot([x_center - length, x_center - length] , [y_center-length, y_center],c='r',linewidth=8)
        drawHTreeWalk(order - 1, x_center - length, y_center - length, length / 2,restrict=['down'])

def drawCompletion(order, x_center, y_center, length,lwfn=lambda o: 1):

    if order < 0:
        return

    plt.plot([x_center - length, x_center - 2*length] , [y_center, y_center],c='y',linewidth=lwfn(order))
    plt.plot([x_center + length, x_center + 2*length] , [y_center, y_center],c='y',linewidth=lwfn(order))

    if order < 1:
        return

    plt.plot([x_center - length, x_center - length] , [y_center+length, y_center + 2 *length],c='y',linewidth=lwfn(order))
    plt.plot([x_center - length, x_center - length] , [y_center-length, y_center - 2 *length],c='y',linewidth=lwfn(order))

    plt.plot([x_center + length, x_center + length] , [y_center+length, y_center + 2 *length],c='y',linewidth=lwfn(order))
    plt.plot([x_center + length, x_center + length] , [y_center-length, y_center - 2 *length],c='y',linewidth=lwfn(order))

    drawCompletion(order - 1, x_center - length, y_center - length, length / 2,lwfn=lwfn)
    drawCompletion(order - 1, x_center + length, y_center - length, length / 2,lwfn=lwfn)
    drawCompletion(order - 1, x_center - length, y_center + length, length / 2,lwfn=lwfn)
    drawCompletion(order - 1, x_center + length, y_center + length, length / 2,lwfn=lwfn)

def drawGrid(order, x_center, y_center, length):
    for y in np.linspace(y_center-2*length, y_center+2*length, 2**(order+1)+1):
        plt.plot([x_center - 2*length, x_center + 2*length] , [y, y], c='gray',linewidth=0.5)

    for x in np.linspace(x_center-2*length, y_center+2*length, 2**(order+1)+1):
        plt.plot([x, x] , [y_center - 2*length, y_center + 2*length], c='gray',linewidth=0.5)

def drawZigZag(order, x_center, y_center, length):
    ys = np.linspace(y_center-2*length, y_center+2*length, 2**(order+1)+1)
    xs = np.linspace(x_center-2*length, y_center+2*length, 2**(order+1)+1)

    offset = 4*length/(2**(order+2))

    for x,y in list(zip(xs,ys))[:-2]:
        plt.plot([x+offset, y+offset] , [x+3*offset, y+offset], c='red',linewidth=8)
        plt.plot([x+3*offset, y+offset] , [x+3*offset, y+3*offset], c='red',linewidth=8)

plt.figure(figsize=(25,25))

drawGrid(3, 100, 100, 200)

drawZigZag(3, 100, 100, 200)

plt.axes().set_aspect('equal', 'datalim')

plt.axis('off')

plt.gca().xaxis.set_major_locator(NullLocator())
plt.gca().yaxis.set_major_locator(NullLocator())

plt.savefig('img/htree/grid-small-zigzag.pdf',transparent=True,figsize=(500,500),bbox_inches='tight', pad_inches=0)

plt.clf()

drawGrid(3, 100, 100, 200)

drawHTreeWalk(3, 100, 100, 200)

plt.axes().set_aspect('equal', 'datalim')

plt.axis('off')

plt.gca().xaxis.set_major_locator(NullLocator())
plt.gca().yaxis.set_major_locator(NullLocator())

plt.savefig('img/htree/grid-small-treewalk.pdf',transparent=True,figsize=(500,500),bbox_inches='tight', pad_inches=0)

plt.clf()

drawGrid(4, 100, 100, 200)

drawHTreeWalk(4, 100, 100, 200)

plt.axes().set_aspect('equal', 'datalim')

plt.axis('off')

plt.gca().xaxis.set_major_locator(NullLocator())
plt.gca().yaxis.set_major_locator(NullLocator())

plt.savefig('img/htree/grid-large-treewalk.pdf',transparent=True,figsize=(500,500),bbox_inches='tight', pad_inches=0)

plt.clf()

drawGrid(4, 100, 100, 200)

drawZigZag(4, 100, 100, 200)

plt.axes().set_aspect('equal', 'datalim')

plt.axis('off')

plt.gca().xaxis.set_major_locator(NullLocator())
plt.gca().yaxis.set_major_locator(NullLocator())

plt.savefig('img/htree/grid-large-zigzag.pdf',transparent=True,figsize=(500,500),bbox_inches='tight', pad_inches=0)

plt.clf()

drawGrid(3, 100, 100, 200)

drawHTree(3, 100, 100, 200,lwfn=lambda o: 8)

plt.axes().set_aspect('equal', 'datalim')

plt.axis('off')

plt.gca().xaxis.set_major_locator(NullLocator())
plt.gca().yaxis.set_major_locator(NullLocator())

plt.savefig('img/htree/const-tree-grid.pdf',transparent=True,figsize=(500,500),bbox_inches='tight', pad_inches=0)

plt.clf()

drawGrid(4, 100, 100, 200)

drawHTree(4, 100, 100, 200,lwfn=lambda o: 1.5*o+4)

plt.axes().set_aspect('equal', 'datalim')

plt.axis('off')

plt.gca().xaxis.set_major_locator(NullLocator())
plt.gca().yaxis.set_major_locator(NullLocator())

plt.savefig('img/htree/var-tree-grid.pdf',transparent=True,figsize=(500,500),bbox_inches='tight', pad_inches=0)

plt.clf()

drawGrid(4, 100, 100, 200)

drawCompletion(4, 100, 100, 200,lwfn=lambda o: 1.5*o+4)

drawHTree(4, 100, 100, 200,lwfn=lambda o: 1.5*o+4)

plt.axes().set_aspect('equal', 'datalim')

plt.axis('off')

plt.gca().xaxis.set_major_locator(NullLocator())
plt.gca().yaxis.set_major_locator(NullLocator())

plt.savefig('img/htree/var-tree-compl-grid.pdf',transparent=True,figsize=(500,500),bbox_inches='tight', pad_inches=0)

plt.clf()

drawGrid(4, 100, 100, 200)

drawCompletion(4, 100, 100, 200,lwfn=lambda o: 5)

drawHTree(4, 100, 100, 200,lwfn=lambda o: 5)

plt.axes().set_aspect('equal', 'datalim')

plt.axis('off')

plt.gca().xaxis.set_major_locator(NullLocator())
plt.gca().yaxis.set_major_locator(NullLocator())

plt.savefig('img/htree/const-tree-compl-grid.pdf',transparent=True,figsize=(500,500),bbox_inches='tight', pad_inches=0)

plt.clf()

drawGrid(2, 100, 100, 200)

plt.axes().set_aspect('equal', 'datalim')

plt.axis('off')

plt.gca().xaxis.set_major_locator(NullLocator())
plt.gca().yaxis.set_major_locator(NullLocator())

plt.xlabel("N")
plt.ylabel("N")

plt.savefig('img/htree/grid.pdf',transparent=True,figsize=(500,500),bbox_inches='tight', pad_inches=0)
