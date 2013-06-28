from django.http import HttpResponse

def displaySurvey(request, id):
    return HttpResponse("Survey id: " + str(id))
