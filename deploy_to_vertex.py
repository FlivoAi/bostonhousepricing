import os
from google.cloud import aiplatform
 
def deploy_model():
    from google.cloud import aiplatform
    project_id = os.getenv('GOOGLE_PROJECT')
    bucket= os.getenv('GCS_BUCKET_NAME')
    region = "us-central1"  
    # Initialize the Vertex AI client
    aiplatform.init(project=os.getenv(project_id), location=region)
        # Upload the model
    model = aiplatform.Model.upload(
        display_name='my-model',
        # url_model="regmodel.pkl"
        artifact_uri=f'gs://{bucket}',
        serving_container_image_uri='us-central1-docker.pkg.dev/{project_id}/test1/ml-img',
    )
    #creating endpoint 
    endpoint = aiplatform.Endpoint.create(
    project=project_id,
    display_name="ml-endpoint",
    location=region,  # Optional, change if needed
    )
    print(f"Endpoint created: {endpoint.name}")

    # Deploy the model to an endpoint
    endpoint = model.deploy(
        deployed_model_display_name='ml-endpoint',
        machine_type='n2-standard-4',
        min_replica_count=1,
        max_replica_count=4,
    )
 
    print(f"Model deployed to endpoint: {endpoint.resource_name}")
 
if __name__ == '__main__':
    deploy_model()
