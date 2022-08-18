

#include "ros/ros.h"
#include "std_msgs/String.h"

#include <stress/stress.h>

#include <sstream>
#include <vector>

#define NUM_BYTES 1e7

/**
 * This tutorial demonstrates simple sending of messages over the ROS system.
 */
int main(int argc, char **argv)
{
  ros::init(argc, argv, "talker");
  ros::NodeHandle n;
  ros::Publisher chatter_pub = n.advertise<stress::stress>("chatter", 1000);
  ros::Rate loop_rate(10);
  int count = 0;

 std::vector<int64_t> vec( NUM_BYTES / 64 );  

  while (ros::ok())
  {

    stress::stress s;
    s.datum = vec; 

    chatter_pub.publish(s); 
  }


  return 0;
}