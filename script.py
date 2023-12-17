#!/usr/bin/env python3
import rospy
import time
from geometry_msgs.msg import Twist

from sensor_msgs.msg import LaserScan

class robot():
    def __init__(self):

        self.robot_sub = rospy.Subscriber("/scan", LaserScan,self.scan_callback)
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.d = 0.0

        self.ctrl_c =False

        self.rate = rospy.Rate(5)
        rospy.on_shutdown(self.shutdownhook)
    def scan_callback(self,msg):
       # print(len(msg.ranges))
        self.a = msg.ranges[180]
        self.b = msg.ranges[360]
        self.c = msg.ranges[540]
        self.d = msg.ranges[1]

    def read_laser(self):
        while not self.ctrl_c:
            if self.a>5:
                self.a =5
            if self.b>5:
                self.b =5
            if self.c>5:
                self.c =5
            if self.d>5:
                self.d =5

            print("a= " + str(self.a) + " b= " + str(self.b) + " c= " + str(self.c) + " d " + str(self.d))
            self.rate.sleep()

            
    def shutdownhook(self):
        self.ctrl_c = True

    def avoid_wall(self):
        maxi = max(self.a,self.b,self.c,self.d)
        if self.a == maxi:
            if __name__== '__main__':
                rospy.init_node("calibrate left right")
                rospy.loginfo("node has been started")

                rate = rospy.Rate(10)

                pub = rospy.Publisher("/cmd_vel",Twist,queue_size =10)

            while not rospy.is_shutdown():
                    #publish cmnd velo


                msg = Twist()
                msg.linear.x = 0.0
                msg.angular.z = 1.0
                pub.publish(msg)
                time.sleep(3.1)

        elif self.b == maxi:
            if __name__== '__main__':
                rospy.init_node("calibrate left right")
                rospy.loginfo("node has been started")

                rate = rospy.Rate(10)

                pub = rospy.Publisher("/cmd_vel",Twist,queue_size =10)

            while not rospy.is_shutdown():
                    #publish cmnd velo


                msg = Twist()
                msg.linear.x = -1.0
                msg.angular.z = 0.0
                pub.publish(msg)
                time.sleep(3.1)

        elif self.c == maxi:
            if __name__== '__main__':
                rospy.init_node("calibrate left right")
                rospy.loginfo("node has been started")

                rate = rospy.Rate(10)

                pub = rospy.Publisher("/cmd_vel",Twist,queue_size =10)

            while not rospy.is_shutdown():
                    #publish cmnd velo


                msg = Twist()
                msg.linear.x = 0.0
                msg.angular.z = -1.0
                pub.publish(msg)
                time.sleep(3.1)

        else:
            if __name__== '__main__':
                rospy.init_node("calibrate left right")
                rospy.loginfo("node has been started")

                rate = rospy.Rate(10)

                pub = rospy.Publisher("/cmd_vel",Twist,queue_size =10)

            while not rospy.is_shutdown():
                    #publish cmnd velo


                msg = Twist()
                msg.linear.x = 1.0
                msg.angular.z = 0.0
                pub.publish(msg)
                time.sleep(3.1)



            

if __name__ =='__main__':
    rospy.init_node('rosbot_test',anonymous=True)
    robot_object = robot()
    try:
        robot_object.read_laser()
        robot_object.avoid_wall()
    except rospy.ROSInterruptException:
        pass    

