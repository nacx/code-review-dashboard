
def load():
    return Tetrate()


class Tetrate:
    def __init__(self):
        self.config = {
            'title': 'Tetrate Code Review Dashboard',
            'headers': {'left': 'Need More Work', 'middle': 'CircleCI Happy', 'right': 'Approved!'},
            'template': 'tetrate.html',
        }

    def repos(self, github):
        return github.list_org_repos('tetrateio') + github.list_org_repos('tetratelabs')

    def parse_pull(self, pull, data):
        data['obsolete'] = data['old'] >= 2

    def classify(self, pull):
        approved = pull['likes']
        rejected = pull['dislikes']

        if approved > rejected:
            return 'right'
        elif pull['build_status'] == 'success':
            return 'middle'
        elif pull['build_status'] == 'failure':
            return 'left'
        else:
            return 'left'

    def parse_comment(self, comment, summary):
        pass
