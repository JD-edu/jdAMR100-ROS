import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    urdf = os.path.join(get_package_share_directory('jdamr100_description'), 'urdf', 'jdamr100.urdf')
  
    with open(urdf, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',),
        
			Node(
				package='robot_state_publisher',
				executable='robot_state_publisher',
				name='robot_state_publisher',
				output='screen',
				parameters=[{
				'use_sim_time': use_sim_time,
				'robot_description': robot_desc,
				'source_list': ['joint1', 'joint2'],
				'zeros': {
					'joint1': 1.5708,
					'joint2': 1.5708
				}
				}]
			),
			Node(
				package='jdamr100_description',
				executable='jdamr100',
				name='jdamr100',
				output='screen'
			
			),
			Node(
				package='rviz2',
				executable='rviz2',
				name='rviz2',
				output='screen',
				#arguments=['-d', os.path.join(get_package_share_directory('jdamr100_description'),'rviz','jdamr100_rviz.rviz')]
			),
   		])


if __name__ == '__main__':
    print(os.path.join(get_package_share_directory('jdam100_description'), 'urdf', 'jdamr100.urdf'))
    generate_launch_description()
