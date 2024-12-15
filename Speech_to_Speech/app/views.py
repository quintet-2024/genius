from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request,"index.html")

def feedback(req):
    return render(req, "feedback.html")
def complaints(req):
    return render(req, "complaints.html")
def users(req):
    return render(req, "viewusers.html")
def admin_home(req):
    return render(req, "admin_home.html")