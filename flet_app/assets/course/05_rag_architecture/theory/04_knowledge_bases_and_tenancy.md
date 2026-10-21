# Knowledge Bases and Tenancy

Amazon Bedrock Knowledge Bases package parsing, chunking, embeddings, a vector store, and sync. That is the right default until a requirement forces you out. The requirement that most often forces a stronger design is **isolation**, not chunk size.

## Managed versus custom

| Stay with Knowledge Bases | Leave, or wrap them, when |
|---------------------------|---------------------------|
| S3 or a supported connector is the source of truth | You need a chunker or an embedding model the product cannot express |
| One platform team can own sync | The index already exists and migrating it is the expensive part |
| Metadata filters cover tenancy | A filter bug is an unacceptable cross-tenant disclosure |

Vector store choices inside or beside that decision: OpenSearch Serverless (AWS-operated, watch the OCU floor), Aurora PostgreSQL with pgvector (vectors next to relational filters you already run), S3 Vectors when you want object-storage economics for the vectors, or a third-party index only after a vendor and data-flow review. The store is a residency and cost decision. It is not where you hide a missing tenant filter.

## Isolation levels

`tenant_isolation(regulatory, tenant_count)`:

| Regulatory class | Result |
|------------------|--------|
| `tenant_count < 1` | `ValueError` |
| `regulated_plus` | `account_per_tenant` |
| `strict` | `index_per_tenant` |
| `standard` | `shared_index_metadata_filter` |
| Anything else | `ValueError` |

`tenant_count` does not weaken the class. A thousand regulated tenants do not become a shared index because accounts are inconvenient. They become a platform problem you staff. Cost shows up in the ADR; it does not override the class.

| Level | Protects against | You still owe |
|-------|------------------|---------------|
| Shared index, mandatory metadata filter | Accidental queries, if every path uses the gateway | A bug or a second client that forgets the filter |
| Index (or collection) per tenant | A forgotten filter in one app | Shared credentials, shared logs, a noisy embedding pipeline |
| Account per tenant | A much larger blast radius, IAM included | Account vending, quota, and cost operations |

The filter is applied in **one retrieval gateway**. Application teams do not pass a raw query to `Retrieve`. The gateway injects `tenant_id` from the authenticated caller. The model is not asked to add it.

Review line: **"A metadata filter is a control only if the model cannot bypass the component that sets it."**

## IAM

The runtime role gets `bedrock:Retrieve` on the specific knowledge base, not `bedrock:*`, and not `Retrieve` on every knowledge base in the account. The ingest role can write documents and start sync. It cannot be the role the user-facing service assumes. Module 08 puts that matrix in code.
