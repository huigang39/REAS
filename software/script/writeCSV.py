from extractEigen import Eigen
import os


class OUTPUT:
    def __init__(self, fileList: list) -> None:
        self.fileList = fileList
        self.normalStage = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}  # 病人理论动作
        self.patientStage = {1: [], 2: [],
                             3: [], 4: [], 5: [], 6: []}  # 病人实际动作

    @staticmethod
    def getfileList(path: str) -> list:
        """
        获取指定目录下的所有文件完整路径
        """
        fileList = []
        for root, dirs, files in os.walk(path):
            for file in files:
                fileList.append(os.path.join(root, file))
        return fileList

    def makeDirs(self) -> None:
        """
        创建文件夹
        """
        for file in self.fileList:
            if not os.path.exists(file[0:file.rfind('/')].replace('BVH', 'dataset')):
                os.makedirs(file[0:file.rfind('/')].replace('BVH', 'dataset'))

    def writeSingleEigenToCSV(self) -> None:
        """
        将单个文件数据的特征值写入 csv 文件
        """
        self.makeDirs()
        for file in self.fileList:
            eigen = Eigen(file, 'RightShoulder', ['x', 'y', 'z'])

            with open(file.replace('BVH', 'dataset').replace('bvh', 'csv'), 'w') as f:
                f.writelines('mean,std,ppv,aboveMean,stage\n')

                f.writelines(
                    str(eigen.getMean()) + ',' +
                    str(eigen.getStd()) + ',' +
                    str(eigen.getPPV()) + ',' +
                    str(eigen.getAboveMean()) + ',')

                if 'drink_water' not in file:
                    f.writelines(file[file.rfind('/') -
                                 1:file.rfind('/')] + '\n')

    # TODO
    def writeCollectiveEigen(self) -> None:
        """
        将同一时期的文件数据的特征值写入 csv 文件
        """
        for file in self.fileList:
            if 'normal' in file:
                self.normalStage[int(file[file.rfind(
                    '/')-1:file.rfind('/')])].append(file)

            if 'patient' in file:
                self.patientStage[int(file[file.rfind(
                    '/')-1:file.rfind('/')])].append(file)


if __name__ == '__main__':
    fileList = OUTPUT.getfileList('software/data/BVH/')
    test = OUTPUT(fileList)
    test.writeSingleEigenToCSV()
    # test.writeCollectiveEigen()
