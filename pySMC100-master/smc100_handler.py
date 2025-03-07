from pystages.smc100 import SMC100
from pystages import Vector

smc = SMC100(dev="/dev/ttyUSB0", addresses=[1])
smc.enter_leave_disable_state(1, False)

smc.home(wait=True)
smc.move_to(Vector(10))


print(smc.controller_address(1))
print(smc.get_error_and_state(1).state)
#smc.enter_configuration_state(2)


#smc.reset(1)