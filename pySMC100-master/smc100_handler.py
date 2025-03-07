from pystages.smc100 import SMC100
from pystages import Vector

smc = SMC100(dev="/dev/ttyUSB1", addresses=[1])
smc.home(wait=True)
print(smc.controller_address(1))
print(smc.get_error_and_state(1).state)
#smc.enter_configuration_state(2)

smc.move_to(Vector(10))
#smc.reset(1)