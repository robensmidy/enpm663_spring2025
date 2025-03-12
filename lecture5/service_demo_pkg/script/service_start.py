#!/usr/bin/env python3

import rclpy
from service_demo_pkg.service_demo_interface import HeatingService


def main(args=None):
    """
    Main function to initialize and run the ROS2 publisher node.

    Args:
        args (list, optional): Command-line arguments passed to the node. Defaults to None.
    """
    rclpy.init(args=args)
    node = HeatingService()
    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        # Log a message when the node is manually terminated
        node.get_logger().warn("Keyboard interrupt detected")
    finally:
        # Cleanly destroy the node instance
        node.destroy_node()
        # Shut down the ROS 2 Python client library
        rclpy.shutdown()



if __name__ == "__main__":
    main()  # Execute the main function when the script is run