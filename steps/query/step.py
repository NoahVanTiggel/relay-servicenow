#!/usr/bin/env python
import pysnow
import json
from relay_sdk import Interface, Dynamic as D

relay = Interface()

# Create client object
host = relay.get(D.servicenow.connection.host)
user = relay.get(D.servicenow.connection.user)
password = relay.get(D.servicenow.connection.password)
arguments = relay.get(D.arguments)

c = None
try:
    c = pysnow.Client(host=host, user=user, password=password)
except:
    print('ERROR: Failed to authenticate to ServiceNow. Exiting.') 
    exit(1)

# Define a resource
resource = c.resource(api_path=relay.get(D.resource))

# Execute the query
iterable_content = resource.get(relay.get(D.query), **arguments).all()

# Set the output
relay.outputs.set('output', iterable_content)
