from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.utils.decorators import method_decorator
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseNotFound


from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer


from webscrape.application.models import *
from webscrape.application.responses import *

from webscrape.application.services import *



class NiftyGainers(viewsets.ViewSet):

	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'application/listings.html'

	def list(self, request, *args, **kwrgs):

		try:
			result = NiftyGainersService.retrieve()

			if result.get('success'):
				data = result.get('data')
			else:
				data = list()

			return Response({'data': data})

		except Exception as e:
			raise e

	def retrieve(self, request, *args, **kwrgs):

		try:
			result = NiftyGainersService.filter()

			if result.get('success'):
				data = result.get('data')
			else:
				data = list()

			return Response({'data': data}, template_name='application/lists.html')

		except Exception as e:
			raise e
