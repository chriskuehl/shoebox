import json
import os

def get_repo(dir):
	if not os.path.isfile(config_path(dir)):
		return None

	repo = Repository(dir)
	repo.load_config()
	
	return repo

def config_path(dir):
	return "{}/shoebox".format(dir)

class Repository:
	format = "simple"
	__tags = set()

	def __init__(self, dir):
		self.dir = dir
	
	def __repr__(self):
		return "Repository(dir={})".format(self.dir)

	def init_defaults(self):
		DAY = 60 * 60 * 24

		self.__tags = {
				# tag name, time between snapshots, time to keep
				Tag(  "daily",        0,      7 * DAY),
				Tag( "weekly",  7 * DAY,     30 * DAY),
				Tag("monthly", 30 * DAY, 6 * 30 * DAY)}
	
	def write_config(self):
		config = self.config
	
	@property
	def config(self):
		pass

	def load_config(self):
		with open(self.config_path) as file:
			return json.load(file)
	
	@property
	def config_path(self):
		return config_path(self.dir)

	@property
	def tags(self):
		"""Returns all tags sorted by age"""
		return sorted(self.__tags, key=lambda tag: tag.age)


class Tag:
	"""A Tag which may be applied to an individual backup. Tags are
	applied to a backup based on the 'age' property of the tag. A new
	backup will be tagged with every tag for which the last backup
	stored with that tag is older than 'age'.

	title: human-readable tag title (short, lowercase, no spaces)
	age: time (in seconds) for which a backup is considered current
	keep: time (in seconds) before the tag should no longer apply to
	      a backup
	"""
	def __init__(self, title, age, keep):
		self.title = title
		self.age = age
		self.keep = keep
	
	def __repr__(self):
		return "Tag(title={}, age={}, keep={})".format(title, age, keep)
