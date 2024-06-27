from google.cloud import aiplatform

model = aiplatform.Model('projects/your-project/locations/us-central1/endpoints/your-endpoint')
model.deploy(
    machine_type='n1-standard-4',
    min_replica_count=1,
    max_replica_count=4
)
