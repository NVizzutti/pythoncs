from google.appengine.ext import db
class Result(db.Model):
  date = db.DateTimeProperty(auto_now=True)
  team = db.StringProperty()
  line = db.StringProperty()





 


    
