from openlineage.client import OpenLineageClient
from openlineage.client.run import RunEvent, RunState
from datetime import datetime

def log_lineage():

    client = OpenLineageClient(url="http://localhost:5000")

    event = RunEvent(
        eventType=RunState.COMPLETE,
        eventTime=str(datetime.utcnow()),
        run={"runId": "resume-shortlisting-run"},
        job={"namespace": "mlops-project", "name": "resume-pipeline"},
        inputs=[{"namespace": "data", "name": "resumes.csv"}],
        outputs=[{"namespace": "model", "name": "resume-model"}],
    )

    print("Lineage event created (mock/demo mode)")