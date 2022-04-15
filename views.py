from django.shortcuts import render
from .models import *
import json

def main(request):
	도_광역시s = 도_광역시.objects.all()
	지역s = 지역.objects.all()
	재활센터s = 재활센터.objects.all()
	context = {'도_광역시':도_광역시s, '지역':지역s, '재활센터':재활센터s}
	return render(request, 'index.html', context)

def map(request):
	도_광역시s = 도_광역시.objects.all()
	지역s = 지역.objects.all()
	재활센터s = 재활센터.objects.all()
	context = {'도_광역시':도_광역시s, '지역':지역s, '재활센터':재활센터s}
	return render(request, 'map.html', context)

	

