#!/usr/bin/env python3

import rclpy
from rclpy.executors import MultiThreadedExecutor
from executor_demo_pkg.executor_demo_interface import DualMutuallyExclusiveInterface


def main(args=None):
    rclpy.init(args=args)
    node = DualMutuallyExclusiveInterface("dual_mutually_exclusive_demo")

    # Use a MultiThreadedExecutor to allow callbacks in different groups to run concurrently
    executor = MultiThreadedExecutor()
    executor.add_node(node)

    try:
        executor.spin()
    finally:
        executor.shutdown()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()