# dla_poc

## Datasets
1. Github repository GitHub repository containing a dataset for assessing a web server's compliance with national cybersecurity agency requirements related to Transport Layer Security (TLS)
https://zenodo.org/records/15011611

## Build Custom Workbench Image
```
source .env
oc create secret docker-registry quay-creds --docker-server=quay.io \ 
--docker-username=${DOCKER_USERNAME}${DOCKER_USERNAME_SUFFIX} \
--docker-password=${DOCKER_PASSWORD} \
--docker-email=${DOCKER_EMAIL}
oc new-build --name=sdghub-wb --to="quay.io/oawofolurh/sdg:latest" --strategy=docker --push-secret quay-creds --binary
oc start-build sdghub-wb --from-dir docker --follow
```
