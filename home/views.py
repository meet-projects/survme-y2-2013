from django.http import HttpResponse
from django.shortcuts import render
from models import Survey, Answer


def displaySurvey(request, sid):
    queryRes = Survey.objects.filter(id=sid)
    if not len(queryRes) == 1:
        # survey doesnt exist
        context = {"id":-1}
        return render(request, "displaysurvey.html", context)
    survey = queryRes[0]
    surveyAnswers = Answer.objects.filter(survey=sid)
    context = {
        "id":survey.id,
        "title":survey.title,
        "desc":survey.desc,
        "answers":surveyAnswers,
        "author":survey.author,
        "display":survey.display,
        "public":survey.public
        }
    return render(request, "displaysurvey.html", context)

def createSurvey(request, id):
    return HttpResponse("Create survey page")

def homepage(request):
    queryRes = Survey.objects.all()
    context = { }
    return render(request, "home.html", context)


----

from django.http import HttpResponse
from django.shortcuts import render
from home.models import *
def displaySurvey(request, id):
    queryRes = Survey.objects.filter(id=id)
    if not len(queryRes) == 0:
        # survey doesnt exist
        pass
    survey = queryRes[0]
    queryRes = Answer.objects.filter(survey=sid)
    surveyAnswers = []
    for answer in queryRes:
        surveyAnswers.append((survey.text, survey.votes))
    context = {
        "id":survey.id,
        "title":survey.title,
        "desc":survey.desc,
        "answers":surveyAnswers,
        "author":survey.author,
        "display":survey.display,
        "public":survey.public
        }
    return render(request, "displaysurvey.html", context)

def createSurvey(request, id):
    return HttpResponse("Create survey page")
 
