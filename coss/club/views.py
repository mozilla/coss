from django.contrib.auth.decorators import login_required


@login_required
def registration_complete(request):
    return render(request, 'pages/registration_complete.html')
