from django.http import HttpResponse
from celerydemo.tasks import create_poll

def create_poll_view(request):
    question = request.GET.get("question")
    if not question:
        question = "What is the airspeed velocity of an unladen swallow?"
    create_poll.apply_async(kwargs={"question": question}, countdown=60)
    return HttpResponse("HARRO!")
