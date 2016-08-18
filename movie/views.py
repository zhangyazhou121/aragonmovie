# -*- coding: utf-8 -*-
from django.shortcuts import render

import sqlite3
import sys
import json
from django.template import loader
from django.http import HttpResponse
from .models import movieinfo

reload(sys)
sys.setdefaultencoding('utf-8')

def index(request):
	template = loader.get_template('movie/index.html')
	movielist = movieinfo.objects.all().order_by('movie_rating')
	context = {'request': request, 'movielist': movielist}
	return render(request, 'movie/index.html', context)
