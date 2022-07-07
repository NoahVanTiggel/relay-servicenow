#!/usr/bin/env python
import pysnow
from relay_sdk import Interface, Dynamic as D

relay = Interface()

# Create client object
host = relay.get(D.servicenow.connection.host)
user = relay.get(D.servicenow.connection.user)
password = relay.get(D.servicenow.connection.password)

c = None
try:
    c = pysnow.Client(host=host, user=user, password=password)
except:
    print('ERROR: Failed to authenticate to ServiceNow. Exiting.') 
    exit(1)

# Define an incident table resource
incident = c.resource(api_path=relay.get(D.resource))

# Get the record object
record = relay.get(D.record)

# Create a new incident record
result = incident.create(payload=record)

# Print the result
r = result.all()[0]

# Set the output
print('\nSetting incident details to the output `incident`')
relay.outputs.set('incident', r)
