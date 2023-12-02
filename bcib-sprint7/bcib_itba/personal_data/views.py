from django.shortcuts import render

# Create your views here.
def data_view(request):
    return render(request, "personal_data/personal_data.html")