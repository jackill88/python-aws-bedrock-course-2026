"""
Challenge: Citation Policy
Module 05: RAG Architecture

Implement the function(s) below. Run tests with:
    pytest tests/05_rag_architecture/ -v
"""


def citation_policy(user_facing: bool, retrieved_count: int) -> str:
    """
    Return "optional", "abstain_or_disclose_ungrounded", or "cite_sources".

    Raise ValueError if retrieved_count < 0.
    Not user-facing -> "optional".
    User-facing and retrieved_count == 0 -> "abstain_or_disclose_ungrounded".
    User-facing and retrieved_count > 0 -> "cite_sources".
    """
    pass
