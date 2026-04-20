---
name: messenger
description: Comprehensive master skill for the Meta Messenger Platform, covering all API capabilities, webhooks, marketing messages, utility templates, and integration patterns.
---

# Messenger Platform Master Skill

This skill provides a complete operational framework for interacting with the Meta Messenger Platform, synthesized from the full developer documentation.

## When to use

- Implementing full-scale chatbot logic or human-agent handover systems.
- Setting up complex marketing automation via Recurring/Marketing Notifications.
- Configuring advanced UI elements like Persistent Menus, Personas, and specialized Templates.
- Troubleshooting API errors or handling diverse Webhook events (reactions, handovers, opt-ins, edits).
- Managing Page/User/Business Access Tokens and Meta App configurations.
- Sending Utility messages for order/account status updates.

## 1. Foundation & Authentication

### Meta App Setup
1. Create a Meta App and add the **Messenger** product.
2. Link the app to a Facebook Page.
3. Configure **Webhooks**: Set Callback URL and Verify Token.

### Permissions Required
- `pages_messaging`: Core messaging.
- `pages_show_list`: To see pages the user manages.
- `pages_manage_metadata`: For webhook configuration.
- `page_utility_messaging`: Required for Utility Messages.
- `marketing_messages_messenger` or `paid_marketing_messages`: For Marketing Messages.
- `ads_management`: For marketing message onboarding.

### Access Tokens
- **User Access Token**: Short-lived (~1h), obtained via Login.
- **Page Access Token**: Long-lived or non-expiring, used for most API calls.
- **System-Business Access Token**: Non-expiring, used for "Facebook Login for Business" / Marketing Messages Flow 1.
- **Graph API Endpoint**: `https://graph.facebook.com/v25.0/`

---

## 2. Webhook Master Reference

Configure your endpoint to handle `GET` (verification) and `POST` (events).

### Essential Events
- `messages`: Standard text, media, and quick replies.
- `messaging_postbacks`: Triggered by button clicks with `payload`.
- `messaging_optins`: Crucial for Marketing Messages (Recurring Notifications).
- `messaging_handovers`: `pass_thread_control`, `take_thread_control`, `request_thread_control`.
- `message_reads` & `message_deliveries`: Status tracking.

### Specialized Events
- `message_reactions`: User emoji reactions.
- `message_edits`: Payload includes `message_id` and the new `text`.
- `messaging_referrals`: Triggered by `m.me` links with parameters.
- `messaging_account_linking`: Handling account linking flows.
- `send_cart`: Triggered when a user sends a cart from a catalog.
- `messaging_game_plays`: Events for Instant Games.
- `standby`: Events received when NOT the primary receiver in a handover.
- `response_feedback`: User feedback from Customer Feedback templates.

---

## 3. Messaging Capabilities

### Send API (`POST /me/messages`)
Use `recipient` (PSID) and `message` objects.

### Messaging Window (24+1 Rule)
Standard messages can only be sent within 24 hours of the user's last message. Outside this window, use `MESSAGE_TAG`:
- `CONFIRMED_EVENT_UPDATE`
- `POST_PURCHASE_UPDATE`
- `ACCOUNT_UPDATE`
- `HUMAN_AGENT` (Allows 7-day window for human responses).

### Sender Actions
Use `mark_seen`, `typing_on`, and `typing_off` via `POST /me/messages` with `sender_action` field.

### Personas
Create virtual identities for bot/agents:
- **Create**: `POST /me/personas` (returns `persona_id`).
- **Use**: Add `"persona_id": "<ID>"` to message payload.

---

## 4. Assets & Attachment Management

### Saving Assets (Attachment Upload API)
Eliminates the need to upload files repeatedly.
- **Method A (Send API)**: Add `"is_reusable": true` in the `payload` of a message.
- **Method B (Upload API)**: `POST /me/message_attachments`.
- **Reuse**: Use the returned `attachment_id` in future payloads:
  ```json
  "attachment": { "type": "image", "payload": { "attachment_id": "<ID>" } }
  ```
