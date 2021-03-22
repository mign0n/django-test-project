class GHUserProjectsInfo:
    def __init__(self, ghinstance, target_username):
        self.ghinstance = ghinstance
        self.target_username = target_username
        self.user = self.ghinstance.get_user(self.target_username)
        self.repos = (repo for repo in self.user.get_repos())

    def get_all_pulls_from(self, repo):
        return repo.get_pulls(state='all')

    def get_pulls_urls(self, pulls):
        mpulls = dict()
        umpulls = dict()
        for pull in pulls:
            if pull.merged:
                mpulls[pull.number] = pull.html_url
            else:
                umpulls[pull.number] = pull.html_url
        return mpulls, umpulls

    def get_comments_number_of(self, pulls):
        return {
            pull.number: len(
                [comment.id for comment in pull.get_comments()]
            ) for pull in pulls
        }

    def make_pulls_urls_comments(self, pulls_num_url, pulls_num_comments):
        return {
            pulls_num_url.get(number): pulls_num_comments.get(number)
            for number in pulls_num_url.keys()
        }

    def change_data_format(self, data_dict):
        return [
            {'url': url, 'comments_number': num} for url, num in data_dict.items()
        ]

    def make_projects_scroll(self):
        scroll = []
        for repo in self.repos:
            name = repo.name
            url = repo.html_url
            stars = repo.stargazers_count
            pulls = self.get_all_pulls_from(repo)
            comments_number = self.get_comments_number_of(pulls)
            merged_pulls, unmerged_pulls = self.get_pulls_urls(pulls)
            merged_pulls = self.make_pulls_urls_comments(merged_pulls, comments_number)
            unmerged_pulls = self.make_pulls_urls_comments(unmerged_pulls, comments_number)
            merged_pulls = self.change_data_format(merged_pulls)
            unmerged_pulls = self.change_data_format(unmerged_pulls)
            if merged_pulls:
                scroll.append(
                    {
                        'name': name,
                        'url': url,
                        'stars': stars,
                        'merged_pulls': merged_pulls,
                        'unmerged_pulls': unmerged_pulls
                    }
                )
        return scroll
