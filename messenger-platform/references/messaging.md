# Messaging & Send API

## Standard Messaging Window (24h Policy)
Businesses have **24 hours** to respond after a user interaction.
- Inside this window, messages can be promotional or non-promotional.
- Outside this window, use approved mechanisms: **Message Tags**, **Marketing Messages**, or other policy-approved paths.

## Message Tags
Used for approved non-promotional updates outside the 24h window:
- `CONFIRMED_EVENT_UPDATE`
- `POST_PURCHASE_UPDATE`
- `ACCOUNT_UPDATE`
- `HUMAN_AGENT` (extended manual response window)

## Send API Structure
- **Endpoint**: `POST /v25.0/me/messages`
- **Base payload**:
```json
{
  "messaging_type": "RESPONSE",
  "recipient": { "id": "<PSID>" },
  "message": { "text": "Hello!" }
}
```

## Core Message UI Components
- **Conversation Components**: build message flows from text, attachments, quick replies, and postbacks.
- **Buttons**: postback, URL, and other call-to-action formats.
- **Quick Replies**: up to 13 one-tap responses that collapse after use.
- **Sender Actions**: `mark_seen`, `typing_on`, `typing_off`.
- **Persistent Menu**: fixed navigation surface configured in Messenger Profile.

## Structured Templates
### Generic Template
Carousel-style cards (up to 10 bubbles), with title/subtitle/buttons.

### Button Template
Text + up to 3 buttons for focused decisions.

### Media Template
Single rich media card (image/video) with optional action buttons.

### Receipt Template
Order summary and transactional detail (`order_number`, `currency`, `payment_method`, `summary`).

### Customer Feedback Template
Post-interaction rating collection (CSAT/NPS-like patterns).

### Coupon Template
Coupon-style presentation for promotional and campaign use cases.

## Asset Reuse (Saving Assets)
- Use `is_reusable: true` in Send API attachment payloads to receive an `attachment_id`.
- Or upload in advance using `POST /me/message_attachments`.
- Reuse `attachment_id` to avoid repeated uploads.
- Supported types include image/audio/video/file (size limits apply; commonly 25MB max in Messenger docs).

## Marketing Message Interaction Building Blocks
- Marketing notification flows often use **postbacks** and **quick replies** for opt-in journeys.
- Keep payload design explicit and versioned for safe routing.

## Policy-Driven Messaging Notes
- One-time and recurring notification mechanisms are opt-in driven and token based.
- Keep a compliance-safe split between promotional and utility/transactional traffic.
- Preserve audit trails for messaging type, tag, token origin, and consent updates.
