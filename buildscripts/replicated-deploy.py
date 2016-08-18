#!/bin/python
import boto
import json
import os
from boto.sqs.message import RawMessage

data = {
    "project": os.environ["CIRCLE_PROJECT_REPONAME"],
    "sha": os.environ["CIRCLE_SHA1"][:7]
}

sqs = boto.connect_sqs()
q = sqs.create_queue("chatops-deployer-staging")

m = RawMessage()
m.set_body(json.dumps(data))
q.write(m)
