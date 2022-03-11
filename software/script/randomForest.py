from extractEigen import *
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from ast import literal_eval


class RandomForest:
    def __init__(self, file) -> None:
        self.data = pd.read_csv(file)

    def decisionTreeModel(self) -> None:
        # 决策树模型
        x = self.data[['mean', 'std', 'ppv', 'aboveMean']].to_numpy()
        y = self.data['stage']

        # 将字符串型的数组转换为数字型的数组
        for i in range(0, len(x[0])):
            x[0, i] = literal_eval(
                x[0, i].replace('  ', ' ').replace(' ', ','))

        self.treeClf = DecisionTreeClassifier(max_depth=2, random_state=42)
        self.treeClf.fit(x[0], y)

    def drawModel(self) -> None:
        import matplotlib.pyplot as plt
        from sklearn.tree import plot_tree
        plt.figure(figsize=(12, 8))
        plot_tree(self.treeClf, filled=True)


if __name__ == '__main__':
    test = RandomForest('software/data/dataset/patient/1/patient_1.csv')
    test.decisionTreeModel()
    test.drawModel()
