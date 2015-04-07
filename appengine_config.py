from gaesessions import SessionMiddleware

# Original comments deleted ... 
# Create a random string for COOKIE_KDY and the string has to
# be permanent. "os.urandom(64)" function may be used but do
# not use it *dynamically*.
# For me, I just randomly generate a string of length 64
# and paste it here, such as the following:

COOKIE_KEY = "ppb52adekdhD25dqpbKu39dDKsdrfergergegegrrgrgr"

def webapp_add_wsgi_middleware(app):
   # from google.appengine.ext.appstats import recording
    app = SessionMiddleware(app, cookie_key=COOKIE_KEY)
    #app = recording.appstats_wsgi_middleware(app)
    return app