- **Constraints**: Max size 25MB. Supported types: `image`, `audio`, `video`, `file`.

---

## 5. Advanced UI & Structured Templates

### Interactive Elements
- **Quick Replies**: Up to 13 buttons; disappear after use.
- **Persistent Menu**: Fixed menu for core navigation (`POST /me/messenger_profile`).

### Templates
- **Generic**: Horizontal carousel (up to 10 items) with images/buttons.
- **Button**: Text + 3 buttons.
- **Media**: High-res media with buttons.
- **Receipt**: Detailed order confirmations.
- **Coupon**: Promoting discounts with a `coupon_code`.
- **Customer Feedback**: Gather CSAT/NPS ratings.

---

## 6. Utility Messages

Used for non-marketing updates (orders, account status, appointments).
- **Permission**: `page_utility_messaging`.
- **Flow**:
  1. **Search**: `GET /message_template_library` to find Meta templates.
  2. **Clone**: `POST /<PAGE_ID>/message_templates` to copy to your Page.
  3. **Send**: `POST /<PAGE_ID>/messages` with `messaging_type: UTILITY`.
- **Parameter Formats**: Supports `NAMED` (e.g., `{{customer_name}}`) or `POSITIONAL` (e.g., `{{1}}`).

---

## 7. Marketing & Recurring Notifications

Send messages outside the 24h window for marketing purposes.
- **Flow**:
  1. Send **Opt-in Request** (Template type `notification_messages`).
  2. Receive `messaging_optins` webhook with `notification_messages_token`.
  3. Send messages using this token.
- **Onboarding Businesses**:
  - **Flow 1 (Business Portfolio)**: Generates non-expiring tokens. Best for Business Manager admins.
  - **Flow 2 (Asset-Based)**: Short-lived tokens. Best for Page/Ad Account admins without BM access.
- **Regional Constraints**: Generally available globally except EU, Japan, South Korea, Australia, UK.

---

## 8. Handover Protocol

Allows multiple apps to manage one thread.
- **Primary Receiver**: Usually the bot; receives all events.
- **Pass Thread**: Bot → Live Chat (`POST /me/pass_thread_control`).
- **Take Thread**: Live Chat → Bot (`POST /me/take_thread_control`).
- **Request Thread**: App requests control from Primary.

---

## 9. Best Practices & Policy

- **Avoid Spam**: Always provide an "Unsubscribe" path.
- **Latency**: Respond within 30 seconds to avoid user frustration.
- **Testing**: Use the **Graph API Explorer** to validate payloads.
- **Rate Limiting**: Formula: `200 * (Number of monthly active users)`.
- **Whitelisted Domains**: Must whitelist domains to open URLs in the Messenger Webview.

---

## 10. Error Handling Master List

- `100`: Invalid parameter (Check PSID or JSON structure).
- `200`: Permissions error (Check Token scopes).
- `551`: User unreachable (24h window closed or blocked).
- `613`: Rate limit exceeded (Implement exponential backoff).
- `2018034`: Message too long (Text limit is ~2000 characters).

---

## Reference Payloads

### Utility Message (Named Params)
```json
{
  "recipient": { "id": "<PSID>" },
  "message": {
    "template": {
      "name": "order_update",
      "language": { "code": "en" },
      "components": [
        {
          "type": "body",
          "parameters": [
            { "type": "text", "parameter_name": "order_id", "text": "12345" }
          ]
        }
      ]
    }
  }
}
```

### Save Asset (Attachment Upload)
```bash
curl -F 'message={"attachment":{"type":"image", "payload":{"is_reusable":true}}}' \
     -F 'filedata=@/path/to/image.png' \
     "https://graph.facebook.com/v25.0/me/message_attachments?access_token=<TOKEN>"
```
