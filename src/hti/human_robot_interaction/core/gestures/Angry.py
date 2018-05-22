# Choregraphe bezier export in Python.
from naoqi import ALProxy

names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([ 0.10000, 1.50000, 2.80000, 4.30000])
keys.append([ [ -0.18719, [ 3, -0.03333, 0.00000], [ 3, 0.46667, 0.00000]], [ 0.28972, [ 3, -0.46667, 0.00000], [ 3, 0.43333, 0.00000]], [ 0.28972, [ 3, -0.43333, 0.00000], [ 3, 0.50000, 0.00000]], [ -0.18719, [ 3, -0.50000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("HeadYaw")
times.append([ 0.10000, 4.30000])
keys.append([ [ -0.00464, [ 3, -0.03333, 0.00000], [ 3, 1.40000, 0.00000]], [ -0.00464, [ 3, -1.40000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LAnklePitch")
times.append([ 0.10000, 1.50000, 2.80000, 4.30000])
keys.append([ [ 0.07052, [ 3, -0.03333, 0.00000], [ 3, 0.46667, 0.00000]], [ -0.14661, [ 3, -0.46667, 0.00000], [ 3, 0.43333, 0.00000]], [ -0.14661, [ 3, -0.43333, 0.00000], [ 3, 0.50000, 0.00000]], [ 0.07052, [ 3, -0.50000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LAnkleRoll")
times.append([ 0.10000, 4.30000])
keys.append([ [ -0.10734, [ 3, -0.03333, 0.00000], [ 3, 1.40000, 0.00000]], [ -0.10734, [ 3, -1.40000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LElbowRoll")
times.append([ 0.10000, 1.50000, 2.80000, 4.30000])
keys.append([ [ -0.59057, [ 3, -0.03333, 0.00000], [ 3, 0.46667, 0.00000]], [ -1.56207, [ 3, -0.46667, 0.00000], [ 3, 0.43333, 0.00000]], [ -1.56207, [ 3, -0.43333, 0.00000], [ 3, 0.50000, 0.00000]], [ -0.59057, [ 3, -0.50000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LElbowYaw")
times.append([ 0.10000, 1.50000, 2.80000, 4.30000])
keys.append([ [ -1.23359, [ 3, -0.03333, 0.00000], [ 3, 0.46667, 0.00000]], [ -0.26529, [ 3, -0.46667, 0.00000], [ 3, 0.43333, 0.00000]], [ -0.26529, [ 3, -0.43333, 0.00000], [ 3, 0.50000, 0.00000]], [ -1.23359, [ 3, -0.50000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHand")
times.append([ 0.10000, 1.50000, 2.80000, 4.30000])
keys.append([ [ 0.00405, [ 3, -0.03333, 0.00000], [ 3, 0.46667, 0.00000]], [ 0.00646, [ 3, -0.46667, 0.00000], [ 3, 0.43333, 0.00000]], [ 0.00646, [ 3, -0.43333, 0.00000], [ 3, 0.50000, 0.00000]], [ 0.00405, [ 3, -0.50000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHipPitch")
times.append([ 0.10000, 1.50000, 2.80000, 4.30000])
keys.append([ [ 0.20406, [ 3, -0.03333, 0.00000], [ 3, 0.46667, 0.00000]], [ -0.11345, [ 3, -0.46667, 0.00000], [ 3, 0.43333, 0.00000]], [ -0.11345, [ 3, -0.43333, 0.00000], [ 3, 0.50000, 0.00000]], [ 0.20406, [ 3, -0.50000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHipRoll")
times.append([ 0.10000, 1.50000, 2.80000, 4.30000])
keys.append([ [ 0.11202, [ 3, -0.03333, 0.00000], [ 3, 0.46667, 0.00000]], [ 0.03840, [ 3, -0.46667, 0.00000], [ 3, 0.43333, 0.00000]], [ 0.03840, [ 3, -0.43333, 0.00000], [ 3, 0.50000, 0.00000]], [ 0.11202, [ 3, -0.50000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHipYawPitch")
times.append([ 0.10000, 4.30000])
keys.append([ [ -0.16103, [ 3, -0.03333, 0.00000], [ 3, 1.40000, 0.00000]], [ -0.16103, [ 3, -1.40000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LKneePitch")
times.append([ 0.10000, 1.50000, 2.80000, 4.30000])
keys.append([ [ -0.09055, [ 3, -0.03333, 0.00000], [ 3, 0.46667, 0.00000]], [ 0.34907, [ 3, -0.46667, 0.00000], [ 3, 0.43333, 0.00000]], [ 0.34907, [ 3, -0.43333, 0.00000], [ 3, 0.50000, 0.00000]], [ -0.09055, [ 3, -0.50000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LShoulderPitch")
times.append([ 0.10000, 1.50000, 2.80000, 4.30000])
keys.append([ [ 1.58110, [ 3, -0.03333, 0.00000], [ 3, 0.46667, 0.00000]], [ -0.67544, [ 3, -0.46667, 0.00000], [ 3, 0.43333, 0.00000]], [ -0.67544, [ 3, -0.43333, 0.00000], [ 3, 0.50000, 0.00000]], [ 1.58110, [ 3, -0.50000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LShoulderRoll")
times.append([ 0.10000, 1.50000, 2.80000, 4.30000])
keys.append([ [ 0.17408, [ 3, -0.03333, 0.00000], [ 3, 0.46667, 0.00000]], [ 0.68068, [ 3, -0.46667, 0.00000], [ 3, 0.43333, 0.00000]], [ 0.68068, [ 3, -0.43333, 0.00000], [ 3, 0.50000, 0.00000]], [ 0.17408, [ 3, -0.50000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LWristYaw")
times.append([ 0.10000, 1.50000, 2.80000, 4.30000])
keys.append([ [ 0.10887, [ 3, -0.03333, 0.00000], [ 3, 0.46667, 0.00000]], [ -1.09432, [ 3, -0.46667, 0.00000], [ 3, 0.43333, 0.00000]], [ -1.09432, [ 3, -0.43333, 0.00000], [ 3, 0.50000, 0.00000]], [ 0.10887, [ 3, -0.50000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RAnklePitch")
times.append([ 0.10000, 1.50000, 2.80000, 4.30000])
keys.append([ [ 0.06294, [ 3, -0.03333, 0.00000], [ 3, 0.46667, 0.00000]], [ -0.00873, [ 3, -0.46667, 0.00000], [ 3, 0.43333, 0.00000]], [ -0.00873, [ 3, -0.43333, 0.00000], [ 3, 0.50000, 0.00000]], [ 0.06294, [ 3, -0.50000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RAnkleRoll")
times.append([ 0.10000, 4.30000])
keys.append([ [ 0.06600, [ 3, -0.03333, 0.00000], [ 3, 1.40000, 0.00000]], [ 0.06600, [ 3, -1.40000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowRoll")
times.append([ 0.10000, 1.50000, 2.80000, 4.30000])
keys.append([ [ 0.43839, [ 3, -0.03333, 0.00000], [ 3, 0.46667, 0.00000]], [ 1.56207, [ 3, -0.46667, 0.00000], [ 3, 0.43333, 0.00000]], [ 1.56207, [ 3, -0.43333, 0.00000], [ 3, 0.50000, 0.00000]], [ 0.43839, [ 3, -0.50000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowYaw")
times.append([ 0.10000, 1.50000, 2.80000, 4.30000])
keys.append([ [ 1.18545, [ 3, -0.03333, 0.00000], [ 3, 0.46667, 0.00000]], [ 0.83427, [ 3, -0.46667, 0.00000], [ 3, 0.43333, 0.00000]], [ 0.83427, [ 3, -0.43333, 0.00000], [ 3, 0.50000, 0.00000]], [ 1.18545, [ 3, -0.50000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHand")
times.append([ 0.10000, 1.50000, 2.80000, 4.30000])
keys.append([ [ 0.00710, [ 3, -0.03333, 0.00000], [ 3, 0.46667, 0.00000]], [ 0.00716, [ 3, -0.46667, 0.00000], [ 3, 0.43333, 0.00000]], [ 0.00716, [ 3, -0.43333, 0.00000], [ 3, 0.50000, 0.00000]], [ 0.00710, [ 3, -0.50000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHipPitch")
times.append([ 0.10000, 1.50000, 2.80000, 4.30000])
keys.append([ [ 0.18864, [ 3, -0.03333, 0.00000], [ 3, 0.46667, 0.00000]], [ 0.08029, [ 3, -0.46667, 0.00000], [ 3, 0.43333, 0.00000]], [ 0.08029, [ 3, -0.43333, 0.00000], [ 3, 0.50000, 0.00000]], [ 0.18864, [ 3, -0.50000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHipRoll")
times.append([ 0.10000, 1.50000, 2.80000, 4.30000])
keys.append([ [ -0.06745, [ 3, -0.03333, 0.00000], [ 3, 0.46667, 0.00000]], [ 0.00175, [ 3, -0.46667, 0.00000], [ 3, 0.43333, 0.00000]], [ 0.00175, [ 3, -0.43333, 0.00000], [ 3, 0.50000, 0.00000]], [ -0.06745, [ 3, -0.50000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RKneePitch")
times.append([ 0.10000, 1.50000, 2.80000, 4.30000])
keys.append([ [ -0.07359, [ 3, -0.03333, 0.00000], [ 3, 0.46667, 0.00000]], [ 0.08029, [ 3, -0.46667, 0.00000], [ 3, 0.43333, 0.00000]], [ 0.08029, [ 3, -0.43333, 0.00000], [ 3, 0.50000, 0.00000]], [ -0.07359, [ 3, -0.50000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderPitch")
times.append([ 0.10000, 1.50000, 2.80000, 4.30000])
keys.append([ [ 1.47672, [ 3, -0.03333, 0.00000], [ 3, 0.46667, 0.00000]], [ -0.38921, [ 3, -0.46667, 0.00000], [ 3, 0.43333, 0.00000]], [ -0.38921, [ 3, -0.43333, 0.00000], [ 3, 0.50000, 0.00000]], [ 1.47672, [ 3, -0.50000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderRoll")
times.append([ 0.10000, 1.50000, 2.80000, 4.30000])
keys.append([ [ -0.11874, [ 3, -0.03333, 0.00000], [ 3, 0.46667, 0.00000]], [ -0.61959, [ 3, -0.46667, 0.00000], [ 3, 0.43333, 0.00000]], [ -0.61959, [ 3, -0.43333, 0.00000], [ 3, 0.50000, 0.00000]], [ -0.11874, [ 3, -0.50000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RWristYaw")
times.append([ 0.10000, 1.50000, 2.80000, 4.30000])
keys.append([ [ 0.26529, [ 3, -0.03333, 0.00000], [ 3, 0.46667, 0.00000]], [ 1.02800, [ 3, -0.46667, 0.00000], [ 3, 0.43333, 0.00000]], [ 1.02800, [ 3, -0.43333, 0.00000], [ 3, 0.50000, 0.00000]], [ 0.17330, [ 3, -0.50000, 0.00000], [ 3, 0.00000, 0.00000]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys);
except BaseException, err:
  print err
