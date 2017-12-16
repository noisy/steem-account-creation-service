import re
from collections import defaultdict

from social_core.backends.github import GithubOAuth2

dict_roles = {
    'GITHUB__FOLLOWERS__GT': '100,10',
    'GITHUB__CREATED_AT__BEFORE': '2017-12-01,40',
}

operators = {
    'lt': lambda attr, param, weight: int(weight) if attr < int(param) else 0,
    'gt': lambda attr, param, weight: int(weight) if attr > int(param) else 0,
    'before': lambda attr, param, weight: int(weight) if attr < param else 0,
}


class Github(GithubOAuth2):
    GET_ALL_EXTRA_DATA = True

    def extra_data(self, user, uid, response, details=None, *args, **kwargs):
        """Return access_token, token_type, and extra defined names to store in
            extra_data field"""
        data = super(GithubOAuth2, self).extra_data(user, uid, response, details, *args, **kwargs)
        data.update(details)

        return data

    def get_score(self, data, *args, **kwargs):

        score = 0

        roles = defaultdict(list)
        backend_name = self.name.upper()
        for key, value in dict_roles.items():
            res = re.match(r"{}__(\w+)__(\w+)".format(backend_name), key)
            if res:
                key = res[1].lower()
                op = res[2].lower()

                roles[key].append({
                    'operator': operators[op],
                    'params': value.split(",")
                })
            else:
                print("Key: '{}' do not match '{{BACKEND_NAME}}__{{ATTR}}__{{OPERATOR}}' pattern".format(key))

        for attr, val in data.items():
            for role in roles.get(attr, []):
                op = role['operator']
                res = op(val, *role['params'])
                score += res

        return score
