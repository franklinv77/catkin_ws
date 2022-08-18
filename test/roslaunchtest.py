import roslaunch
import rospkg
import rospy

uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
roslaunch.configure_logging(uuid) 

launch = roslaunch.parent.ROSLaunchParent(uuid, [
    "/home/fvolcic/catkin_ws/launch/sample.launch",
    "/home/fvolcic/catkin_ws/launch/sample2.launch"])

launch.start()

import pdb
pdb.set_trace()

while(True):
    rospy.sleep(3)
#launch.shutdown()
