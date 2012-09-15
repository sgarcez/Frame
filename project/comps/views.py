from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from comps.forms import CompForm
from comps.frame import Comp
from comps.models import Device

def test(request, *args, **kwargs ):
    context = {}
    if request.method == 'POST':
        form = CompForm(request.POST, request.FILES)
        if form.is_valid():
            device = Device.objects.get(id=form.data['device'])
            c = Comp(request.FILES['image'], device.overlay_image, (device.screen_x, device.screen_y), 
                    'white')
            comp = c.build()
            # comp.show()
            
            import StringIO
            output = StringIO.StringIO()
            comp.save(output, format='png')
            contents = output.getvalue().encode('base64')
            context['image'] = contents
            output.close()
            
            # import ipdb; ipdb.set_trace()
    else:
        form = CompForm() # An unbound form

    context['form'] = form
    return render_to_response('test_form.html', context,
                              context_instance=RequestContext(request))
    

