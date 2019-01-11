import json

with open('settings.json', 'r') as json_settings:
    data = json.load(json_settings)

data['device']['room'] = 1234

with open('settings.json', 'w') as json_settings:
    json.dump(data, json_settings, sort_keys=True, indent=4, separators=(',', ': '))
