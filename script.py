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

        self.rate = rospy.Rate(1)
        rospy.on_shutdown(self.shutdownhook)
    def scan_callback(self,msg):
       # print(len(msg.ranges))
        self.a = min(msg.ranges[180],5)
        self.b = min(msg.ranges[360],5)
        self.c = min(msg.ranges[540],5)
        self.d = min(msg.ranges[1],5)


        print("a= " + str(self.a) + " b= " + str(self.b) + " c= " + str(self.c) + " d " + str(self.d))
      #  self.rate.sleep()
        time.sleep(1)


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
        while not self.ctrl_c:
            maxi = max(self.a,self.b,self.c,self.d)
            print(maxi)
            print("a")
            time.sleep(1)

            #self.rate.sleep()

           # rospy.init_node("calibrate_left_right")
            




        """if self.a == maxi:
            
            rospy.init_node("calibrate_left_right")
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
            
            rospy.init_node("calibrate_left_right")
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
            
            rospy.init_node("calibrate_left_right")
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
            
            rospy.init_node("calibrate_left_right")
            rospy.loginfo("node has been started")

            rate = rospy.Rate(10)

            pub = rospy.Publisher("/cmd_vel",Twist,queue_size =10)

            while not rospy.is_shutdown():
                    #publish cmnd velo


                msg = Twist()
                msg.linear.x = 1.0
                msg.angular.z = 0.0
                pub.publish(msg)
                time.sleep(3.1)"""



            

if __name__ =='__main__':    
    
    rospy.init_node('rosbot_test',anonymous=True)
    robot_object = robot()
    try:
       # robot_object.read_laser()
        robot_object.avoid_wall()
        rospy.loginfo("node has been started")
        pub = rospy.Publisher("/cmd_vel",Twist,queue_size =10)
        rate = rospy.Rate(1)

        while not rospy.is_shutdown():
            msg = Twist()
            msg.linear.x = 0.0
            msg.angular.z = 1.0
            
            #time.sleep(3.1)
            pub.publish(msg)
            rate.sleep()


    except rospy.ROSInterruptException:
        pass    

