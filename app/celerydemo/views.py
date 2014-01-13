import datetime

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from celerydemo.tasks import do_something

def homepage(request):
    return HttpResponse("""
        <h1 style="text-align: center">Welcome to the sample Celery app!</h1>
        <h4 style="text-align: center">Click <a href="/sample_tasks/">here</a> to create some sample Celery tasks</h4>
    """)

@csrf_exempt
def sample_tasks_view(request, template_name="sampletasks.html"):
    if request.method == "GET":
        return render_to_response(template_name, context_instance=RequestContext(request))

    elif request.method == "POST":
        countdown = request.POST.get("countdown")
        if not countdown:
            countdown = 60
        try:
            countdown = int(countdown)
        except ValueError:
            messages.error(request, "Countdown needs to be an integer")
            return render_to_response(template_name, context_instance=RequestContext(request))

        task_id = do_something.apply_async(
            args=[],
            kwargs={"created_at": datetime.datetime.now()},
            countdown=countdown,
        )
        messages.success(request, "Task with countdown=%s seconds and id=%s created!" % (countdown, task_id))
        return render_to_response(template_name, context_instance=RequestContext(request))
