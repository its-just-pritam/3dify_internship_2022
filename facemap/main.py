import os
import sys
from mapping import centroid_mapper
from dotenv import load_dotenv

if __name__ == '__main__':

    load_dotenv()
    blender_path = os.getenv('BLENDER_PATH')

    mp_file = sys.argv[1]
    hg_file = sys.argv[2]

    centroid_mapper(mp_file, hg_file)
    print('++ Mapping Completed ++')
    blender_invoke_command = '"' + blender_path + '"' + ' --background --python ' + 'transform.py ' + mp_file + ' ' + hg_file
    os.system(blender_invoke_command)
    print('++ Template Generated ++')