#from django.template.loader import get_template
from django.http import HttpResponse
#from django.template import Template, Context
from django.shortcuts import render
import datetime
def hello(request):
    return HttpResponse("Hello world")

#def current_datetime(request):
#    now = datetime.datetime.now()
#    fp = open('/Users/kunal.chelani/Desktop/myvirtualenv/mysite/mysite/mytemplate.html')
##    t = Template("<html><body>It is now {{ current_date }}.</body></html>")
#    t = Template(fp.read())
#    fp.close()
##    html = "It is now %s. " % now
#    c = Context({'current_date': now})
#    html = t.render(c)
#    return HttpResponse(html)

#def current_datetime(request):
#    now = datetime.datetime.now()
#    t = get_template('mytemplate.html')
#    c = Context({'current_date': now})
#    html = t.render(c)
#    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'mytemplate.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hour(s), it will be  %s." % (offset, dt)
    return HttpResponse(html)

def dummy_view(request):
    return render(request, 'mainpage.html', {'name': "Kunal"})
