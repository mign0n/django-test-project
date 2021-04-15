from django.shortcuts import render
from github import Github
from github.GithubException import RateLimitExceededException

from ghuser_activity.forms import UserNameForm
from ghuser_activity.models import GHUserProjectsInfo
from mytest.settings import GITHUB_TOKEN


def get_projects_scroll(username):
    gh = Github(login_or_token=GITHUB_TOKEN)
    try:
        scroll = GHUserProjectsInfo(gh, username).make_projects_scroll()
    except RateLimitExceededException:
        scroll = []
        print('API rate limit exceeded.')
    return scroll


def index(request):
    username = 'Unknown'
    proj_scroll = None
    if request.method == 'POST':
        form = UserNameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            proj_scroll = get_projects_scroll(username)
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
