# standby - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/standby

# `standby` Webhook Event Reference

For bots using the [handover protocol](/docs/messenger-platform/handover-protocol) and [conversation routing](https://developers.facebook.com/docs/messenger-platform/conversation-routing/), this callback will occur when a message has been sent to your page, but your application is not the current thread owner.

Instead of delivering the callback through the normal `messaging` channel, the events will be delivered to `standby` channel. You can receive [message](/docs/messenger-platform/webhook-reference/message), [read](/docs/messenger-platform/webhook-reference/message-read), and [delivery](/docs/messenger-platform/webhook-reference/message-delivered) events through history messages.

You can subscribe to this callback by selecting the `standby` field when [setting up](/docs/messenger-platform/webhook-reference#setup) your webhook.

### Contents

* [Supported Events](#events)
* [Example Event](#example)
* [Properties](#properties)

## Supported Events

The following events are delivered to the standby channel:

* [`message_reads`](/docs/messenger-platform/reference/webhook-events/message-reads)
* [`message_deliveries`](/docs/messenger-platform/reference/webhook-events/message-deliveries)
* [`messages`](/docs/messenger-platform/reference/webhook-events/messages)
* [`messaging_postbacks`](/docs/messenger-platform/reference/webhook-events/messaging-postbacks)

Note that `messaging_postback` events delivered via the Standby channel will not include the postback payload. The app that originally sent the [postback button](/docs/messenger-platform/reference/buttons/postback) will receive the normal [`messaging_postbacks`](/docs/messenger-platform/reference/webhook-events/messaging-postbacks) webhook event that includes the postback payload.

## Example Event

```
{
  "object":"page",
  "entry":[
    {
      "id":"<PAGE_ID>",
      "time":1458692752478,
      "standby":[
        {
          "sender":{
            "id":"<USER_ID>"
          },
          "recipient":{
            "id":"<PAGE_ID>"
          },

          ...
        }
      ]
    }
  ]
}
```

## Properties

Property | Type | Description || `id` | String | The PSID of the user that triggered the webhook event. |
| `time` | Timestamp | Timestamp of the message send. |
| `standby` | Array | Array of messages received in the standby channel. |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)