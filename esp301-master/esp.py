import serial

class esp:
	def __init__(self, dev="/dev/ttyUSB0", b=19200,axis=1,reset=True, initpos = 0.0,useaxis=[]):

		self.dev = serial.Serial(
			port=dev,
			baudrate=b,
			bytesize=serial.EIGHTBITS,
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE,
			timeout=1,
			dsrdtr=False,
			rtscts=False,
			xonxoff=False
		)

		self.inuse = useaxis
		if(len(self.inuse)==0):
			self.inuse = [axis]
		self.defaxis = axis

		if(reset):
			for n in self.inuse:

				self.reset(n)
				r = self.check_errors()
				if(r!=0):
					print("Error while setting up controller, error # %d"%r)
				if(initpos!=0):
					self.setpos(initpos)
					r = self.check_errors()
					if(r!=0):
						print("Error while setting up controller, error # %d"%r)

	def reset(self,axis):
		self.dev.write(b"%dOR;%dWS0\r"%(axis,axis))
	
	def check_errors(self):
		self.dev.write(b"TE?\r")
		return len(self.dev.readline().decode("utf-8"))

	def getpos(self,axis=None):
		a = self.defaxis
		if(axis and axis>0):
			a = axis
		self.dev.write(b"%dTP\r"%a)
		return float(self.dev.readline().decode("utf-8"))
	
	def setpos(self,pos,axis=None):
		a = self.defaxis
		if(axis and axis>0):
			a = axis
		print("setting to %f"%pos)
		self.dev.write(b"%dPA%.4f;%dWS1;%dTP\r"%(a,pos,a,a))
		# return float(self.dev.readline().decode("utf-8"))

	def position(self,pos=None,axis=None):
		if(isinstance(pos,(float,int))):
			self.setpos(pos,axis)
			self.getpos()
			self.setpos(pos,axis)
		return self.getpos(axis)

axis1 = esp(dev="/dev/ttyUSB1", axis=1)

axis1.setpos(100, 1)
axis1.setpos(-100, 1)
axis1.reset(1)


axis2 = esp(dev="/dev/ttyUSB1", axis=2)
axis2.setpos(100, 2)
axis2.setpos(-100, 2)
axis2.reset(2)
axis3 = esp(dev="/dev/ttyUSB1", axis=3)
axis3.setpos(200, 3)
axis3.setpos(-200, 3)
axis3.reset(3)

