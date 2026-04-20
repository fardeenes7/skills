# message_reads - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/message-reads

# `message_reads` Webhook Event Reference

This event will be sent to your webhook when a message a Page has sent has been read by the user.  
You can subscribe to this callback by selecting the `message_reads` field when [setting up](/docs/messenger-platform/webhook-reference#setup) your webhook.

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
   "read":{
      "watermark":1458668856253
   }
}
```

## Properties

### `sender`

`sender` Field | Description || `id` *string* | The Page-scoped ID for the person who sent a message to your business |

### `recipient`

`recipient` Field | Description || `id` *string* | The ID for your Facebook Page |

### `read`

Property | Type | Description || `watermark` | Number | All messages that were sent before or at this timestamp were read |

The `watermark` field is used to determine which messages were read. It represents a timestamp indicating that all messages with a timestamp before `watermark` were read by the recipient.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)