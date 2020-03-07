from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def home(request):
    x_forward_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forward_for:
        ip = "HTTP_X_FORWARDED_FOR: {0}".format((x_forward_for.split(",")[0]))
    else:
        ip = "REMOTE_ADDR {0}".format(request.META.get("REMOTE_ADDR"))
    
    print("\n"+ ip+"\n-----------------------------------------\nIP Saved on djserver/data.txt\n")

    opnr = open("data.txt", "a+")
    opnr.write("\n" + ip + "\n")
    opnr.close()

    return render(request, "index.html")