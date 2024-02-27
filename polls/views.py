from django.http import HttpResponse

def detail(requestion,question_id):
    return HttpResponse("You are looking at question %s. %question_id")

def result(request, question_id):
    response = "You are looking at the result of the question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)