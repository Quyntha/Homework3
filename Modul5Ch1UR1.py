class String:
	def __get__(self, instance, owner):
		return instance.text

	def __set__(self, instance, value):
		instance.text = value

class StringVar:
	string = String()

	def __init__(self, text):
		self.text = text

control = StringVar('some text')
control.string = 'new text'