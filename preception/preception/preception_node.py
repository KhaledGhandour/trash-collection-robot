import rclpy
from rclpy.node import Node


from std_msgs.msg import String
from custom_interface.srv import ComponentStatus


class preception_node(Node):
    def __init__(self):
        super().__init__("preception_node")

        self.camera_subscriner=self.create_subscription(String,'camera',self.camera_callback,10)
        self.trash_detection_publisher=self.create_publisher(String,"trash_detection",10)
        self.component_status_service=self.create_service(ComponentStatus,'comonpont_status',self.handle_component_status)


    

    def camera_callback(self,message):

        msg=String()

        if (message.data == "trash"):
            msg.data = "I see Trash"
        
        else:
            msg.data = " iI can not see any thing"

        
        self.trash_detection_publisher.publish(msg)
        self.get_logger().info('publishing : %s'%msg.data)




    
    def handle_component_status(self, request, response):
      self.get_logger().info("Server called!")
      if request.component == "camera":
       response.status = "Camera Battery is at 100%"
      else:
       response.status = "Error: Component unavailable"

      return response



def main(args=None):
    rclpy.init(args=args)


       
    rclpy.spin(preception_node())

    """
    Destroy the node explicitly
    (optional - otherwise it will be done automatically
    when the garbage collector destroys the node object)
    """

    
    preception_node.destroy_node()
    rclpy.shutdown()





if __name__=='__main__':
    main()






























































































# import rclpy
# from rclpy.node import Node

# from std_msgs.msg import String
# from custom_interfaces.srv import ComponentStatus


# class PerceptionNode(Node):

#   def __init__(self):
#     super().__init__('perception_node')

#     self.cameraTopic = self.declare_parameter(
#         "cameraTopic",
#         "None"
#     )
#     self.trashDetectionTopic = self.declare_parameter(
#         "trashDetectionTopic",
#         "None"
#     )
#     self.componentStatusService = self.declare_parameter(
#         "componentStatusService",
#         "None"
#     )

#     self.get_parameter_values()

#     self.cameraSubscriber = self.create_subscription(
#         String,
#         self.cameraTopic,
#         self.camera_callback,
#         10
#     )

#     self.trashDetectionPublisher = self.create_publisher(
#         String,
#         self.trashDetectionTopic,
#         10
#     )

#     self.componentStatusService = self.create_service(
#         ComponentStatus,
#         self.componentStatusService,
#         self.handle_component_status
#     )

#   def get_parameter_values(self):
#     self.cameraTopic = self.get_parameter(
#         'cameraTopic').get_parameter_value().string_value
#     self.trashDetectionTopic = self.get_parameter(
#         'trashDetectionTopic').get_parameter_value().string_value
#     self.componentStatusService = self.get_parameter(
#         'componentStatusService').get_parameter_value().string_value

#   def camera_callback(self, message):
#     msg = String()
#     """
#     In practical cases, we process images to understand if trash is present
#     """
#     if (message.data == "trash"):
#       msg.data = "I see trash"
#     else:
#       msg.data = "I see nothing"
#     self.trashDetectionPublisher.publish(msg)
#     self.get_logger().info('Publishing: "%s"' % msg.data)

#   def handle_component_status(self, request, response):
#     self.get_logger().info("Server called!")
#     if request.component == "camera":
#       response.status = "Camera Battery is at 100%"
#     else:
#       response.status = "Error: Component unavailable"

#     return response


# def main(args=None):
#   rclpy.init(args=args)

#   perceptionNode = PerceptionNode()

#   rclpy.spin(perceptionNode)

#   # Destroy the node explicitly
#   # (optional - otherwise it will be done automatically
#   # when the garbage collector destroys the node object)
#   perceptionNode.destroy_node()
#   rclpy.shutdown()


# if __name__ == '__main__':
#   main()