# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request, *args, **kwargs ):
    context = {}
    return render_to_response('base.html', context,
                              context_instance=RequestContext(request))

