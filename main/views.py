from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from datetime import date
from datetime import datetime
from datetime import timedelta

# from .forms import AppointmentCreateFormDoctor
# from .forms import AppointmentCreateFormModerator
# from .forms import AppointmentCreateFewForm
#from .models import Appointment
# from .models import Moderator
# from .models import Doctor
# from .models import Customer

# TODO: Do refactor. Move excessive code to business_logic.


def index(request):
    return render(request, 'index.html')