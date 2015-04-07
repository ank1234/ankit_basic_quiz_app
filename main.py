#!/usr/bin/env python
# -*- coding: cp1252 -*-
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import time
import cgi
from gaesessions import get_current_session
html="""
<html>
  <head>
     <title>Information</title>
     <style>
body {
        background-color: yellow;
       
} 
 
</style>
 
  </head>
    <body>
        <h1>Details</h1>
         <p style="color:red">%s</p>
        <form method="post">
           <label for="firstName">First- Name:</label>
           <input name="firstName" type="text" value="%s"><br>

            <label for="lastName">Sir - Name: </label>
            <input name="lastName" type="text" value="%s"><br>

            <input name="" type="submit" value="send">
        </form>





    </body>


</html>


"""
html1="""
<html>
<head>
<title>Welcome </title>

</head>
<body bgcolor="blue">
<h1>Mr/Miss . Your Session has been started</h1>
<span id="countdown" class="timer"></span>
<script>
 
var seconds = 60;
function secondPassed() {
    var minutes = Math.round((seconds - 30)/60);
    var remainingSeconds = seconds % 60;
    if (remainingSeconds < 10) {
        remainingSeconds = "0" + remainingSeconds;  
    }
    document.getElementById('countdown').innerHTML = minutes + ":" + remainingSeconds;
    if (seconds == 0) {
        clearInterval(countdownTimer);
        document.getElementById('countdown').innerHTML = "Buzz Buzz......u can still check the answer but u failed";
    } else {
        seconds--;
    }
}
 
var countdownTimer = setInterval('secondPassed()', 1000);
</script>
 <form method="post">
           <label for="q1"> India’s largest MNC in 2011 in terms of turnover is:</label>
           <input name="q1" type="text" value="%s"><br><br><br><br>

            <label for="q2">What is the term used to describe long winded speeches in parliament to obstruct or delay a matter under consideration for voting: </label>
            <input name="q2" type="text" value="%s"><br><br><br><br><br>

            <input name="" type="submit" value="send">
        </form>


</body>




</html>






"""
html2="""
<html>
<head>

</head>
<body bgcolor="red">
<strong>.Its %s Answer.</strong>


</body>
</html>
"""
class MainHandler(webapp2.RequestHandler):
    def get(self):
        session = get_current_session()
        firstName =cgi.escape(session.get('firstName', ''),quote=True)
        lastName = cgi.escape(session.get('lastName', ''),quote=True)
        message= cgi.escape(session.get('message', ''),quote=True)
        self.response.out.write(html % (message,firstName,lastName))
    def post(self):
        firstName = self.request.get("firstName")
        lastName = self.request.get("lastName")
        session = get_current_session()
        session['firstName'] = firstName
        session['lastName']= lastName
        session['message'] = ''
        if len(firstName) < 2 or len(lastName) < 2:
          session['message'] = "Firstname and Lastname are mandatory "
          self.redirect("/")
        else:
            self.redirect("/second")
class a(webapp2.RequestHandler):
    def get(self):
        session = get_current_session()
        q1 =cgi.escape(session.get('q1', ''),quote=True)
        q2 = cgi.escape(session.get('q2', ''),quote=True)
        self.response.out.write(html1)
    def post(self):
        q1 = self.request.get("q1",'')
        q2 = self.request.get("q2",'')
        session = get_current_session()
        if q1=="maruti suzuki" and q2=="fillibuster":
            self.response.out.write(html2 % ("correct Answers :)" ))
        else:
            self.response.out.write(html2 % ("wrong Answer :("))
    
        

           
           

app = webapp2.WSGIApplication([
    ('/', MainHandler),('/second', a)
    
], debug=True)

