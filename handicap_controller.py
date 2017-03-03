import handicapfunc
import cgi
import os
import math
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import model
import sessions

# main page appears on load
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

class statsHandler(webapp.RequestHandler):
  def get(self):
      user = users.get_current_user()
      logout = users.create_logout_url('/')
      nickname = user.nickname()
      sess = sessions.Session()
      TeamA=sess['teamA']
      #calculations for stats
      PPG1=self.request.get('PPG1')
      PA1=self.request.get('PA1')	
      FGP1=self.request.get('FGP1')
      PPG2=self.request.get('PPG2')	
      PA2=self.request.get('PA2')	
      FGP2=self.request.get('FGP1')
      PPG1=float(PPG1)
      PA1=float(PA1)
      FGP1=float(FGP1)
      PPG2=float(PPG2)
      PA2=float(PA2)
      FGP2=float(FGP2)
      X=handicapfunc.calcPoints(PPG1,PA1,FGP1)
      Y=handicapfunc.calcPoints(PPG2,PA2,FGP2)	
      X=float(X)
      Y=float(Y)
      winStat=handicapfunc.winStat(X,Y)
	#calculations for ratings
      CA=self.request.get('CA')
      GI=self.request.get('GI')
      SA=self.request.get('SA')
      HC=self.request.get('HC')
      BP=self.request.get('BP')
      I=self.request.get('I')
      TE=self.request.get('TE')
      TM=self.request.get('TM')
      SI=self.request.get('SI')
      HH=self.request.get('HH')
      CA=float(CA)
      GI=float(GI)
      SA=float(SA)
      HC=float(HC)
      BP=float(BP)
      I=float(I)
      TE=float(TE)
      TM=float(TM)
      SI=float(SI)
      HH=float(HH)
      winRank=handicapfunc.winRank(CA,GI,SA,HC,BP,I,TE,TM,SI,HH)
      Final1=(winRank+winStat)/2
      Final2=round(Final1,2)
      Final=math.fabs(Final2)
      Line1=handicapfunc.getLine(Final)
      Line='%.1f' % Line1
      result = model.Result()
      LineString = TeamA + ' ' + Line
      result.line=str(LineString)
      result.put()
      previous = db.GqlQuery("Select * from Result")
       #set up template value
      template_values={'WinPercentStat':winStat,'WinPercentRank':winRank,'WinPercentFinal':Final,'Line':Line, 'previous' : previous,'final':Final,'TeamA':TeamA,'user':nickname,'logout':logout}
      path = os.path.join(os.path.dirname(__file__),'result.html')
      self.response.out.write(template.render(path,template_values))



# create this global variable that represents the application and specifies which class
# should handle each page in the site
application = webapp.WSGIApplication(
					# MainPage handles the home page load
                                     [('/', MainPage),
				      ('/team', teamHandler),
				      ('/stats', statsHandler)
                                     ],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
