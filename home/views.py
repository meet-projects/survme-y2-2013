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
