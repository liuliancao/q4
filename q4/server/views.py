from django.shortcuts import render
from django.views.decorators.http import require_POST
from jfu.http import upload_receive, UploadResponse, JFUResponse
from django.conf import settings
from django.core.urlresolvers import reverse
from q4.server.models import Host, Purchase
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import decorators
import os
from django.views import generic
from configparser import ConfigParser


# Create your views here.
def server_index(request):
    return HttpResponse('index')


def purchase(request):
    if request.method == 'GET':
        try:
            applicant = request.get('applicant', 'null')
            product = request.get('product', 'null')
            idc = request.get('idc', 'null')
            cost_centre = request.get('cost_centre', 'null')
            ticket = request.get('ticket ', 'null')
            allocation = request.get('allocation ', 'null')
            number = request.get('number ', 'null')
            apply_type = request.get('apply_type ', 'null')
            cmdb_type = request.get('cmdb_type ', 'null')
            cmdb_from = request.get('cmdb_from ', 'null')
            cmdb_to = request.get('cmdb_to ', 'null')
            reason = request.get('reason ', 'null')
            desc = request.get('desc ', 'null')
            state = request.get('state', 'null')
            purch = Purchase(applicant=applicant,
                             product=product,
                             idc=idc,
                             cost_centre=cost_centre,
                             ticket=ticket,
                             allocation=allocation,
                             number=number,
                             apply_type=apply_type,
                             cmdb_type=cmdb_type,
                             cmdb_from=cmdb_from,
                             cmdb_to=cmdb_to,
                             reason=reason,
                             desc=desc,
                             state=state
                             )
            return HttpResponse('add successfully')
        except Exception as e:
            print(str(e))
            return HttpResponse('add failed error:\n'+str(e))
    else:
        return HttpResponse('do not accept the method')
