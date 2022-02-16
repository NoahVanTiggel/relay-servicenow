# servicenow-step-query

This [ServiceNow](https://servicenow.com) step container runs a query.

## Specification

This step expects the following fields in the `spec` section of a workflow step definition that uses it:

| Setting       | Data type | Description                                                                     				      | Default | Required |
|---------------|-----------|-----------------------------------------------------------------------------------------------|---------|----------|
| `connection`  | Object    | Your ServiceNow connection                                               						          | None    | Yes      |
| `resource`    | String   	| The resource to query                      													                          | None	  | Yes      |
| `query`   	  | String    | The query to run 																				                                      | None    | Yes      | 
| `arguments` 	| Object    | Optional arguments to use during query                   										                  | None    | No       |
| `filter` 		  | String    | Optional Python lambda filter to reduce the output size										                    | None    | No       |

## Outputs

This step provides the following outputs:

| Output                      | Data type | Description                                                                     	| Default | Required |
|-----------------------------|-----------|-----------------------------------------------------------------------------------|---------|----------|
| `output`                    | Object    | The output of the query                                               						| None    | Yes      |
| `record_count`              | Integer   | Total number of records retrieved from ServiceNow                      						| 0	      | Yes      |
| `filtered_record_count`   	| Integer   | Number of records after Python filter is applied 																	| 0       | No       | 

## Usage

```yaml
step:
  name: query-servicenow
  image: relaysh/servicenow-step-query
  spec:
    servicenow:
      connection: !Connection { type: servicenow, name: my-snow-account }
    resource: '/table/mytable'
    query: 'os=Linux Red Hat^ORos=Windows'
    filter: 'lambda x: x["hostname"].startswith("host-")'
    arguments:
      limit: 30
      fields: ["hostname", "os"]
```