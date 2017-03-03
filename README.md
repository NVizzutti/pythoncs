##Old Python 
####(2009)
This code was written by me in college when I was beginning to learn programming for the first time. There are two console games hangman and mastermind, as well as a small application that calculated point spreads for basketball. This code hasn't been refactored, but did help me reacquaint with python once I was more skilled in OOP. 

##Handicapper 
This small web application was the first actual application I built. It was developed completely in python and HTML, using Django. It was originally deployed on google app engine but has since been deleted when it became a paid service. 

```Python
class MainPage(webapp.RequestHandler):
  def get(self):
      user = users.get_current_user()
      nickname = user.nickname()
      template_values={'user':nickname}
      path = os.path.join(os.path.dirname(__file__),'index.html')
      self.response.out.write(template.render(path,template_values))
 
class teamHandler(webapp.RequestHandler):
  def get(self):
      user = users.get_current_user()
      nickname = user.nickname()
      sess = sessions.Session()
      TeamA=self.request.get('TeamA')
      TeamB=self.request.get('TeamB')
      sess['teamA']=TeamA
      previous = db.GqlQuery("Select * from Result")
      # set up template value
      template_values={'TeamA': TeamA,'TeamB':TeamB,'user':nickname,'previous':previous}
      path = os.path.join(os.path.dirname(__file__),'input.html')
      self.response.out.write(template.render(path,template_values))
```
      
The application handled user sessions and would allow users to input team data and basketball statistics to calculaute a point spread and win percentage prediction. 
(never was quite accurate enough to get me rich though, guess I needed to incorporate machine learning)

###Hangman 
Hangman was built as a console game and then adapted later for the web using some minimal controller logic and images to represent gameplay. 

###Mastermind 
The classic game in the console, easy for a beginner to create. 
 
