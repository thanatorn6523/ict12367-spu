from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("ICT12367")

def contact(request):
    return HttpResponse(
        "<h1>ติดต่อ</h1>"
        "<p>รหัสนักศึกษา: 68116523</p>"
        "<p>ชื่อ: ธนธร</p>"
        "<p>นามสกุล: นามกร</p>"
    )

def form(request):
    return render(request, "form.html")