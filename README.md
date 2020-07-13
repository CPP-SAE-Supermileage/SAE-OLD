# SAE Autonomous Simulation

This guide will cover how to install and configure the simulation software using a 64-bit Windows 10 system as an example. You will be installing the following on your computer:
+ Git
+ Python
+ CoppeliaSim Education Edition

### 1. Install Git
Installing git will allow you to easily download the repository, which contains the Python scripts you need to run with the simulation. [Download and install Git from here.](https://git-scm.com/downloads) If you are new to Git and require tutorials for installing and using it, check out this [LinkedIn Learning course.](https://www.linkedin.com/learning/git-essential-training-the-basics/)

#### 1.1: Clone the Repository
Open your Git terminal, and navigate to an empty directory of your choosing. Then, enter the following command to download the Github repository to your computer: 
`git clone https://github.com/maxwildersmith/SAE.git`
#### 1.2: Delete Specific Files
Delete the following files from your clone of the repository. 
+ `__pycache__` (delete the entire directory) 
+ `sim.py`
+ `simConst.py`
+ `remoteApi.dll`

We will replace these at a later stage with copies that reference your system's locally built Python libraries.
### 2. Install Python
First, check if you have Python installed already. To do so, open a command terminal of your choosing. Enter the "python" command like so. A response similar to this means Python is installed.
![Image: Python screenshot](https://i.imgur.com/46VwQXF.png)

If the "python" command is not recognized, that means Python is not installed. [Download and install the correct Python version for your system here.](https://www.python.org/downloads/)

#### IMPORTANT: You must install the correct Python version for your system. If you have a 64-bit operating system, make sure your download specifically includes "64" in the file name. Python installation files without "64" in the file name are for 32-bit systems. Your scripts built for the simulation software will crash if you try running them with an incorrect version installed.

After installing Python, relaunch your command terminal and enter "python" again to verify installation.

#### 2.1: Install Required Python Libraries
Two supplementary Python libraries are required: matplotlib and opencv-python. To download them, enter the following two commands into your terminal:
`pip install matplotlib`
`pip install opencv-python`

You will need to wait for them to finish downloading and installing.
### 3. Install CoppeliaSim Education Edition
This is the simulation software we are using. [Download and install it from here. Choose the "edu" option.](https://www.coppeliarobotics.com/downloads) You may close the simulator after installing it.

### 4. Copy Deleted Files
Now we will copy the files we deleted in step 1.2 back into the directory of our local repository.

First, navigate to the directory where CoppeliaSim was installed. On Windows 10, the default installation location is 
`C:\Program Files\CoppeliaRobotics`

#### 4.1: `sim.py` and `simConst.py`
From the `CoppeliaRobotics` directory, navigate to `CoppeliaRobotics\CoppeliaSimEdu\programming\remoteApiBindings\python\python`

Copy the `sim.py` and `simConst.py` files from this directory into your local repository's directory.

#### 4.2: `remoteApi.dll`
From the `CoppeliaRobotics` directory, navigate to `CoppeliaRobotics\CoppeliaSimEdu\programming\remoteApiBindings\lib\lib`

You will choose the next directory to enter based on your operating system. If you are using Windows, enter the `Windows` directory. If you are on a Mac, enter the `MacOS` directory, etc.

Copy the `remoteApi` file from the appropriate directory into your local repository's directory. Non-Windows operating systems will use file extensions different from `.dll`

#### 4.3: `__pycache__`
This directory will be automatically remade as you run the Python scripts and does not need to be copied over.

### 5. Verify Correct Setup
Finally, we will verify everything was setup correctly by running the simulation software using a Python script.

#### 5.1: Run CoppeliaSim 
In your local repository there is a file called `scene.ttt`. Run this file and it will open up in CoppeliaSim. Click the play button shown in the image below to start the simulation. ![Play Button](https://i.imgur.com/8AaNstM.png)
#### 5.2: Run Python Script
Open a command terminal and navigate to your local repository's directory. Execute the following command. Make sure the simulation is running (step 5.1) or your script will be unable to connect.

`python main.py`

You should see a small frame that takes the perspective of the simulated vehicle and your terminal should be receiving feedback from the simulation. If these two things are happening, then you have successfully completed the setup.
