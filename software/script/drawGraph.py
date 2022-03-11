from extractEigen import *
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, data: Eigen) -> None:
        self.data = data

    def drawLine(self) -> None:
        """
        绘制线图
        """
        plt.plot(self.data.getDataDiff())
        plt.show()


if __name__ == '__main__':
    test = Graph(Eigen('software/data/BVH/drink_water/normal.bvh',
                 'RightShoulder', ['x', 'y', 'z']))
    test.drawLine()
