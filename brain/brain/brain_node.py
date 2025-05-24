import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from custom_interface.srv import ComponentStatus


from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor


class brain_node(Node):

    def __init__(self):
        
        super().__init__("brain_node")
        self.callback_group = ReentrantCallbackGroup()



        self.detection_subscriber=self.create_subscription(String,"trash_detection",self.trash_detection_callback,10,callback_group=self.callback_group)



        self.component_status_client=self.create_client(ComponentStatus,"comonpont_status")
        while not self.component_status_client.wait_for_service(timeout_sec=1.0):
            if not rclpy.ok():
                self.get_logger().error('Interruped while waiting for the server.')
                return
            else:
                self.get_logger().info('Server not available, waiting again...')

        self.request=ComponentStatus.Request()

        self.componentStatusTimer=self.create_timer(5,self.send_component_status_request,callback_group=self.callback_group)


    

    def trash_detection_callback(self,msg):
       self.get_logger().info('I heard: "%s"' % msg.data)
       message = msg.data
       if "trash" in message:
           self.get_logger().info("Sending move request to actuator")
       else:
           self.get_logger().info("Sending no request to actuator")









    async def send_component_status_request(self):
      

      self.request.component = "camera"
      self.future = self.component_status_client.call_async(self.request)
      result = await self.future
      self.get_logger().info(f"Service response is:{result.status}")



        

    










        







def main(args=None):

    rclpy.init(args=args)
    brainNode = brain_node()

    executor = MultiThreadedExecutor()

    rclpy.spin(brainNode,executor)
    brain_node.destroy_node()
    brain_node.destroy_timer()
    rclpy.shutdown()

if __name__ == '__main__':
    main()















































# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import String
# from custom_interfaces.srv import ComponentStatus

# from rclpy.callback_groups import ReentrantCallbackGroup
# from rclpy.executors import MultiThreadedExecutor


# class BrainNode(Node):

#   def __init__(self):
#     super().__init__('brain_node')
    
#     self.trashDetectionTopic = self.declare_parameter(
#         "trashDetectionTopic",
#         "None"
#     )
#     self.componentStatusService = self.declare_parameter(
#         "componentStatusService",
#         "None"
#     )

#     self.get_parameter_values()
#     self.callback_group = ReentrantCallbackGroup()

#     self.trashDetectionSubscriber = self.create_subscription(
#         String,
#         self.trashDetectionTopic,
#         self.trash_detection_callback,
#         10,
#         callback_group=self.callback_group
#     )

#     self.componentStatusServiceTimer = self.create_timer(
#         5,
#         self.send_component_status_request,
#         callback_group=self.callback_group
#     )

#     self.componentStatusClient = self.create_client(
#         ComponentStatus, self.componentStatusService)
#     while not self.componentStatusClient.wait_for_service(timeout_sec=1.0):
#       self.get_logger().info('service not available, waiting again...')
#     self.request = ComponentStatus.Request()

#   def get_parameter_values(self):
#     self.trashDetectionTopic = self.get_parameter(
#         'trashDetectionTopic').get_parameter_value().string_value
#     self.componentStatusService = self.get_parameter(
#         'componentStatusService').get_parameter_value().string_value

#   def trash_detection_callback(self, msg):
#     self.get_logger().info('I heard: "%s"' % msg.data)
#     message = msg.data
#     if "trash" in message:
#       self.get_logger().info("Sending move request to actuator")
#     else:
#       self.get_logger().info("Sending no request to actuator")

#   async def send_component_status_request(self):
#     self.request.component = "camera"
#     self.future = self.componentStatusClient.call_async(self.request)
#     result = await self.future
#     self.get_logger().info(f"Service response is:{result.status}")


# def main(args=None):
#   rclpy.init(args=args)

#   brainNode = BrainNode()

#   executor = MultiThreadedExecutor()
#   rclpy.spin(brainNode, executor)
#   brainNode.destroy_node()
#   rclpy.shutdown()


# if __name__ == '__main__':
#   main()