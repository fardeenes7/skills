# Webhook Events - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/webhook-events

# Webhook Events Reference

Webhook events are how the Messenger Platform notifies your bot when a variety of interactions or events happen, including when a person sends a message. Webhook events are sent by the Messenger Platform as POST requests to your webhook.

**Note:** You will need to subscribe all messaging apps for your business to the messaging webhooks.

## List of Webhook Events

Below is a list of the events that can be sent to your webhook from the Messenger Platform.

**Note:** It is recommended that you use the latest API version to receive all information available for each webhook.

Messaging Webhooks Field | Description || `message_deliveries` | A notification is sent when a message that was sent by your business has been [delivered to a customer](/docs/messenger-platform/webhook-reference/message-delivered). Only available for Messenger conversations. |
| `message_echoes` | A notification is sent when [your business has sent a message](/docs/messenger-platform/webhook-reference/message-echo). This separate webhook field is available only for Messenger conversations. For Instagram Messaging conversations, the message echo notifications are included with the `message` webhook field subscription. |
| `message_edits` | A notification is sent when [a customer edits a previously-sent message](/docs/messenger-platform/reference/webhook-events/message-edit). Only availalbe for Messenger conversations. |
| `message_reactions` | A notification is sent when [a customer reacts to a message sent by your business.](/docs/messenger-platform/reference/webhook-events/message-reactions) |
| `message_reads` | A notification is sent when [a customer reads a message sent by your business, for Messenger conversations.](/docs/messenger-platform/webhook-reference/message-read) See `messaging_seen` for Instagram Messaging conversations. |
| `messages` | A notification is sent when your business has [received a message from a customer](/docs/messenger-platform/webhook-reference/message-received) from any conversation entry point. For Instagram Messaging, this subscription will also include notifications when your Instagram Professional account has sent a message since there is no separate `message_echoes` subscription field for Instagram Messaging. |
| `messaging_account_linking` | A notification is sent when a [customer links or unlinks their Messenger account from their account with your business.](/docs/messenger-platform/webhook-reference/account-linking) Only available for Messenger conversations. |
| `messaging_feedback` | A notification is sent when a person has [submitted feedback for your business.](https://developers.facebook.com/docs/messenger-platform/send-messages/templates/customer-feedback-template) Only available for Messenger conversations. |
| `messaging_game_plays` | A notification is sent when a person has played [a round of an Instant Game.](/docs/messenger-platform/reference/webhook-events/messaging_game_plays/) Only available for Messenger conversations. |
| `messaging_handovers` | A notification is sent when [a change has occurred during the Handover Protocol](/docs/messenger-platform/reference/webhook-events/messaging_handovers) |
| `messaging_optins` | A notification is sent when a customer has [clicked a Messenger plugin, accepted a message request using customer matching, or has opted in to receive messages via the checkbox plugin.](/docs/messenger-platform/reference/webhook-events/messaging_optins) Only available for Messenger conversations. |
| `messaging_policy_enforcement` | A notification is sent when [a policy enforcement warning has been sent or a policy enforcement action has been taken on the app associated with the Page.](/docs/messenger-platform/webhook-reference/policy-enforcement) |
| `messaging_postbacks` | A notification is sent when [a customer clicks a postback button, Get Started button, or persistent menu item for Messenger conversations or an Icebreaker option or Generic Template button for Instagram Messaging conversations.](/docs/messenger-platform/webhook-reference/postback-received) |
| `messaging_referrals` | A notification is sent when [a customer resumes a conversation with the Page by clicking an ig.me or m.me link, or an ad.](/docs/messenger-platform/webhook-reference/referral) |
| `messaging_seen` | A notification is sent when [a customer reads a message sent by your business, for Instagram Messaging conversations.](/docs/messenger-platform/webhook-reference/message-read) See `messaging_reads` for Messenger conversations. |
| `messenger_template_status_update` | A notification is sent when [a utility message template's review status has change](https://developers.facebook.com/docs/messenger-platform/send-messages/template/utility-messaging). |
| `response_feedback` | A notification is sent [when a customer provides feedback on a message sent by your business by clicking the feedback buttons](/docs/messenger-platform/reference/webhook-events/response_feedback). |
| `send_cart` | A notification is sent when your business has received a message from a customer, when the message contains cart/order information. Only available for Messenger conversations. |
| `standby` | A notification is sent when [a conversation is idle for an app during the Handover Protocol](/docs/messenger-platform/reference/webhook-events/standby) |

## Event Format

All callbacks for the Messenger Platform have a common set of properties that provide information you will need to process and respond to input from people using your bot. In addition to the properties below, each event also has a set of specific properties that detail the event.

```
{
  "object":"page",
  "entry":[
    {
      "id":"<PAGE_ID>",
      "time":1458692752478,
      "messaging":[
        {
          "sender":{
          "id":"<PSID>"
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

### Properties

Property | Type | Description || `object` | String | Value will be `page` |
| `entry` | Array of [`entry`](#entry) | Array containing event data |

### `entry`

Property | Type | Description || `id` | String | Page ID of page |
| `time` | Number | Time of update (epoch time in milliseconds) |
| `messaging` | Array<[`messaging`](#messaging)> | Array containing one [`messaging`](#messaging) object. Note that even though this is an array, it will only contain one `messaging` object. |

### `entry.messaging`

Property | Type | Description || `sender.id` | String | Sender user ID |
| `recipient.id` | String | Recipient user ID |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)