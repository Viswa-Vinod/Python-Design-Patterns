class AtmState():

	name = "state"
	allowed = []

	def goNext(self, state):
		if state.name in self.allowed:
			print("Current State: ", self, " switched to: ", state.name)
			self.name = state.name
			self.allowed = state.allowed

		else:
			print("Current State: ", self, " switching to: ", state.name, " not possible!")

	def __str__(self):
		return self.name

class Off(AtmState):

	name = "off"
	allowed = ['on']

class On(AtmState):
	name = "on"
	allowed = ["off"]
		

class ATM():
	
	def __init__(self):
		self.state = On()

	def setState(self, state):
		self.state.goNext(state)

def main():
	atm = ATM()
	# print(atm.__str__())
	atm.setState(Off())
	# print(atm.__str__())
	atm.setState(Off())
	atm.setState(On())
	

if __name__ == "__main__":
	main()
