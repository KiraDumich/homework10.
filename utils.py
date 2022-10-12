import json


def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_all():
    return load_candidates()


def get_by_pk(pk):
    for candidate in load_candidates():
        if candidate['id'] == pk:
            return candidate
    return 'No candidate'


def get_candidates_by_skill(skill):
    result = []
    for candidate in load_candidates():
        if skill in candidate['skill'].lower():
            result.append(candidate)
    return result


