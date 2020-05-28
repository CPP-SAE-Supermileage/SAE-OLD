import sys

import cv2
import sim
import time
import numpy as np
import matplotlib as mpl

print('Program started')

sim.simxFinish(-1)  # just in case, close all opened connections 116"
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)  # Connect to CoppeliaSim
if clientID != -1:  # check if client connection successful
    print('Connected to remote API server')

else:
    print('Connection not successful')
    sys.exit('Could not connect')

errorCode, left_motor_handle = sim.simxGetObjectHandle(clientID, 'LeftMotor', sim.simx_opmode_oneshot_wait)

if errorCode != sim.simx_return_ok:
    print('Error: ', errorCode)

errorCode, right_motor_handle = sim.simxGetObjectHandle(clientID, 'RightMotor', sim.simx_opmode_oneshot_wait)

if errorCode != sim.simx_return_ok:
    print('Error: ', errorCode)

time.sleep(2)
sim.simxAddStatusbarMessage(clientID, 'Connected and running', sim.simx_opmode_oneshot)
vel = 1
print("Forward")
sim.simxSetJointTargetVelocity(clientID, left_motor_handle, -vel, sim.simx_opmode_streaming)
sim.simxSetJointTargetVelocity(clientID, right_motor_handle, -vel, sim.simx_opmode_streaming)
time.sleep(10)
print("Left")
sim.simxSetJointTargetVelocity(clientID, left_motor_handle, vel, sim.simx_opmode_streaming)
time.sleep(10)
sim.simxSetJointTargetVelocity(clientID, left_motor_handle, 0, sim.simx_opmode_streaming)
sim.simxSetJointTargetVelocity(clientID, right_motor_handle, 0, sim.simx_opmode_streaming)
print("Stop")

# open cv code
print('Vision Sensor object handling')
res, v1 = sim.simxGetObjectHandle(clientID, 'Vision_sensor', sim.simx_opmode_oneshot_wait)
print('Getting first image')
err, resolution, image = sim.simxGetVisionSensorImage(clientID, v1, 0, sim.simx_opmode_streaming)


while(sim.simxGetConnectionId(clientID) != -1):
    err, resolution, image = sim.simxGetVisionSensorImage(clientID, v1, 0, sim.simx_opmode_buffer)
    if err == sim.simx_return_ok:
        print('image OK!!')
        img = np.array(image, dtype=np.uint8)
        img.resize([resolution[1], resolution[0], 3])
        cv2.imshow('image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif err == sim.simx_return_novalue_flag:
            print('no image yet')
            pass
        else:
            print(err)


# end
sim.simxGetPingTime(clientID)

sim.simxFinish(clientID)
print('Program ended')
