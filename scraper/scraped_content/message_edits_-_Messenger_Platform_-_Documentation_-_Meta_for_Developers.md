# message_edits - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/message-edits

# `message_edits` Webhook Event Reference

This event will be sent to your webhook when a user edits a previously-sent message.  
You can subscribe to this callback by selecting the `message_edits` field when [setting up](/docs/messenger-platform/webhook-reference#setup) your webhook.

## Example

```
{
  "sender": {
    "id": "<PSID>"
  },
  "recipient": {
    "id": "<PAGE_ID>"
  },
  "timestamp": 1458668856463,
  "message_edit": {
    "mid": "<MESSAGE_ID>",
    "text": "<TEXT>",
    "num_edit": "<INT>",
  }
}
```

## Properties

### `sender`

`sender` Field | Description || `id` *string* | The Page-scoped ID for the person who sent a message to your business |

### `recipient`

`recipient` Field | Description || `id` *string* | The ID for your Facebook Page |

### `message_edit`

Property | Type | Description || `mid` | string | The Message ID of the message that the user edited. |
| `text` | string | The new message content, after the user's edit. |
| `num_edit` | integer | The number of times the user has edited the message. (The user cannot edit a message more than five times. This constraint is on the Messenger client side.) |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)