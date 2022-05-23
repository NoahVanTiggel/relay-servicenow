#!/usr/bin/env python
import pysnow
import json
from relay_sdk import Interface, Dynamic as D

relay = Interface()

# Create client object
host = relay.get(D.servicenow.connection.host)
user = relay.get(D.servicenow.connection.user)
password = relay.get(D.servicenow.connection.password)


# get the spec object to process optional arguments
spec = relay.get()

# arguments are optional
arguments = {}
if 'arguments' in spec:
    arguments = spec['arguments']

c = None
try:
    c = pysnow.Client(host=host, user=user, password=password)
except:
    print('ERROR: Failed to authenticate to ServiceNow. Exiting.')
    exit(1)

# Define a ServiceNow resource
resource = c.resource(api_path=relay.get(D.resource))

# query is optional
query = {}
if 'query' in spec:
    query = spec['query']

# filter and filterparameters are optional
pyfilter = None
filterparameters = []
if 'filter' in spec:
    pyfilter = spec['filter']
    if 'filterparameters' in spec:
        filterparameters = spec['filterparameters']
        for filterparameter in filterparameters:
            print(f'Applying parameter "{filterparameter}" to filter "{pyfilter}".')
            pyfilter = pyfilter.replace(f'#{filterparameter}', f'filterparameters["{filterparameter}"]')

# Execute the query
iterable_content = resource.get(query, **arguments).all()

# Log and set record count
print(f'Retrieved {len(iterable_content)} records using query "{query}".')
relay.outputs.set('record_count', len(iterable_content))
# print(json.dumps(iterable_content, indent=1))

# Filter using a Python lambda and log and set filtered record count
if pyfilter:
    print(f'Applying filter "{pyfilter}" to dataset.')
    filter_expr = eval(pyfilter)
    iterable_content = list(filter(filter_expr, iterable_content))
    print(
        f'Filtered to {len(iterable_content)} records using filter "{pyfilter}".')
    # print(json.dumps(iterable_content, indent=1))
    relay.outputs.set('filtered_record_count', len(iterable_content))

# Set the output
relay.outputs.set('output', iterable_content)
