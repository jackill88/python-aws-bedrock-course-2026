"""
Challenge: Classify API Plane
Module 01: Bedrock Platform

Implement the function(s) below. Run tests with:
    pytest tests/01_bedrock_platform/ -v
"""


def classify_api_plane(api_name: str) -> str:
    """
    Return "control" or "data".

    control:
        CreateGuardrail, CreateKnowledgeBase,
        PutModelInvocationLoggingConfiguration,
        CreateProvisionedModelThroughput, ListFoundationModels
    data:
        Converse, ConverseStream, InvokeModel, Retrieve,
        RetrieveAndGenerate, ApplyGuardrail

    Raise ValueError for any other name.
    """
    pass
