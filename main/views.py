from django.shortcuts import render, render_to_response
from django.http import HttpResponse
# Create your views here.
from main.models import State, City
from django.template import RequestContext
from main.forms import ContactForm, CityEditForm
from django.core.mail import send_mail
from django.conf import settings


#list views
#detail views
#create view
#edit view
#delete view
#make the view --> make the url


def state_list(request):

    context = {}

    # states = State.objects.all()

    # context['states'] = states

    context['states'] = State.objects.all()

    #template -> context dictionary -> context_instance variable
    return render_to_response('state_list.html', context, context_instance=RequestContext(request))


def state_detail(request, pk):

    context = {}

    state = State.objects.get(pk=pk)

    context['state'] = state

    return render_to_response('state_detail.html', context, context_instance=RequestContext(request))


def state_search(request):

    context = {}

    context['request'] = request

    # context['get_vars'] = request.GET['a']

    # context['get_vars'] = request.GET.get('a', None)

    # state = request.GET.get('state', None)

    state = request.POST.get('state', None)
    
    if state != None:
        states = State.objects.filter(name__icontains=state)
    else:
        states = State.objects.all()

    context['states'] = states

    return render_to_response('state_search.html', context, context_instance=RequestContext(request))

def city_search(request):

    context = {}

    context['request'] = request

    city = request.GET.get('city', None)
    
    if city != None:
        cities = City.objects.filter(name__icontains=city)
    else:
        cities = City.objects.all()

    context['cities'] = cities

    return render_to_response('city_search.html', context, context_instance=RequestContext(request))


def city_detail(request, pk):

    context = {}

    city = City.objects.get(pk=pk)

    context['crazy_steve'] = city

    return render_to_response('city_detail.html', context, context_instance=RequestContext(request))


def city_create(request):

    context = {}

    context['request'] = request.method

    context['states'] = State.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name', None)
        county = request.POST.get('county', None)
        zip_code = request.POST.get('zip_code', None)
        latitude = request.POST.get('latitude', None)
        longitude = request.POST.get('longitude', None)
        state_id = request.POST.get('state', None)

        if state_id != None:
            state = State.objects.get(pk=state_id)
        else:
            state = State.objects.get(name='Texas')

        the_city, created = City.objects.get_or_create(name=name)

        the_city.county = county
        the_city.zip_code = zip_code
        the_city.latitude = latitude
        the_city.longitude = longitude
        the_city.state = state

        the_city.save()

        context['created'] = 'Operation Successful'

    elif request.method == 'GET':
        print "it was a GET request"

    return render_to_response('city_create.html', context, context_instance=RequestContext(request))


def city_edit(request, pk):

    context = {}

    city = City.objects.get(pk=pk)

    form = CityEditForm(request.POST or None, instance=city)

    context['city'] = city
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/state_list/')

    return render_to_response('city_edit.html', context, context_instance=RequestContext(request))


def contact_view(request):

    context = {}

    if request.method == 'POST':
        form = ContactForm(request.POST)
        context['form'] = form
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            send_mail('STATES SITE MESSAGE FROM %s' % name,
                      message,
                      email,
                      [settings.EMAIL_HOST_USER],
                      fail_silently=False
                      )
            context['message'] = "email sent"
        else:
            context['message'] = form.errors
    elif request.method == 'GET':
        form = ContactForm()
        context['form'] = form

    return render_to_response('contact_view.html', context, context_instance=RequestContext(request))





    