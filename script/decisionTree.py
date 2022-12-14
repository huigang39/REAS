import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier


class DecisionTree():
    def __init__(self, trainData: pd.DataFrame, testData: pd.DataFrame) -> None:
        self.trainData = trainData.dropna()
        self.testData = testData.dropna()

    def preProcessData(self) -> None:
        """
        数据预处理
        """
        # 训练数据
        self.X_train = pd.get_dummies(self.trainData.drop(
            'stage', axis=1), drop_first=True)
        self.y_train = self.trainData['stage']

        # 测试数据
        self.X_test = pd.get_dummies(self.testData.drop(
            'stage', axis=1), drop_first=True)
        self.y_test = self.testData['stage']

    def trainModel(self) -> None:
        """
        训练模型
        """
        self.model = RandomForestClassifier(
            n_estimators=10, max_features='auto', random_state=101)
        self.model.fit(self.X_train, self.y_train)

    # def gridSearch(self) -> None:
    #     """
    #     网格搜索与 AdaBoost 提升法
    #     """
    #     ada_clf = AdaBoostClassifier(
    #         DecisionTreeClassifier(max_depth=1), random_state=101)
    #     ada_clf.fit(self.X_train, self.y_train)
    #     param_grid = {'n_estimators': [10, 15, 20, 25, 30, 35, 40], 'learning_rate': [
    #         0.01, 0.1, 0.5, 1], 'algorithm': ['SAMME', 'SAMME.R']}
    #     grid = GridSearchCV(ada_clf, param_grid)
    #     grid.fit(self.X_train, self.y_train)
    #     print("grid.best_params_ = ", grid.best_params_,
    #           ", grid.best_score_ =", grid.best_score_)

    def predictResult(self) -> list:
        """
        预测结果
        """
        preds = self.model.predict(self.X_test)
        score = accuracy_score(self.y_test, preds)
        return preds, score


if __name__ == '__main__':
    trainData = pd.read_csv(
        'software/data/dataset/康复评估动作/dataset/allData.csv')
    testData = pd.read_csv(
        'software/data/dataset/康复评估动作/test/2/2.csv')

    test = DecisionTree(trainData, testData)
    data = test.preProcessData()
    model = test.trainModel()
    # test.gridSearch()
    print(test.predictResult())
