# example/views.py
# from datetime import datetime
from django.contrib.auth import get_user_model
from django.http import HttpResponse

User = get_user_model()

def index(request):
    print(User.objects.all())
    # now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is. {'Khong thay User' if User.objects.exists() else 'Not Found'}</p>
        </body>
    </html>
    '''
    return HttpResponse(html)