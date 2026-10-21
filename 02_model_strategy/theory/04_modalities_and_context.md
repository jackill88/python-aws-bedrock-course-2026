# Modalities and Context

"The model accepts 200k tokens" is not an architecture. Context is a **budget** you spend on system instructions, history, retrieved text, tool results, and the answer. Modalities (text, image, document, speech) change the pipeline before the model ever sees tokens.

## Context is not free knowledge

| Approach | Fits when | You accept |
|----------|-----------|------------|
| Prompt only | The policy or facts are small and stable | Manual updates when facts change |
| Long context | A medium corpus, slow change, and you will pay input tokens every call | Latency, cost, and "lost in the middle" quality |
| RAG | The corpus is large or fresh | A retrieval system, citations, and tenant filters (Module 05) |

Stuffing a full handbook into every call because the window allows it will pass a demo and fail a cost review. It also makes tenancy harder: you just put every tenant's text in the prompt.

## Modalities

| Input | Architect's extra path |
|-------|------------------------|
| Plain text | Token budget, injection from user text |
| Office docs and PDFs | Parsing first. A raw PDF dump is not a knowledge base. Tables and scans need a parser or Bedrock Data Automation, then chunks |
| Images | A vision-capable model id, size limits, and a decision about whether the image is untrusted input |
| Audio | Transcription as its own quality stage; the transcript is what retrieval and policy see |
| Embeddings | A different model id than the chat model. Dimension and normalization must match the index |

Do not send images or audio to a text-only model and call the failure a prompt bug. The route includes the modality.

## Tool use vs a longer prompt

If the model must **read a system of record**, give it a tool or a retrieval API. Do not paste the database into the context "because the window is large." The window is not an authorization boundary, and it is not fresh.

If the model must **decide among a few policies that fit in a page**, a long prompt can be simpler than RAG. Write that down so the next team does not add a vector store out of habit.

## Parameters that belong in the review

| Parameter | Production default tendency |
|-----------|----------------------------|
| Temperature | Low (often near 0–0.3) for extraction, tools, and policy answers. Higher only for ideation, and not on the regulated path |
| Max output tokens | Capped. Unbounded generation is a cost and latency incident |
| Stop sequences | When you need to cut a tool channel or a delimiter you defined |

These are use-case config, next to the model id. A frontier model at high temperature is not "more intelligent"; it is less repeatable, which makes evals lie.

## Review questions

- What is the p95 input token count, not the maximum window?
- Which modality is on the critical path, and what parses it?
- If we drop from frontier to balanced, which modality or tool schema breaks?
- Are system prompt + tool definitions stable enough to cache (Module 03)?

Review line: **"Window size is a ceiling. The budget we pay for is the median request."**
