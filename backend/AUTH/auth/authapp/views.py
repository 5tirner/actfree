from django.http import HttpResponse

def login(req):
    if req.method == "POST":
        print("This Is A GET Method")
    return HttpResponse("AUTHENTICATION PAGE")