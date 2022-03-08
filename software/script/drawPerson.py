from readBVH import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def main():
    with open('software/data/shangzhizhanbi1_01_part_Char00.bvh') as f:
        mocap = Bvh(f.read())
    LeftForeArm = mocap.frame_joint_channel(22, 'LeftForeArm', 'Xrotation')
    print(LeftForeArm)


if __name__ == '__main__':
    main()
