# message_reactions - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/message-reactions

# `message_reactions` Webhook Event Reference

This event will be sent to your webhook when a user reacts to a message on Messenger.  
You can subscribe to this callback by selecting the `message_reactions` field when [setting up](/docs/messenger-platform/webhook-reference#setup) your webhook.

## Example

```
{
   "sender":{
      "id":"<PSID>"
   },
   "recipient":{
      "id":"<PAGE_ID>"
   },
   "timestamp":1458668856463,
   "reaction":{
         "reaction": "smile|angry|sad|wow|love|like|dislike|other",
         "emoji": "\u{2764}\u{FE0F}",
         "action": "react|unreact",
         "mid": "<MID_OF_ReactedTo_Message>",
   }
}
```

## Properties

### `sender`

`sender` Field | Description || `id` *string* | The Page-scoped ID for the person who sent a message to your business |

### `recipient`

`recipient` Field | Description || `id` *string* | The ID for your Facebook Page |

### `reaction`

Property | Type | Description || `reaction` | string | Text description of the reaction. Possible values: `smile`, `angry`, `sad`, `wow`, `love`, `like`, `dislike`.   `other` could also be returned in case the emoji based reaction does not match the ones above. |
| `emoji` | UTF-8 Emoji | Reference to the emoji corresponding to the reaction. |
| `action` | string | Action performed by the user. Possible values: `react`, `unreact` |
| `mid` | string | Reference to the Message ID that the user reacted performed the reaction on. |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)