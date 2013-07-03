from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from models import Survey, Answer, Comment
import json

def percent(list):
    arr = []
    total = sum(list)
    for i in range(len(list)):
        p = 0.0
        if total != 0:
            p = (1.0 * list[i] / total)*100
        arr.append(float(str("%.2f" % p)))
    return arr

def votes_dic(answers):
    res = {}
    for a in answers:
        res[a.text] = a.votes
    return res
        
def displaySurvey(request, sid):
    queryRes = Survey.objects.filter(id=sid)
    if not len(queryRes) == 1:
        # survey doesnt exist
        context = {"id":-1}
        return render(request, "displaysurvey.html", context)
    survey = queryRes[0]
    answers = Answer.objects.filter(survey=sid)
    comments = Comment.objects.filter(survey=sid)
    JSON = {}
    JSON['categories'] = [(answer.text) for answer in answers]
    JSON['votes'] = votes_dic(answers)
    JSON['percent'] = percent([(answer.votes) for answer in answers])
    context = {
        "poll":survey,
        "answers":answers,
        "comments":comments,
        # ohai ron python encodes python dictionaries into json nicely so you don't have to fuck with curly braces etc. <3 <3 <3
        "JSON": json.dumps(JSON) 
        }
    return render(request, "displaysurvey.html", context)

def handleVote(request, sid):
    choice = int(unicode(request.POST['answers']))
    answers = Answer.objects.filter(survey=sid)
    answer = answers[choice-1]
    answer.votes += 1
    answer.save()
    return HttpResponseRedirect('/survey/' + str(sid))

def handleComment(request, sid):
    new_text = unicode(request.POST['text'])
    new_author = unicode(request.POST['author'])
    queryRes = Survey.objects.filter(id=sid)
    if len(queryRes) == 1:
        sur = queryRes[0]
        comment = Comment(survey=sur, text=new_text, author=new_author)
        comment.save()
    return HttpResponseRedirect('/survey/' + str(sid))

def createSurvey(request):
    context = {}
    return render(request, "newsurvey.html", context)

def handleForm(request):
    new_title = request.POST['title']
    new_author = request.POST['author']
    new_desc = request.POST['desc']
    answers = []
    for i in range(1, 20):
        input_name = "answer" + str(i)
        if input_name in request.POST:
            answers.append(request.POST[input_name])
    new_survey = Survey(title=new_title, author=new_author, desc=new_desc)
    new_survey.save()
    for answer in answers:
        new_answer = Answer(survey=new_survey, text=answer, votes=0)
        new_answer.save()
    return HttpResponseRedirect('/survey/' + str(new_survey.id))

def homepage(request):
    def getLatestFive():
        objects = Survey.objects.order_by('id')
        objects.reverse()
        return objects[:5]
    def getPopularFive():
        objects = Answer.objects.all()
        votes = {}
        for answer in objects:
            if answer.survey in votes:
                votes[answer.survey] += answer.votes
            else:
                votes[answer.survey] = answer.votes
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
