from django.http import HttpResponse

def home(request):
    return HttpResponse("🎓 University ERP is LIVE SUCCESSFULLY")