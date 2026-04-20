# Parsed Docs Coverage Matrix

This matrix maps the parsed Messenger Platform docs corpus to this skill so coverage can be audited quickly.

## 1) Platform Foundations, Setup, and Governance
- **Overview / Get Started / Quick Start / Sample App / Create App**: represented across onboarding flow in `authentication.md` and skill workflow in `SKILL.md`.
- **Policy**: 24-hour standard window, tags, and compliance expectations represented in `messaging.md` + `troubleshooting.md`.
- **General Best Practices / Rate Limits**: represented in `webhooks.md` and `troubleshooting.md`.
- **Support Resources + FAQ**: represented in `troubleshooting.md` support and debugging sections.

## 2) Authentication and Identity
- **Facebook Login token flows** (user, page, long-lived/system user tokens): `authentication.md`.
- **Permission model** (`pages_messaging`, `pages_manage_metadata`, `instagram_manage_messages`, `page_utility_messaging`, `marketing_messages_messenger`): `authentication.md`.
- **Scoped IDs** (`PSID`, `IGSID`, `SID`): `authentication.md`.

## 3) Core Messaging and UX Components
- **Send API / Send Messages**: `messaging.md`.
- **Buttons / Quick Replies / Sender Actions / Persistent Menu**: `messaging.md`.
- **Templates**: generic, button, media, receipt, customer feedback, coupon in `messaging.md`.
- **Saving Assets / Attachment reuse**: `messaging.md`.
- **Conversation Components**: `messaging.md`.

## 4) Marketing and Utility Messaging
- **Marketing Messages on Messenger** (opt-in flow, token handling, onboarding businesses): `advanced_features.md`.
- **Get subscription tokens / Send marketing messages / quick reply + postback usage**: `advanced_features.md` + `messaging.md`.
- **Utility Messages**: `advanced_features.md`.

## 5) Specialized Platform APIs
- **Messenger Profile API** (get started button, greeting, ice breakers, persistent menu, domain allowlist, account linking URL, commands): `advanced_features.md`.
- **Conversations API** (list conversations, list messages, message detail retrieval, ownership filtering): `advanced_features.md`.
- **Reference-level API orientation** (Send API + templates): `messaging.md` and `webhooks.md`.

## 6) Webhook Events Coverage
`webhooks.md` includes setup/security plus event handling guidance for:
- `messages`
- `messaging_postbacks`
- `message_reads`
- `message_echoes`
- `message_deliveries`
- `message_reactions`
- `message_edits`
- `messaging_optins`
- `messaging_handovers`
- `messaging_referrals`
- `messaging_account_linking`
- `response_feedback`
- `send_cart`
- `group_feed`
- `standby`
- `messaging_game_plays`

## 7) Errors, Operations, and Escalation
- **Error Codes** (token, permission, window, payload size, user block, rate limiting): `troubleshooting.md`.
- **Operational checks** (status pages, retries/backoff, dedupe, webhook reliability): `troubleshooting.md`.
- **Escalation paths** (Meta Support, developer tools, bug reports, support inbox): `troubleshooting.md`.

## Notes on Source Normalization
- Duplicate source entries (`Get_Started`/`Get_started`, repeated access-token links, repeated template links) were normalized into single consolidated guidance sections.
- Where parsed docs are highly granular (for example individual webhook event pages), this skill consolidates them into operationally grouped references while preserving event-level coverage.
