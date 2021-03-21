from django.shortcuts import render

from ghuser_activity.forms import UserNameForm

# mock
proj_scroll = [
    {
        'name': None,
        'url': None,
        'stars': None,
        'merged_pulls': {'url': None, 'comments_number': None},
        'unmerged_pulls': {'url': None, 'comments_number': None},
    },
    {
        'name': None,
        'url': None,
        'stars': None,
        'merged_pulls': {'url': None, 'comments_number': None},
        'unmerged_pulls': {'url': None, 'comments_number': None},
    },
]


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
            'proj_scroll': proj_scroll,
        },
    )
