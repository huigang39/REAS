import pandas as pd
import plotly.express as px
import streamlit as st
from fastdtw import *
from sklearn.metrics import r2_score

from extractEigen import *


class DTW:
    def __init__(self, normalData: Eigen, patientData: Eigen) -> None:
        self.column = ['x', 'y', 'z']
        self.normalData = pd.DataFrame(columns=self.column)
        self.patientData = pd.DataFrame(columns=self.column)

        for i in range(0, len(normalData.getDataDiff())):
            for j in ['x', 'y', 'z']:
                self.normalData[j] = [normalData.getDataDiff()[
                    i][['x', 'y', 'z'].index(j)]]
                self.patientData[j] = [patientData.getDataDiff()[
                    i][['x', 'y', 'z'].index(j)]]

    def drawDTW(self):
        self.distance, self.path = fastdtw(
            self.normalData['x'], self.patientData['x'])

        result = []
        for i in range(0, len(self.path)):
            result.append([self.normalData['x'].iloc[self.path[i][0]],
                           self.normalData['y'].iloc[self.path[i][0]],
                           self.normalData['z'].iloc[self.path[i][1]]])

        dfSync = pd.DataFrame(data=result, columns=[
            'x', 'y', 'z']).dropna()
        dfSync = dfSync.drop_duplicates(subset=['x'])
        dfSync = dfSync.sort_values(by='x')
        dfSync = dfSync.reset_index(drop=True)
        dfSync.to_csv('software/data/synchronized_dataset.csv', index=False)

    def visualizeChart(self):
        pass


if __name__ == '__main__':
    normalData = Eigen(
        'software/data/BVH/康复恢复动作/drink_water/normal.bvh', 'RightShoulder', ['x', 'y', 'z'])
    patientData = Eigen(
        'software/data/BVH/康复恢复动作/drink_water/patient.bvh', 'RightShoulder', ['x', 'y', 'z'])

    test = DTW(normalData, patientData)
    test.drawDTW()
