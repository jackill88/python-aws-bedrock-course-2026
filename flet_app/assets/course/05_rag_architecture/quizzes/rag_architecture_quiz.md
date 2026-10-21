# RAG Architecture Quiz

10 multiple-choice questions. Answers are at the bottom.

---

**1.** Hourly-changing facts and a large labeled behavior set should be:

- A) Fine-tune only
- B) RAG plus fine-tune
- C) Prompt only
- D) A longer temperature

**2.** A 120,000-token handbook that changes rarely, with an 8,000-token budget, maps to:

- A) `long_context`
- B) `prompt_only`
- C) `finetune`
- D) `rag_plus_finetune`

**3.** A 500,000-token corpus that changes rarely and does not fit the budget maps to:

- A) `long_context`
- B) `rag`
- C) `prompt_only`
- D) `finetune`

**4.** FAQ content should be chunked as:

- A) `hierarchical`
- B) `one_chunk_per_item`
- C) `parse_then_fixed`
- D) One embedding per character

**5.** Scanned forms should be:

- A) Embedded as images with no parse step in this course's strategy
- B) `parse_then_fixed`
- C) `one_chunk_per_item`
- D) Left out of metadata

**6.** The tenant filter belongs:

- A) In the system prompt as a reminder
- B) In the retrieval query, set by a gateway the model cannot skip
- C) In the temperature
- D) Only in the citation footnote

**7.** `regulated_plus` isolation means:

- A) A shared index with a metadata filter
- B) An account per tenant
- C) No IAM
- D) Fine-tuning the embedding model per tenant by default

**8.** A user-facing answer with zero retrieved passages should:

- A) Answer from model memory and cite "general knowledge"
- B) Abstain or disclose that it is ungrounded
- C) Raise the temperature
- D) Switch to provisioned throughput

**9.** `Retrieve` plus your own `Converse` is preferred over `RetrieveAndGenerate` when:

- A) You must own citations, the prompt, and the eval
- B) You want to avoid filters
- C) You have no corpus
- D) The task is a pure fine-tune

**10.** Deleting a superseded policy from the index is:

- A) Optional, because the model will notice the date
- B) Part of ingestion, or the assistant will quote stale text confidently
- C) A control-plane IAM problem only
- D) Handled by prompt caching

## Answers

1. B  2. A  3. B  4. B  5. B  6. B  7. B  8. B  9. A  10. B
