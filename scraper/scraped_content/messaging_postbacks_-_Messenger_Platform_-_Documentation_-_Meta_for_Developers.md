# messaging_postbacks  - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messaging_postbacks

# `messaging_postbacks` Webhooks Reference

This document explains the JSON payload your webhooks server will receive when a messaging postback webhook event is triggered. A postback webhook event is triggered when a person clicks a postback button, Get Started button, or persistent menu item.

## Example Notification

The following is an example of the JSON payload that will be sent to your webhooks server.

```
{
  "field": "messaging_postbacks",
  "value": {
    "sender": {
      "user_ref": "USER-REF-ID"
    },
    "recipient": {
      "id": "PAGE-ID"
    },
    "timestamp": "1527459824",
    "postback": {
      "mid": "m_MESSAGE-ID",
      "title": "TITLE-FOR-THE-CTA",
      "payload": "USER-DEFINED-PAYLOAD",
      "referral": {
        "ref": "USER-DEFINED-REFERRAL-PARAM",
        "source": "SHORT-URL",
        "type": "OPEN_THREAD"
      }
    }
  }
}
```

### JSON Properties

All JSON properties in a webhook notification are strings.

Property | Description || `postback.mid` | The ID for the message |
| `postback.payload` | Information defined in the CTA `payload` parameter. This is only included in the webhook notification sent to the app that sent the message to the person. |
| `postback.referral` | Information about the action the person took to enter a conversation.  The `referral` property information is included in the webhook notification only when a person starts a conversation using one of the following then clicking a CTA such as a Get Started button:   * An m.me Link * A Click to Messenger Ad * A Messenger QR Code * A Welcome Screen |
| `postback.referral.ref` | The arbitrary data that was originally passed in the `ref` param added to the m.me link. Only alphanumeric characters as well as -, \_, and = are supported |
| `postback.referral.source` | The URL for this referral. For m.me links, the value of source is `“SHORTLINK”`. For referrals from Messenger Conversation Ads, the value of source is `"ADS"` |
| `postback.referral.type` | The identifier for the referral. For referrals coming from m.me links, it will always be `"OPEN_THREAD"`. |
| `postback.title` | The title for the Call To Action (CTA) that a person clicked |
| `recipient.id` | The ID for your Facebook Page |
| `sender.user_ref` | The ID for the reference for a person who took an action, such as clicked a Get Started, or Persistent Menu item, that sent a message |
| `timestamp` | The Unix timestamp for date when the webhook notification was sent to your server |

## See Also

Additional developer documentation to further your understanding of concepts mentioned in this Messaging Postbacks Webhooks guide.

* [Get Started Button](/docs/messenger-platform/messenger-profile/get-started-button)
* [Handover Protocol - Standby Webhooks](/docs/messenger-platform/webhook-reference/standby-channel)
* [`m.me` Links](/docs/messenger-platform/referral-params)
* [Messenger QR Code](/docs/messenger-platform/messenger-code)
* [Persistent Menu Item](/docs/messenger-platform/messenger-profile/persistent-menu)
* [Postback Button](/docs/messenger-platform/send-api-reference/postback-button)

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)