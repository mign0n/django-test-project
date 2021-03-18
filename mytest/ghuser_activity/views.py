from django.shortcuts import render

from ghuser_activity.forms import UserNameForm


def index(request):
    username = 'Unknown'
    if request.method == 'POST':
        form = UserNameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
    else:
        form = UserNameForm()
    return render(
        request,
        'ghuser_activity/index.html',
        {
            'title': 'Get Github user activity info.',
            'form': form,
            'username': username,
        },
    )
