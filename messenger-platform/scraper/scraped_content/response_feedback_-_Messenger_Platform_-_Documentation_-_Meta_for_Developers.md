# response_feedback - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/response_feedback

# `response_feedback` Webhook Event Reference

This event will be sent to your webhook when a user provides feedback on a message on Messenger. Users provide feedback by clicking the "thumbs up"/"thumbs down" buttons or by pressing the "Good response"/"Bad response" buttons. You can subscribe to this callback by selecting the `response_feedback` field when setting up your webhook.

By subscribing to the `response_feedback` field for a particular page, all messages sent by your app on behalf of that page will have the response feedback options in the message thread. If you do not want those options in the thread, you can unsubscribe from the webhook field.

## User Experience

Once you subscribe to the response\_feedback webhook event, users will see the feedback options in thread in the two following ways:

|  |  |  |
| --- | --- | --- |
| Thumbs up and thumbs down buttons | Good response and bad response buttons in long press menu | Once the user successfully submits the feedback, they will see the following submission confirmation: |

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
   "response_feedback":{
         "feedback": "Good response | Bad response",
         "mid": "<Message-id>",
   }
}
```

## Properties

### `sender`

`sender` Field | Description || `id` *string* | The Page-scoped ID for the person who sent a message to your business |

### `recipient`

`recipient` Field | Description || `id` *string* | The ID for your Facebook Page |

### `response_feedback`

Property | Type | Description || `feedback` | string | Feedback, provided by the user, on the business message.  Possible values: `Good response`, `Bad response` |
| `mid` | string | Reference to the |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)