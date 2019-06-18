from flask import Flask
from  .config  import DevConfig
#intializing application

app = Flask(__name__)

#Setting up configurations
app.config.from_object(DevConfig)


from list import views