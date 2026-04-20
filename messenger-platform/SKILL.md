---
name: Messenger Platform
description: Comprehensive master skill for the Meta Messenger Platform. Triggers for anything related to Facebook/Instagram messaging, Graph API, Webhooks, Send API, Handover Protocol, Marketing Messages, and Messenger UI elements (templates, buttons, quick replies). Use this skill when the user wants to build chatbots, automate messaging, handle customer support integrations, or configure Meta App settings for messaging.
---

# Messenger Platform Master Skill

This skill provides a deep, operational framework for the Meta Messenger Platform (Facebook & Instagram Messaging), organized for progressive disclosure.

## Core Navigation
| Topic | Description | Reference File |
| :--- | :--- | :--- |
| **Authentication** | App setup, permissions, tokens, and scoping (PSID/IGSID). | [authentication.md](file:///home/fardeen/Projects/skills/messenger-platform/references/authentication.md) |
| **Messaging** | Send API, 24h rule, Message Tags, and Structured Templates. | [messaging.md](file:///home/fardeen/Projects/skills/messenger-platform/references/messaging.md) |
| **Webhooks** | Setup, event reference, security validation, and best practices. | [webhooks.md](file:///home/fardeen/Projects/skills/messenger-platform/references/webhooks.md) |
| **Advanced Features** | Handover Protocol, Recurring Notifications, Utility Messages, and Personas. | [advanced_features.md](file:///home/fardeen/Projects/skills/messenger-platform/references/advanced_features.md) |
| **Troubleshooting** | Detailed error code reference and stabilization tips. | [troubleshooting.md](file:///home/fardeen/Projects/skills/messenger-platform/references/troubleshooting.md) |

---

## When to Use
- **Implementation**: Building chatbots, setting up handover protocols, or marketing automation.
- **Maintenance**: Managing access tokens, allowlisting domains, or updating webhook subscriptions.
- **Debugging**: Solving delivery failures, rate limit issues, or permission errors.
- **Design**: Creating rich UI experiences with Generic/Button/Receipt templates.

## Primary Workflow
1. **Setup**: Use [authentication.md](file:///home/fardeen/Projects/skills/messenger-platform/references/authentication.md) to configure your Meta App and obtain tokens.
2. **Inbound**: Use [webhooks.md](file:///home/fardeen/Projects/skills/messenger-platform/references/webhooks.md) to set up your server to receive messages.
3. **Outbound**: Use [messaging.md](file:///home/fardeen/Projects/skills/messenger-platform/references/messaging.md) to send responses and rich templates.
4. **Scale**: Use [advanced_features.md](file:///home/fardeen/Projects/skills/messenger-platform/references/advanced_features.md) for complex logic and marketing.
5. **Debug**: Consult [troubleshooting.md](file:///home/fardeen/Projects/skills/messenger-platform/references/troubleshooting.md) for any API errors.

---

## Quick Reference: Send API Endpoint
```bash
POST https://graph.facebook.com/v25.0/me/messages?access_token=<PAGE_ACCESS_TOKEN>
```
(See [messaging.md](file:///home/fardeen/Projects/skills/messenger-platform/references/messaging.md) for payload structures)
