# Ingestion, Chunking, and Freshness

Retrieval quality is mostly an ingestion problem. A brilliant reranker cannot recover a chunk that merged two policies or dropped the table header.

## Chunk strategy by document shape

`chunk_strategy` returns one strategy:

| Document | Strategy | Why |
|----------|----------|-----|
| `policy_pdf` | `hierarchical` | Retrieve a precise child span, expand to the parent section for context |
| `faq` | `one_chunk_per_item` | The natural unit is already the Q&A pair. Do not slice it |
| `chat_log` | `fixed_with_overlap` | Weak structure. Overlap keeps a sentence that crosses a boundary |
| `code` | `structure_aware` | Split on symbols, not on a character count that cuts a function in half |
| `scanned_form` | `parse_then_fixed` | OCR or document parsing first. Chunking pixels is noise |

Unknown types raise `ValueError`. Adding a type means a conscious choice, not a fallback to 300 tokens.

## Parsing is a stage

PDFs with tables, columns, and scans need a parser before embeddings. Bedrock Knowledge Bases can use default parsing, foundation-model parsing, or Bedrock Data Automation for richer documents. The architect's question is whether the **table a user will ask about** survives as text with its headers. If it does not, no embedding model saves the program.

## Metadata you attach at ingest

| Field | Use |
|-------|-----|
| `tenant_id` | Mandatory filter. Not a hint in the prompt |
| `document_id` and `source_uri` | Citations and deletion |
| `effective_from` / `effective_to` | Prefer the current policy over a superseded one |
| `acl` or group ids | If users inside a tenant do not all see the same corpus |
| embedding model id | So a later migration can find stale vectors |

Deletion and supersession are part of ingestion. A RAG system that only appends will answer with last year's policy and sound confident.

## Freshness

| Change rate | Ingestion posture |
|-------------|-------------------|
| Rare | Nightly sync is fine. Record the lag in the SLO |
| Weekly | Event or scheduled sync. Answers should cite the effective date |
| Daily or faster | The sync lag is a product requirement. If you cannot meet it, do not promise live facts |

Knowledge Bases sync jobs and a custom pipeline (CDC into your own index) are both valid. Managed sync wins when connectors and chunking fit. A custom pipeline wins when you already operate the index, you need a chunker the product does not offer, or the embedding model is outside the managed list.

Review line: **"State the maximum age of a chunk the assistant is allowed to quote."**
