import MPU9250
import time
import sys
import time
import math
mpu9250 = MPU9250.MPU9250()
mag = mpu9250.readMagnet()

max_x = 0
max_y = 0
max_z = 0
min_x = 0
min_y = 0
min_z = 0

vmax_x = 0
vmax_y = 0
vmax_z = 0
vmin_x = 0
vmin_y = 0
vmin_z = 0
sample_freq = 512
try:
  while True:
    mag = mpu9250.readMagnet()
    if(mag['x'] > max_x):
      max_x = mag['x']
    if(mag['y'] > max_y):
      max_y = mag['y']
    if(mag['z'] > max_z):
      max_z = mag['z']

    if(mag['x'] < min_x):
      min_x = mag['x']
    if(mag['y'] < min_y):
      min_y = mag['y']
    if(mag['z'] < min_z):
      min_z = mag['z']
    time.sleep(1/sample_freq)  
except KeyboardInterrupt:
  print "Max : (" , max_x , "," , max_y , "," , max_z , ")"
  print "\nMin : (" , min_x, "," , min_y , "," , min_z , ")"
  print "\nAverages : (" , (max_x+min_x)/2 , "," , (max_y+min_y)/2 , "," , (max_z+min_z)/2 , ")"
  vmax_x = max_x - ((max_x+min_x)/2)
  vmax_y = max_y - ((max_y+min_y)/2)
  vmax_z = max_z - ((max_z+min_z)/2)
  vmin_x = min_x - ((max_x+min_x)/2)
  vmin_y = min_y - ((max_y+min_y)/2)
  vmin_z = min_z - ((max_z+min_z)/2)
  avgs_x = vmax_x + (vmin_x * -1)
  avgs_y = vmax_y + (vmin_y * -1)
  avgs_z = vmax_z + (vmin_z * -1)
  avg_rad = avgs_x + avgs_y + avgs_z
  avg_rad = avg_rad / 3
  x_scale = avg_rad/avgs_x
  y_scale = avg_rad/avgs_y
  z_scale = avg_rad/avgs_z
  print "\nScales : (" , x_scale , "," , y_scale , "," , z_scale , ")"
