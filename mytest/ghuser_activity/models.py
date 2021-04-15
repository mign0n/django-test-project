class GHUserProjectsInfo:
    def __init__(self, gh_instance, target_username):
        self.gh_instance = gh_instance
        self.target_username = target_username
        self.user = self.gh_instance.get_user(self.target_username)
        self.repos = (repo for repo in self.user.get_repos())

    @staticmethod
    def get_all_pulls_from(repo):
        return repo.get_pulls(state='all')

    @staticmethod
    def get_pulls_urls(pulls):
        merged_pulls = dict()
        unmerged_pulls = dict()
        for pull in pulls:
            if pull.merged:
                merged_pulls[pull.number] = pull.html_url
            else:
                unmerged_pulls[pull.number] = pull.html_url
        return merged_pulls, unmerged_pulls

    @staticmethod
    def get_comments_number_of(pulls):
        return {
            pull.number: len(
                [comment.id for comment in pull.get_comments()]
            ) for pull in pulls
        }

    @staticmethod
    def make_pulls_urls_comments(pulls_num_url, pulls_num_comments):
        return {
            pulls_num_url.get(number): pulls_num_comments.get(number)
            for number in pulls_num_url.keys()
        }

    @staticmethod
    def change_data_format(data_dict):
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
