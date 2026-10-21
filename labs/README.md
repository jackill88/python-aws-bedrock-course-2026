# Optional live labs

These exercises are not part of `pytest`. They need an AWS account, Bedrock model access in a region you are allowed to use, and a sandbox that does not contain production prompts. Prices and console clicks change; treat the AWS docs for Bedrock as the source of truth for the current screen.

Do this work in a sandbox account with a spend alarm. Do not point a prototype at a production knowledge base.

## Lab 1 — One Converse call through a role you could defend

1. Create a role that can call `bedrock:Converse` and `bedrock:InvokeModel` only on the model id you picked.
2. From a sandbox, send a short `converse` request with a system text, a user text, `maxTokens`, and a low temperature.
3. Record the `stopReason` and the input and output token counts from the response.
4. Confirm a second principal without that resource ARN is denied.

## Lab 2 — Pin a guardrail version

1. Create a guardrail with one denied topic and a sensitive-information filter.
2. Publish a version. Point the sandbox call at that version, not at the draft.
3. Send a prompt that should trip the topic and one that should not. Keep the trace long enough to see which policy fired.
4. Call `ApplyGuardrail` on a tool-argument string without invoking a model.

## Lab 3 — A tiny knowledge base

1. Put two short policy files in an S3 bucket, with a tenant id in metadata if the console path you are using supports it.
2. Create a knowledge base and sync it.
3. `Retrieve` as the runtime role. Confirm a query returns a citation location you can open.
4. Ask for a fact that is in neither file and practice the abstain path in your own code, not only in the console chat.

## Lab 4 — See what you would actually log

1. Enable model invocation logging to a bucket in the sandbox.
2. Make one call. See whether the prompt body was stored.
3. Turn content logging off, or restrict the bucket, until the object matches the field policy in Module 08.
4. Find the same call's management events in CloudTrail and confirm the prompt is not there.

## Lab 5 — Region list

1. If you use a cross-region inference profile, write down every destination region the profile documents.
2. Compare that list to the regions your data is allowed to enter.
3. If they differ, pin a single-region model id instead of "fixing" it in the prompt.

Stop when you can point at a role, a guardrail version, a retrieve filter, and a log bucket and say which module each one came from.
