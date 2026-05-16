from feast import Entity, FeatureView, Field
from feast.types import Int64

# entity (candidate)
candidate = Entity(
    name="candidate_id",
    join_keys=["candidate_id"]
)

# feature view (resume features only)
resume_features = FeatureView(
    name="resume_features",
    entities=[candidate],
    schema=[
        Field(name="experience", dtype=Int64),
        Field(name="skills", dtype=Int64),
        Field(name="projects", dtype=Int64),
    ],
)