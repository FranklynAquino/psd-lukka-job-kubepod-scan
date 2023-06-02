
# Kubernetes service-connector scan for job_ids

This script accepts arguments 

Example run:

`python3 run.py <path to file>`

File requirements: .txt file of job_id(s)


## Environment Variables

To run this project locally, you will need to add the following environment variables to your .env file

```
RESOURCE_PATH= .
HOST_NAME=kibana.lukka.tech
PORT_NUMBER=443
OPENSEARCH_USERNAME=production_support_sa
OPENSEARCH_PASSWORD=5{3zfx8D?phTre5H
```

To make changes to the openSearch query, you may change the following configs in your atlas_k8s manifest file or your personal .env file
```
OPENSEARCH_SET_MINS_BEFORE=< Minutes to look back >
```

