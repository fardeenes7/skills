# Messaging & Send API

## Standard Messaging Window (24+1 Rule)
Businesses have **24 hours** to respond to a user's message. 
- Any message sent within this window can be of any type (promotional or non-promotional).
- After 24 hours, you **MUST** use a **Message Tag** or a **Marketing Message Token**.

## Message Tags
Used to send non-promotional updates outside the 24h window.
- `CONFIRMED_EVENT_UPDATE`: Reminders for booked events.
- `POST_PURCHASE_UPDATE`: Invoices, shipping updates.
- `ACCOUNT_UPDATE`: Security alerts, change in status.
- `HUMAN_AGENT`: Allows human agents to respond within **7 days** (Beta).

## Send API Structure
**Endpoint**: `POST /v25.0/me/messages`
**Payload Example**:
```json
{
  "messaging_type": "RESPONSE",
  "recipient": { "id": "<PSID>" },
  "message": { "text": "Hello!" }
}
```

## Structured Templates
Templates allow you to send rich UI elements.

### Generic Template
Horizontal carousel of up to 10 bubbles.
- **Title**: 80 characters.
- **Subtitle**: 80 characters.
- **Buttons**: Up to 3 per bubble.

### Button Template
Text followed by up to 3 buttons.
- Ideal for simple call-to-actions.

### Media Template
High-res image or video with optional buttons.
- Supports Facebook/Instagram native videos.

### Receipt Template
Detailed order summary.
- Includes `order_number`, `currency`, `payment_method`, and `summary`.

### Customer Feedback Template
Gathers CSAT or NPS scores.
- Customizable scales (1-5, 1-10, or emoji-based).

## Interactive Elements
- **Quick Replies**: Up to 13 buttons that disappear after use.
- **Sender Actions**: `mark_seen`, `typing_on`, `typing_off`.
- **Persistent Menu**: Bottom-aligned navigation menu.

## Attachment Upload API
Use `POST /me/message_attachments` to save media and get an `attachment_id`.
- **Reuse**: Reuse the ID in the Send API to avoid re-uploading.
- **Limit**: Max file size is 25MB.
