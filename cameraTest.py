import picamera
from time import sleep, gmtime, strftime
from os.path import join as pjoin


camera = picamera.PiCamera()
camera.resolution = (640, 480)

filename = "scare_" + strftime("%m-%d %H:%M:%S", gmtime()) + ".h264"
path_to_file = pjoin("Scare Vids", filename)

#start recording using pi camera
camera.start_recording(path_to_file)
camera.start_preview()
#wait for video to record
camera.wait_recording(8)
#stop recording
camera.stop_recording()
camera.stop_preview()
camera.close()
print("video recording stopped")