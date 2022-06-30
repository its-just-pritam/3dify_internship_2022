# *facemap* Module

This module generates a template, i.e. a user generated face mesh being projected over a mediapipe mesh.

## Environment Variables

To run this project, you will need to create a `.env` file in the current directory 
    and update it with the following code below. Assign the value to 
    `BLENDER_PATH` variable.
```
BLENDER_PATH=<path_to_your_blender_exe_file>
``` 
**Eg:**
BLENDER_PATH=C:/Program Files/Blender Foundation/Blender 3.1/blender.exe

## Run Locally

Run the command in the virtual environment by replacing the arguments appropiately.
```
python main.py <MEDIAPIPE_FACE_OBJ_PATH> <FACE_OBJ_PATH>