# Webhooks Reference

## Configuration
- **Callback URL**: Must be HTTPS and return `200 OK`.
- **Verify Token**: A string you choose to verify the subscription.

## Security (X-Hub-Signature)
Meta signs all payloads. Validate using:
1. Get the `X-Hub-Signature-256` header.
2. Calculate HMAC SHA256 of the raw request body using your **App Secret**.
3. Compare (prefixed with `sha256=`).

## Event Reference
| Field | Trigger |
| :--- | :--- |
| `messages` | Incoming text, images, or quick reply data. |
| `messaging_postbacks` | User clicked a button with a `payload`. |
| `message_reads` | User viewed your message. |
| `message_echoes` | Page sent a message (useful for multi-agent sync). |
| `messaging_optins` | User accepted a Recurring Notification or clicked a plugin. |
| `messaging_handovers` | Thread control was passed/taken. |
| `message_reactions` | User added/removed an emoji reaction. |
| `message_edits` | User modified a previously sent message. |

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

## Best Practices
- **Respond Fast**: Meta expects a `200 OK` within 5 seconds. Process logic asynchronously.
- **Deduplication**: Use `mid` (message ID) to avoid processing the same event twice if Meta retries.
- **Chronological Order**: Use the `timestamp` field to ensure messages are processed in order.
