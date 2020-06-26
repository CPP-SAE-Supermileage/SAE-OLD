import sys

import array
import matplotlib as mpl

import cv2
import sim
import time
import numpy as np
import threading

#close all opened connections 116
sim.simxFinish(-1)

# establish connection
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
# check if client connection successful
if clientID != -1:
    print('Connected to remote API server')
else:
    print('Connection not successful')
    sys.exit('Could not connect')

print('Vision Sensor object handling')
res, v1 = sim.simxGetObjectHandle(clientID, 'Vision_sensor', sim.simx_opmode_oneshot_wait)
print('Getting first image')
err, resolution, image = sim.simxGetVisionSensorImage(clientID, v1, 0, sim.simx_opmode_streaming)

errorCode, left_motor_handle = sim.simxGetObjectHandle(clientID, 'LeftMotor', sim.simx_opmode_oneshot_wait)
if errorCode != sim.simx_return_ok:
    print('Error: ', errorCode)

errorCode, right_motor_handle = sim.simxGetObjectHandle(clientID, 'RightMotor', sim.simx_opmode_oneshot_wait)
if errorCode != sim.simx_return_ok:
    print('Error: ', errorCode)

def vision():
    while (sim.simxGetConnectionId(clientID) != -1):
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

def movement():
    sim.simxAddStatusbarMessage(clientID, 'Connected and running', sim.simx_opmode_oneshot)
    vel = 1
    print("Forward")
    sim.simxSetJointTargetVelocity(clientID, left_motor_handle, -vel, sim.simx_opmode_streaming)
    sim.simxSetJointTargetVelocity(clientID, right_motor_handle, -vel, sim.simx_opmode_streaming)
    time.sleep(40)
    print("Left")
    sim.simxSetJointTargetVelocity(clientID, left_motor_handle, vel, sim.simx_opmode_streaming)
    time.sleep(10)
    sim.simxSetJointTargetVelocity(clientID, left_motor_handle, 0, sim.simx_opmode_streaming)
    sim.simxSetJointTargetVelocity(clientID, right_motor_handle, 0, sim.simx_opmode_streaming)
    print("Stop")

def collision():
    print("collision section")





vision_thread = threading.Thread(target=vision)
movement_thread = threading.Thread(target=movement)
collision_thread = threading.Thread(target=collision)

# start running threads
movement_thread.start()
vision_thread.start()
movement_thread.join()


sim.simxGetPingTime(clientID)

sim.simxFinish(clientID)
cv2.destroyAllWindows()

print('Program ended')
