"""
Challenge: Chunk Strategy
Module 05: RAG Architecture

Implement the function(s) below. Run tests with:
    pytest tests/05_rag_architecture/ -v
"""


def chunk_strategy(doc_type: str) -> str:
    """
    Return the ingestion strategy for a document type.

    policy_pdf -> hierarchical
    faq -> one_chunk_per_item
    chat_log -> fixed_with_overlap
    code -> structure_aware
    scanned_form -> parse_then_fixed

    Raise ValueError for any other type.
    """
    pass
