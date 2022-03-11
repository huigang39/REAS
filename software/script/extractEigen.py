from readBVH import *
import numpy as np


class Eigen:
    def __init__(self, bvhfile: str, jointName: str, channels: list[str]) -> None:
        self.bvhfile, self.jointName, self.channels = bvhfile, jointName, channels

        with open(self.bvhfile, 'r') as f:
            bvh = Bvh(f.read())

        # 获取需要的 channels，即为输入的参数补全为完整的合法参数
        self.channels = [self.channels[i].upper()+'rotation'
                         for i in range(0, len(self.channels))]

        self.data = np.array(bvh.frames_joint_channels(
            self.jointName, self.channels))

        # np.array 相邻两个数组的差值
        self.dataDiff = np.diff(self.data, axis=0)

    def getDataDiff(self) -> np.ndarray:
        """
        获取关节角度变化量
        """
        return self.dataDiff

    def getMean(self) -> np.ndarray:
        """
        获取关节角度变化量的均值
        """
        self.meanValue = self.dataDiff.mean(axis=0)
        return self.meanValue

    def getStd(self) -> np.ndarray:
        """
        获取关节角度变化量的标准差
        """
        self.stdValue = self.dataDiff.std(axis=0)
        return self.stdValue

    def getPPV(self) -> np.ndarray:
        """
        获取关节角度变化量的峰峰值
        """
        self.ppvValue = self.dataDiff.ptp(axis=0)
        return self.ppvValue

    def getAboveMean(self) -> np.ndarray:
        """
        获取关节角度变化量的过均值点数量
        """
        self.aboveMeanValue = np.sum(self.dataDiff > self.meanValue, axis=0)
        return self.aboveMeanValue

    def getEigen(self) -> np.ndarray:
        """
        将特征值组合起来
        """
        self.eigenValue = np.array(
            [self.getMean(), self.getStd(), self.getPPV(), self.getAboveMean()])
        return self.eigenValue


if __name__ == '__main__':
    test = Eigen('software/data/BVH/drink_water/normal.bvh',
                 'RightShoulder', ['x', 'y', 'z'])
    print(test.getEigen().tolist())
