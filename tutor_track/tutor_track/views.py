from django.http import HttpResponse

def handler404(request, exception):
    return HttpResponse(
        '''
        <h1>Ups! Page not found!</h1>
        <br>
        <button onclick="window.location.href='/home'">Go to Home Page</button>
        ''',
        status=404)