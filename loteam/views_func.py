import pandas as pd
import datetime
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

from tablib import Dataset


def test2(request):
    print(request.GET)