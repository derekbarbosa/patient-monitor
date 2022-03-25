from celery import Celery

from mysite.myapi.models import User

app = Celery('tasks', broker='redis://localhost')

@app.task
def createUser(firstName, lastName):
    pass
    #User.firstName = firstName
    #User.lastName = lastName
