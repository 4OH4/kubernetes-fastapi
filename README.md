# kubernetes-fastapi

Barebones Python FastAPI in Kubernetes

Built on fastapi-aws-lambda-example (MIT License):

- https://iwpnd.pw/articles/2020-01/deploy-fastapi-to-aws-lambda

## Development setup

To run (in isolation), either:

Run from active Python environment using `uvicorn`:

    pip install uvicorn
    pip install -r requirements.txt
    uvicorn service.main:app --host 0.0.0.0 --port 8080 --reload

Or build and run the Docker container:

    docker build -t 4oh4/kubernetes-fastapi:1.0.0 .
    docker run -p 8080:8080 --name kubernetes-fastapi 4oh4/kubernetes-fastapi:1.0.0

Navigate to http://localhost:8080/docs to test the API.

## Google Cloud GKE initial setup

From command line, with [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) installed:

    gcloud components install kubectl

    gcloud config set project MyProjectName
    gcloud config set compute/zone europe-west2-a

Create a cluster and get credentials for `kubectl`:

    gcloud container clusters create MyClusterName --num-nodes=1
    gcloud container clusters get-credentials MyClusterName

## Kubernetes deployment

    kubectl apply -f api_deployment.yaml

## Teardown

    kubectl delete deployment kf-api
    kubectl delete svc kf-api-svc

## Google Cloud clean-up

    gcloud container clusters delete MyClusterName

** Check all resources have been deleted in the console - if in doubt, delete the project as well **
