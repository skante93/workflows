# Algofab features: Ulpoad through API

## Context

This workflow shows how to upload a resource on Algofab through the API server.

## Outcome

* Being able to upload a resource on Algofab through the API server

## Pre-requisites

* Signin up on Algofab

## Instructions

To create a new resource, send a request like this :

```bash
curl -X POST -H "Content-Type: multipart/form-data" \
  -F 'name=resourceName' \
  -F 'logo=@/path/to/logo' \
  ...
  https://[address of API Server]/resources 
```

where: 
* __[adresse of API Server]__ : is the adress of the API server

### Response

If respone statsus code is :
* __201__: the resource was successfully created
* __otherwise__: there was an error. 
