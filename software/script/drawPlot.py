from readBVH import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


timeLine = []
angleListXrotation = []
angleListYrotation = []
angleListZrotation = []


def main():
    with open('software/data/shangzhizhanbi1_01_part_Char00.bvh') as f:
        mocap = Bvh(f.read())
    drowPlot(mocap)


def drowPlot(mocap: Bvh):
    for i in range(0, mocap.nframes):
        timeLine.append(mocap.frame_time*i)
        angleListXrotation.append(mocap.frame_joint_channel(
            i, 'LeftForeArm', 'Xrotation'))


if __name__ == '__main__':
    main()
