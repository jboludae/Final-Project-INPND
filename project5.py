# We first import all the libraries we will neeed
import webapp2
import jinja2
import os

# We import the ndb
from google.appengine.ext import ndb

# This code initializes a Jinja environment
# Autoescape = True "escapes" any html character by default
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = False)

# We build a Concept class, so all concepts in our notes will go here
# the properties names should be self-explanatory

class Concept(ndb.Model):
	stage = ndb.StringProperty(indexed = True)
	title = ndb.StringProperty(indexed = True)
	explanation = ndb.StringProperty(indexed = False)
	date = ndb.DateTimeProperty(auto_now_add = True)

# We now build a Comment class, so users can input their comments
# properties names should also be self explanatory

class Comment(ndb.Model):
	stage = ndb.StringProperty(indexed = True)
	title = ndb.StringProperty(indexed = True)
	name = ndb.StringProperty(indexed = True)
	explanation = ndb.StringProperty(indexed = False)
	date = ndb.DateTimeProperty(auto_now_add = True)

# This code automatically cleans the database and uploads my updated notes
# It will be used each time I want to update my notes and then I will comment
# it out. A script named my_notes.pyc are also include in the
# project directory.

# we clean de notes database
concepts_query = Concept.query()
concepts = concepts_query.fetch()
for concept in concepts:
	concept.key.delete()

# and now we upload the notes
import my_notes
notes = my_notes.notes_list
for note in notes:
	concept = Concept(stage = note[0],
		title = note[1],
		explanation = note[2])
	concept.put()

# We now write a helper handler that will help to simplify our code:
class Handler(webapp2.RequestHandler):
	def write(self, *a, **ka):
		#this is a helper function that allows us to write more concise code
		self.response.out.write(*a,**ka)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

# This will be the main page handler. It will display our main page.

class MainPage(Handler):
	def get(self):
		self.render("mainpage.html")

# This is the "Stages" handler. The code here selects the notes and comments
# from the selected stage and displays them

class Stages(Handler):
	def get(self):
		# This retrieves all concepts posted in the "Concept" class ordered by date
		# for the selected stage. First concepts are displayed first
		# we programm defensively, so no user can introduce junk in the server
		# using the query parameters. If a user does this, he will be directed to
		# the main page
		stage = self.request.get('Stage')
		valid_stages = ["Stage 0", "Stage 1", "Stage 2", "Stage 3", "Stage 4", "Stage 5","Random Stuff"]
		if stage in valid_stages:
			concept_query = Concept.query( Concept.stage == stage).order(Concept.date)
			concepts = concept_query.fetch()
			# This retrieves all comments posted in the "Comment" class ordered by date
			# for the selected stage. Last comments are displayed first.
			comment_query = Comment.query( Comment.stage == stage).order(-Comment.date)
			comments = comment_query.fetch()
			self.render("stage1.html", concepts = concepts, comments = comments, stage = stage)
		else:
			self.redirect('/')

# This handler is used to input comments

class Input_Comments(Handler):
	def post(self):
		# We first get all the inputs in the form
		name = self.request.get('name').strip()
		title = self.request.get('title').strip()
		explanation = self.request.get('explanation').strip()
		stage = self.request.get('stage')
		# It is required to insert a title a name and an explanation. So we
		# initialize a blank error message. In case one of the three inputs is missing
		# we will set error_message = 'Please fill out all the required fields!' so it
		# will be displayed
		error_message = ''
		# We instantiate a concept using the 4 variables above
		# we write it in the Datastore
		if title and name and explanation:
			comment = Comment(stage = stage,
				title = title,
				name = name,
				explanation = explanation)
			# This code actually upload "comment" to the database
			comment.put()
			# This code will redirect us to the main page
			self.redirect('/Notes?Stage='+stage)
		else:
			# If title, name or explanation are missing, we will be asked to resubmit
			# the form. error.html will keep us in the /Input_Comments URL until we
			# complete the content for title, name and explanation
			error_message = 'Please fill out all the required fields!'
			self.render("error.html", name = name, title = title, explanation = explanation, stage = stage, error_message = error_message)

# This handler is used to delete comments

class Delete_Comments(Handler):
	def post(self):
		# We first get the title of the notes we want to delete
		title = self.request.get('title')
		stage = self.request.get('stage')
		comment_query = Comment.query(Comment.title == title)
		# This code fetches the document and returns a list of comments
		# This is not optimal, but we delete only the first comment in the list
		# In a serious website the user should only be able to delete the comments
		# inserted by him/her
		comment = comment_query.fetch()
		if len(comment)>0:
			comment[0].key.delete()
		self.redirect('/')

# And finally, the standard URL - handler mapping

app = webapp2.WSGIApplication([('/',MainPage),
	('/Notes',Stages),
	('/InputComments', Input_Comments),
	('/DeleteComments', Delete_Comments)
	], debug = True)
