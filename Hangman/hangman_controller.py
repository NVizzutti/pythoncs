import os
import cgi
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext.webapp.util import run_wsgi_app
import sessions
import hangman

class MainPage(webapp.RequestHandler):
    def get(self):
        sess = sessions.Session()
        maker=sess['maker']
        sess['maker']=hangman.genSecret()
        sess['guesscode']=[]
        sess['wrong']=0
                display="Guess"        
        secretCode=""
        while len(secretCode)<len(maker):
            secretCode=secretCode+'0'
        sess['secretCode']=secretCode
        image="/images/1.png"
        template_values={'picHang':image, 'display':display, 'Code':str(maker),'secretCode':str
(secretCode)}
    

        
        path = os.path.join(os.path.dirname(__file__),'index.html')
        self.response.out.write(template.render(path,template_values))

class MMController(webapp.RequestHandler):
    def get(self):
        sess=sessions.Session()
        maker=sess['maker']
        secretCode=sess['secretCode']    
        wrong=sess['wrong']    
        guesscode=sess['guesscode']
        nowGuess=str(self.request.get('letter'))
        if maker==None:
            maker=hangman.genSecret()
            sess['maker']=maker
        i=0
        match=False
        while i<len(maker):
            if nowGuess in guesscode:
                display="You have already guessed that letter..."
                match=True
            elif nowGuess==maker[i]:
                secretCode=secretCode[0:i]+nowGuess+secretCode[i+1:len(secretCode)]
                sess['secretCode']=secretCode
                match=True
            i=i+1
        if not match:    
            wrong=wrong+1
        if wrong==0:
            image='/images/1.png'        
        if wrong==1:
            image='/images/2.png'
        if wrong==2:
            image='/images/3.png'
        if wrong==3:
            image='/images/4.png'
        if wrong==4:
            image='/images/5.png'
        if wrong==5:
            image='/images/6.png'
        if wrong==6:
            image='/images/7.png'
        if wrong==7:
            image='/images/8.png'
        if wrong==8:
            image='/images/9.png'
        if wrong==9:
            image='/images/10.png'
        if wrong==10:
            image='/images/11.png'
            

        sess['wrong']=wrong
                #win        
        if maker==secretCode:
            display="You Won! Congratulations!"
        elif wrong==10:
            display="YOU KILLED YOURSELF!"
            secretCode=maker
        elif nowGuess in guesscode:
            display="DUPLICATE LETTER. Guess Again."
        else:
            guesscode.append(nowGuess)
            sess['guesscode']=guesscode        
            display="Guess your next letter: "
        template_values= {'guess':str(guesscode), 'Code':str(maker), 'guesscode':guesscode, 'display':display, 'picHang':image, 'secretCode':str(secretCode)}


        path = os.path.join(os.path.dirname(__file__),'index.html')
        self.response.out.write(template.render(path,template_values))

class NewGameController(webapp.RequestHandler):
    def get(self):
        sess = sessions.Session()
        sess['maker']=hangman.genSecret()
        maker=sess['maker']
        sess['wrong']=0
        sess['guesscode']=[]
        display="Guess next letter"
        secretCode=""
        while len(secretCode)<len(maker):
            secretCode=secretCode+'*'
        sess['secretCode']=secretCode
        image="/images/1.png"
        template_values={'picHang':image, 'display':display, 'Code':str(maker),'secretCode':str(secretCode)}
        path = os.path.join(os.path.dirname(__file__),'index.html')
        self.response.out.write(template.render(path,template_values))



application = webapp.WSGIApplication(
                    # MainPage handles the home load
                                     [('/', MainPage),
                                      ('/newgame',NewGameController),
                                      ('/on_guess', MMController)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
