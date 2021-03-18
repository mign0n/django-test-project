from django.shortcuts import render


def index(request):
    return render(
        request,
        'ghuser_activity/index.html',
        {'title': 'Get Github user activity info.'}
    )
