import sys

import array
import matplotlib as mpl

import cv2
import sim
import time
import numpy as np


sim.simxFinish(-1)

clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
print('Vision Sensor object handling')
res, v1 = sim.simxGetObjectHandle(clientID, 'Vision_sensor', sim.simx_opmode_oneshot_wait)
print('Getting first image')
err, resolution, image = sim.simxGetVisionSensorImage(clientID, v1, 0, sim.simx_opmode_streaming)

while(sim.simxGetConnectionId(clientID) != -1):
    err, resolution, image = sim.simxGetVisionSensorImage(clientID, v1, 0, sim.simx_opmode_buffer)
    if err == sim.simx_return_ok:
        img = np.array(image, dtype=np.uint8)
        img.resize([resolution[1], resolution[0], 3])

        # image was originally upside down, turn it 180 degree
        img180 = cv2.flip(img, 0)

        # show image
        cv2.imshow('image', img180)

        # press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif err == sim.simx_return_novalue_flag:
            print('no image')
            pass
        else:
            print(err)

else:
  print("Failed to connect to remote API Server")
  sim.simxFinish(clientID)

cv2.destroyAllWindows()



