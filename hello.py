import os
print(os.environ)

import json
print("Content-type: application/json\n\n")
print(json.dumps(dict(os.environ)))
