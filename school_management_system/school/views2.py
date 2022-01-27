from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .forms2 import *
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.urls import reverse

#=====================================================================
