# 2025-02-27T15:35:31.604729
import vitis

client = vitis.create_client()
client.set_workspace(path="uarttest")

status = client.add_platform_repos(platform=["/home/test/uarttest"])

status = client.add_platform_repos(platform=["/home/test/uarttest"])

status = client.add_platform_repos(platform=["/home/test/uarttest/uart test.hw"])

status = client.add_platform_repos(platform=["/home/test/uarttest/uart test.cache"])

status = client.add_platform_repos(platform=["/home/test/uarttest/design_1_wrapper"])

status = client.add_platform_repos(platform=["/home/test/uarttest/design_1_wrapper"])

status = client.add_platform_repos(platform=["/home/test/uarttest/uart test.cache"])

status = client.add_platform_repos(platform=["/home/test/uarttest"])

proj = client.create_sys_project(name="system_project", platform="$COMPONENT_LOCATION/../design_1_wrapper.xsa", template="empty_accelerated_application")

proj = client.create_sys_project(name="system_project", platform="$COMPONENT_LOCATION/../design_1_wrapper.xsa", template="empty_accelerated_application")

proj = client.create_sys_project(name="uarttest", platform="$COMPONENT_LOCATION/../design_1_wrapper.xsa", template="empty_accelerated_application")

proj = client.create_sys_project(name="uarttest", platform="$COMPONENT_LOCATION/../design_1_wrapper.xsa", template="empty_accelerated_application")

proj = client.create_sys_project(name="system_project", platform="$COMPONENT_LOCATION/../design_1_wrapper.xsa", template="empty_accelerated_application")

proj = client.create_sys_project(name="system_project", platform="$COMPONENT_LOCATION/../design_1_wrapper.xsa", template="empty_accelerated_application")

vitis.dispose()

