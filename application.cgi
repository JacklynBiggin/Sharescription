#!C:/Users/Jerry/Documents/Python/Scripts/python.exe
from wsgiref.handlers import CGIHandler
from index import app
CGIHandler().run(app)