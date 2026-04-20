# message_deliveries  - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/message-deliveries

# `message_deliveries` Webhook Event Reference

This callback will occur when a message a Page has sent has been delivered. You can subscribe to this callback by selecting the `message_deliveries` field when [setting up](/docs/messenger-platform/webhook-reference#setup) your webhook.

## Example

```
{
  "sender":{
    "id":"<PSID>"
  },
  "recipient":{
    "id":"<PAGE_ID>"
  },
   "delivery":{
      "mids":[
         "mid.1458668856218:ed81099e15d3f4f233"
      ],
      "watermark":1458668856253
   }
}
```

## Properties

### `sender`

`sender` Field | Description || `id` *string* | The Page-scoped ID for the person who sent a message to your business |

### `recipient`

`recipient` Field | Description || `id` *string* | The ID for your Facebook Page |

### `delivery`

Property | Type | Description || `mids` | Array | Array containing message IDs of messages that were delivered. Field may not be present. |
| `watermark` | Number | All messages that were sent before this timestamp were delivered |

Both `mids` and `watermark` fields are used to determine which messages were delivered. `watermark` is always present and `mids` is sometimes present. `mids` provides delivery receipts on a per-message basis but may not be present (due to backward compatibility reasons with older Messenger clients). `watermark` is always present and is a timestamp indicating that all messages with a timestamp before `watermark` were delivered.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)