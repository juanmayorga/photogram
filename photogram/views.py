'''Photogran views'''

import json
from django.http import HttpResponse
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hello world its {now}'.format(now=now))


def sorted(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints
    }

    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')


def say_hi(request, name, age):
    if age < 12:
        message = 'sorry {}, you are not allowed here'.format(name)
    else:
        message = 'hello {}, wellcome'.format(name)
    return HttpResponse(message)
