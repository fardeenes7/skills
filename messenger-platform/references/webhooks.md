# Webhooks Reference

## Configuration
- **Callback URL**: Must be HTTPS and return `200 OK`.
- **Verify Token**: A secret string you choose for subscription validation.
- **Page Subscriptions**: Ensure your app is subscribed to the correct Page(s), not only configured at app level.

## Security (X-Hub-Signature)
Meta signs payloads. Validate using:
1. Read `X-Hub-Signature-256`.
2. Compute HMAC SHA256 of the **raw request body** using your App Secret.
3. Compare against `sha256=<digest>` with a timing-safe equality check.

## Event Coverage
| Event Field | Purpose |
| :--- | :--- |
| `messages` | Incoming user messages (text, attachments, replies, fallback attachments). |
| `messaging_postbacks` | CTA/postback button clicks with developer payloads. |
| `message_reads` | Read receipts and watermark progression. |
| `message_echoes` | Echoes of Page-sent messages for synchronization/analytics. |
| `message_deliveries` | Delivery receipts (`watermark`, optional `mids`). |
| `message_reactions` | Emoji reactions added/removed on messages. |
| `message_edits` | User edited an existing message. |
| `messaging_optins` | Marketing notification opt-in updates and token lifecycle events. |
| `messaging_handovers` | Pass/take/request thread control and app role changes. |
| `messaging_referrals` | Referral context from m.me links or ads for existing threads. |
| `messaging_account_linking` | Account linked/unlinked events with pass-through authorization data. |
| `response_feedback` | Good/bad response feedback from users on bot responses. |
| `send_cart` | Cart/order payloads from commerce-related interactions. |
| `group_feed` | Facebook Group comment events for private-reply use cases. |
| `standby` | Events delivered while your app is not current thread owner. |
| `messaging_game_plays` | Instant Games play-session events and context metadata. |

## Webhook Object Structure
```json
{
  "object": "page",
  "entry": [
    {
      "id": "<PAGE_ID>",
      "time": 1458692752478,
      "messaging": [
        {
          "sender": { "id": "<PSID>" },
          "recipient": { "id": "<PAGE_ID>" },
          "timestamp": 1458692752478,
          "message": { "text": "Hello world!" }
        }
      ]
    }
  ]
}
```

## Reliability and Processing Patterns
- **Respond fast**: Return `200 OK` within ~5 seconds and process business logic asynchronously.
- **Deduplicate**: Use `mid` + idempotency keys to suppress retries.
- **Ordering**: Use `timestamp` and per-thread sequencing when processing concurrently.
- **Ownership-aware routing**: Handle `standby` and `messaging_handovers` when multiple apps control the same thread.
- **Delivery/read state**: Use `message_deliveries` and `message_reads` to update message-state timelines.

## Practical Subscriptions Guidance
- Subscribe only to events you handle in production.
- Add `messaging_optins`, `messaging_handovers`, and `standby` when implementing recurring notifications or multi-app routing.
- Add `group_feed` and `send_cart` only when your Page workflows require those vertical features.
