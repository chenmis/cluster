from subprocess import Popen, PIPE
p = Popen(['../faceswap/faceswap.py train -A faceSwapProject/faceA -B faceSwapProject/faceB -m faceSwapProject/ModelAB -tia faceSwapProject/faceA -tib faceSwapProject/faceB -to faceSwapProject/TimelapseAB'], stdin=PIPE, shell=True)
p.communicate(input='\n')
