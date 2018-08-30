import re


def load():
    return Tetrate()


class Tetrate:
    def __init__(self):
        self.config = {
            'title': 'Tetrate Code Review Dashboard',
            'headers': {'left': 'Need More Work', 'middle': 'CircleCI Happy', 'right': 'Approved!'},
            'template': 'tetrate.html',
        }
        self.repos = self._repos()

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

    def _repos(self):
        return ["https://api.github.com/repos/tetrateio/tetrate",
                "https://api.github.com/repos/tetrateio/tetrate-ui",
                "https://api.github.com/repos/tetrateio/deployments-prod",
                "https://api.github.com/repos/tetrateio/website",
                "https://api.github.com/repos/tetrateio/ngac",
                "https://api.github.com/repos/tetratelabs/liaison",
                "https://api.github.com/repos/tetratelabs/mcc",
                "https://api.github.com/repos/tetratelabs/envoy-extensions",
                "https://api.github.com/repos/tetratelabs/istio-route53",
                "https://api.github.com/repos/tetratelabs/mixer-lite",
                "https://api.github.com/repos/tetratelabs/istio-tools"
                ]
