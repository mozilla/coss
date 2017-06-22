from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from coss.club.forms import ClubRegistrationForm
from coss.club.models import ClubRegistration


@login_required
def registration(request):
    if request.method == 'POST':
        form = ClubRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_complete')
    else:
        form = ClubRegistrationForm()
    return render(request, 'pages/registration.html', {'form': form})


@login_required
def registration_complete(request):
    return render(request, 'pages/registration_complete.html')


def club_view(request, club_pk):
    club = ClubRegistration.objects.get(pk=club_pk)
    return render(request, 'pages/club.html', {'club': club})
