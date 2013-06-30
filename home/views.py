from django.http import HttpResponse, render

def displaySurvey(request, sid):
    queryRes = Survey.objects.filter(id=sid)
    if not len(queryRes) == 1:
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
