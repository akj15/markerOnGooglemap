import json
from django.shortcuts import render
from django.views.generic import View
from .forms import PointOfInterestForm
from .models import PointOfInterest, Country
from django.http import HttpResponse


class IndexView(View):
	template_name = 'gapp/map.html'

	def get(self, request, *args, **kwargs):
		data = PointOfInterest.objects.all()[0]
		form = PointOfInterestForm(instance=data)
		zone = PointOfInterest.objects.all()
		options = Country.objects.all()
		name_list = PointOfInterest.objects.values_list("pk", "address", "position")
		name_list_json = json.dumps(list(name_list))
		return render(request, self.template_name, {'name_list_json': name_list_json, 'options': options, 'form': form, 'data': data, 'zone':zone})
		
	def post(self, request, *args, **kwargs):
		select_id = request.POST['id']
		country = Country.objects.get(id=int(select_id))
		print select_id
		print country.name
		if country.name == '--all--':
			zone = PointOfInterest.objects.values_list("pk", "address", "position")
		else:
			zone = PointOfInterest.objects.filter(country=country).values_list("pk", "address", "position")
		data = json.dumps(list(zone))
		return HttpResponse(data, content_type="application/json")
