# Module 05: RAG Architecture

Retrieval-augmented generation is a data system that happens to call a model. Lead architects decide when retrieval is the wrong tool, how documents become chunks, and how tenancy is enforced outside the prompt.

## Learning Objectives

By the end of this module you will be able to:

- Choose prompt-only, long context, RAG, fine-tune, or RAG plus fine-tune from freshness, size, and behavior change
- Pick a chunking strategy from the document shape, not from a default of 500 tokens
- Separate logical tenant filters from stronger index and account isolation
- Require citations on user-facing answers and an abstain path when nothing was retrieved

## Lessons

| # | Topic | Theory |
|---|-------|--------|
| 1 | The Grounding Decision | [theory/01_grounding_decision.md](theory/01_grounding_decision.md) |
| 2 | Ingestion, Chunking, and Freshness | [theory/02_ingestion_chunking_freshness.md](theory/02_ingestion_chunking_freshness.md) |
| 3 | Retrieval, Filters, Rerank, Citations | [theory/03_retrieval_filters_rerank_citations.md](theory/03_retrieval_filters_rerank_citations.md) |
| 4 | Knowledge Bases and Tenancy | [theory/04_knowledge_bases_and_tenancy.md](theory/04_knowledge_bases_and_tenancy.md) |

## Quiz

Test your understanding: [quizzes/rag_architecture_quiz.md](quizzes/rag_architecture_quiz.md)

## Challenges

| Challenge | File |
|-----------|------|
| Choose Grounding | [challenges/choose_grounding.py](challenges/choose_grounding.py) |
| Chunk Strategy | [challenges/chunk_strategy.py](challenges/chunk_strategy.py) |
| Tenant Isolation | [challenges/tenant_isolation.py](challenges/tenant_isolation.py) |
| Citation Policy | [challenges/citation_policy.py](challenges/citation_policy.py) |

Run tests for this module:

```bash
pytest tests/05_rag_architecture/ -v
```
