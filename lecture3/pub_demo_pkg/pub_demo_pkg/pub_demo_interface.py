from rclpy.node import Node
from std_msgs.msg import String


class PubDemoInterface(Node):
    """
    A ROS2 publisher node that sends string messages to the 'leia' topic at 0.5-second intervals.

    The messages contain a fixed message, which demonstrates a simple way to publish data continuously in ROS2.

    Attributes:
        _publisher (Publisher): The ROS2 publisher object for sending messages.
        _timer (Timer): A timer object that triggers the publishing event every 1 second.
        _msg (String): A `std_msgs/msg/String` message that holds the data to be published.

    Args:
        node_name (str): The name of the node.
    """

    def __init__(self, node_name):
        """
        Initializes the publisher node, creates a publisher for the 'leia' topic, and starts a timer to publish messages every second.

        Args:
            node_name (str): The name of the node, passed to the parent Node class.
        """
        super().__init__(node_name)
        # Create a publisher object for the 'leia' topic with a queue size of 10.
        self._leia_pub = self.create_publisher(String, "leia", 10)
        # Create a timer that calls `leia_timer_cb` every second.
        self._leia_timer = self.create_timer(0.5, self.leia_timer_cb)
        
        self._string_msg = String()

    def leia_timer_cb(self):
        """
        Callback function for the timer event. This function constructs the message to be published,
        and logs the message to the ROS2 logger.

        The message format is "Help me Obi-Wan Kenobi, you are my only hope", demonstrating
        a simple message pattern.
        """
        # Set the message data.
        self._string_msg.data = "Help me Obi-Wan Kenobi, you are my only hope"
        # Publish the message.
        self._leia_pub.publish(self._string_msg)
        # Log the message being published.
        self.get_logger().info(f"Publishing: {self._string_msg.data}")