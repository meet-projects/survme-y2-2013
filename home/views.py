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
        objects = Answer.objects.all()
        votes = {}
        for answer in objects:
            if answer.survey in votes:
                vote[answer.survey] += answer.votes
            else:
                vote[answer.survey] = answer.votes
        return sorted(votes, key=votes.get, reverse=True)[:5]
    context = {"recentFeed":getLatestFive(), "popularFeed":getPopularFive()}
    return render(request, "home.html", context)

def browse(request):
    all_surveys = Survey.objects.all()
    for survey in all_surveys:
        answers = Answer.objects.filter(survey=survey.id)
        votecount = 0
        for answer in answers:
            votecount += answer.votes
        survey.totalvotes = votecount
    context = {"surveys":all_surveys}
    return render(request, "browse.html", context)
