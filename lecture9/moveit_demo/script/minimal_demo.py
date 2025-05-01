#!/usr/bin/env python3

from rclpy.executors import MultiThreadedExecutor
from moveit_demo.minimal_demo import RobotController
import rclpy

def main(args=None):
    rclpy.init(args=args)
    node = RobotController()
    
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    
    try:
        executor.spin()
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down from keyboard interrupt")
    finally:
        # Cleanup resources properly
        if "node" in locals() and rclpy.ok():
            executor.shutdown()
            node.destroy_node()
        # Only call shutdown if ROS is still initialized
        if rclpy.ok():
            rclpy.shutdown()
        
if __name__ == '__main__':
    main()