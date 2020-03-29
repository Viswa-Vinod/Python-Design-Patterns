import sys

class Colleague(object):
	def __init__(self, mediator, id):
		self._mediator = mediator
		self._id = id

	def getID(self):
		return self._id

	def send(self, msg):
		pass

	def receive(self, msg):
		pass

class ConcreteColleague(Colleague):
	def __init__(self, mediator, id):
		super().__init__(mediator, id)

	def send(self, msg):
		print("Message '" + msg + "' sent by Colleague " + str(self._id))
		self._mediator.distribute(self, msg)

	def receive(self, msg):
		print("Message '" + msg + "' received by Colleague " + str(self._id))


class Mediator:
	def add(self, colleague):
		pass

	def distribute(self, sender, msg):
		pass

class ConcreteMediator(Mediator):
	def __init__(self):
		Mediator.__init__(self)
		self._colleague = []	

	def add(self, colleague):
		self._colleague.append(colleague)

	def distribute(self, sender, msg):
		for colleague in self._colleague:
			if colleague.getID() != sender.getID():
				colleague.receive(msg)


def main():
	mediator = ConcreteMediator()
	vinod = ConcreteColleague(mediator, "Vinod")
	pras = ConcreteColleague(mediator, "Prasanna")
	shyam = ConcreteColleague(mediator, "Shyam")

	mediator.add(vinod)
	mediator.add(pras)
	mediator.add(shyam)

	vinod.send("Hello All")

if __name__ == "__main__":
	main()
