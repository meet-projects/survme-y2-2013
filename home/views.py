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
    def getLatestFive():
        return sorted(Survey.objects.all(), reverse=True)[:5]
    def getPopularFive():
        pass
    context = {"recentFeed":getLatestFive()}
    return render(request, "home.html", context)
