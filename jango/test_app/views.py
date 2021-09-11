from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Test!</h1>")


def index2(request):
    return HttpResponse("<a href='https://www.google.com/'>Google</a>")


def index3(request):  # The view you will see on the base
    return HttpResponse("""<a href="test">Test 1</a>
                        <br>
                        <a href="test2">Test 2</a""")
