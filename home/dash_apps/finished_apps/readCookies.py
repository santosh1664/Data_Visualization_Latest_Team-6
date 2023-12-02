from django.http import HttpResponse

def readCookies(request):
    cookie_value = request.COOKIES.get('toggleState')

    if cookie_value is not None:
        return HttpResponse(f"The value of the cookie 'my_cookie' is {cookie_value}")
    else:
        return HttpResponse("Cookie 'my_cookie' not found")

print(readCookies())