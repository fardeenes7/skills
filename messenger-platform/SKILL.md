---
name: Messenger Platform
description: Comprehensive master skill for the Meta Messenger Platform. Triggers for anything related to Facebook/Instagram messaging, Graph API, Webhooks, Send API, Handover Protocol, Marketing Messages, policy compliance, support operations, and Messenger UI elements (templates, buttons, quick replies).
---

# Messenger Platform Master Skill

This skill provides a structured, operational framework for the Meta Messenger Platform (Facebook + Instagram Messaging), with a coverage map aligned to parsed source docs.

## Core Navigation
| Topic | Description | Reference File |
| :--- | :--- | :--- |
| **Authentication** | App setup, permissions, access tokens, login flows, and ID scoping (PSID/IGSID/SID). | [authentication.md](references/authentication.md) |
| **Messaging** | Send API, 24h policy window, Message Tags, templates, quick replies, sender actions, and asset reuse. | [messaging.md](references/messaging.md) |
| **Webhooks** | Setup, signature verification, core + advanced webhook event reference, and delivery handling patterns. | [webhooks.md](references/webhooks.md) |
| **Advanced Features** | Handover protocol, recurring/marketing notifications, utility messages, personas, profile configuration, and conversation APIs. | [advanced_features.md](references/advanced_features.md) |
| **Troubleshooting** | Error codes, rate limiting, reliability practices, policy checks, FAQ-style debugging, and support escalation paths. | [troubleshooting.md](references/troubleshooting.md) |
| **Parsed Docs Coverage Matrix** | Topic-by-topic mapping to ensure the skill represents the parsed Messenger docs corpus. | [coverage_matrix.md](references/coverage_matrix.md) |

---

## When to Use
- **Implementation**: Build bots, routing logic, profile setup, or marketing/utility messaging pipelines.
- **Maintenance**: Rotate tokens, update subscriptions, maintain compliance, and monitor message health.
- **Debugging**: Diagnose delivery failures, webhook mismatches, permission issues, and policy-window violations.
- **Architecture**: Design multi-app handover systems, stateful conversation ownership, and support workflows.

## Primary Workflow
1. **Foundation + Access**: Start with [authentication.md](references/authentication.md).
2. **Inbound Processing**: Set up callbacks with [webhooks.md](references/webhooks.md).
3. **Outbound Messaging**: Implement sends and templates from [messaging.md](references/messaging.md).
4. **Scale + Ownership**: Add routing/marketing/profile/conversation patterns from [advanced_features.md](references/advanced_features.md).
5. **Stabilize + Govern**: Use [troubleshooting.md](references/troubleshooting.md).
6. **Audit Completeness**: Confirm parsed-doc coverage with [coverage_matrix.md](references/coverage_matrix.md).

---

## Quick Reference: Send API Endpoint
```bash
POST https://graph.facebook.com/v25.0/me/messages?access_token=<PAGE_ACCESS_TOKEN>
```
(See [messaging.md](references/messaging.md) for payload patterns and policy context.)
