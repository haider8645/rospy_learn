# 08.08.2021: This a script to test rospy

import rospy as rospy

from std_msgs.msg import String 


def main():
	rospy.init_node("test_node")
	pub = rospy.Publisher("/test/topic",String,queue_size=10)
	while not rospy.is_shutdown():
		print("ROS is running...")
		rospy.sleep(10)
		pub.publish("Test")

		
		
	
if __name__ == '__main__':
	main()	
