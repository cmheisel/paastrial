from twitterdedupe.daemons import ToggleDaemon

import json

with open('/home/dotcloud/environment.json') as f:
    env = json.load(f)

env['REDISTOGO_URL'] = env['DOTCLOUD_DATA_REDIS_URL']

d = ToggleDaemon(env)
d.run_forever()
