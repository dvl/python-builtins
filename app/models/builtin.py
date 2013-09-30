from app import db

class Builtin(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	function = db.Column(db.String(80))
	help_text = db.Column(db.Text)

	def __init__(self, function, help_text):
		self.function = function
		self.help_text = help_text

	def __repr__(self):
		return '<Builtin %r>' % (self.function,)