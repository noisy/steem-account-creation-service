

def get_score(backend, details, response, uid, user, social, *args, **kwargs):
    score = backend.get_score(social.extra_data)
