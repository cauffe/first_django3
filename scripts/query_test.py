#!/usr/bin/env python

import csv
import sys
import os


sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
import django
django.setup()

from main.models import State, StateCapital, City

# print State.objects.all()
# print State.objects.filter(name__startswith="N")
# state = State.objects.get(pk=153)
# print state.abbrev
# states = State.objects.all().order_by('-pop')
# print states

# for state in states:
#     print state.name

# states = State.objects.all().exclude(name__contains='N')
# states = State.objects.all().exclude(name__icontains='N')

# for state in states:
#     print state.name

#states = State.objects.all().values('name', 'pop')
# for state in states:
#     print state

# states = State.objects.filter(name__startswith="N").values_list('name', 'abbrev', 'pk')

# for state in states:
#     print "State Name: %s, State Abbreviation: %s" % (state[0], state[1])

# states = State.objects.all().values_list('name', 'abbrev', 'pop')

# for name, abbrev, pop in states:
#     print "Name:{2}, Abbrev:{0}, Pop:{1}".format(abbrev, pop, name)

# states = State.objects.all().exclude(name__startswith='N').filter(pop__gte=500000).order_by('-pop').values_list('name', 'pop')

# print states

# for state in states:
#     #for objects
#     # print "%s %s" % (state.name, state.pop)
#     #for dictionaries using values('name', 'pop')
#     #print "%s %s" % (state['name'], state['pop'])
#     #for a list of list using values_list('name', 'pop')
#     print "%s %s" % (state[0], state[1])
# states_list = ['Texas', 'California', 'Nevada', 'Alaska']

# states = State.objects.filter(name__in=states_list)

# print states

# state = State.objects.get(name='Alabama')

# print state.statecapital_set.all()


# state = State.objects.get(pk=153)
# state2 = State.objects.get(pk=194)
# state3 = State.objects.get(pk=195)
# state4 = State.objects.get(pk=196)

# cap = StateCapital.objects.get(pk=1)
# cap2 = StateCapital.objects.get(pk=2)
# cap3 = StateCapital.objects.get(pk=3)

# # state.statecapital_set.remove(cap)
# cap.state.add(state)
# cap.state.add(state2)
# cap.state.add(state3)
# cap.state.add(state4)

# state.statecapital_set.add(cap)
# state.statecapital_set.add(cap2)
# state.statecapital_set.add(cap3)


# print state.statecapital_set.all()
# print cap.state.all()
# print "--------"
# print state.statecapital_set.all()

# states = State.objects.all()

# for state in states:
#     print "State:%s, Capital:%s" % (state.name, state.statecapital.name)

# states_list = ['Texas', 'Alabama', 'Alaska', 'Mars']

# for state in states_list:
#     try:
#         the_gotten_state = State.objects.get(name=state)
#         print "State found! %s" % the_gotten_state
#     except Exception, e:
#         print "State missing! %s" % e

# states = {
#           'state1':
#             {
#                 'name':'Texas', 
#                 'capital':'San Antonio'
#             }, 
#           'state2':
#             {
#                 'name':'California', 
#                 'capital':'Sacramento'
#             }
#         }

# for k, v in states.items():
#     for k, v in v.items():
#         print v


cities = City.objects.all()[:25]

for city in cities:
    print city








