# Quick Replies - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/marketing-messages-on-messenger/send-messages/quick-replies

# Quick Replies

Quick replies provide a way to present a set of up to 13 buttons in-conversation that contain a title and optional image, and appear prominently above the composer. You can also use quick replies to request a person's location, email address, and phone number.

![](https://lookaside.fbsbx.com/elementpath/media/?media_id=668002490333314&version=1776079002)  

When a quick reply is tapped, the buttons are dismissed, and the title of the tapped button is posted to the conversation as a message. A `messages` event will be sent to your webhook that contains the button title and an optional payload.

For a complete list of request properties, see the [Quick Replies Reference](/docs/messenger-platform/reference/send-api/quick-replies/).

## Sending Quick Replies

To send a quick reply, add the `quick_replies` array to message, and include objects that define up to 13 quick reply buttons.

The following quick reply types are supported:

* [Text](#text)
* [Phone Number](#phone)
* [Email](#email)

```
{
  "message_id": "<MESSAGE_ID>",
  "messenger_delivery_data": {
    "subscription_token": "<SUBSCRIPTION_TOKEN>"
  },
  "message":{
   "quick_replies":[
      {
        "content_type":"text",
        "title":"Red",
        "payload":"{POSTBACK_PAYLOAD}",
        "image_url":"http://example.com/img/red.png"
      },{
        "content_type":"text",
        "title":"Green",
        "payload":"{POSTBACK_PAYLOAD}",
        "image_url":"http://example.com/img/green.png"
      }
    ]
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"generic",
        "elements":[
           {
            "title":"Welcome!",
            "image_url":"<IMAGE_URL>",
            "subtitle":"We have the right hat for everyone.",
            "buttons":[
              {
                "type":"web_url",
                "url":"<BUTTON_URL>",
                "title":"View Website"
              },{
                "type":"postback",
                "title":"Start Chatting",
                "payload":"<PAYLOAD_WEBHOOK>"
              }              
            ]      
          }
        ]
      }
    }
  }
}
```

### Webhook Event

When a quick reply is tapped, a text message will be sent to your webhook [Message Received Callback](/docs/messenger-platform/webhook-reference/message-received).

The `text` property of the event will correspond to the title of the Quick Reply. The message object will also contain a field named `quick_reply` containing the `payload` data on the Quick Reply.

```
{
  "object": "page",
  "entry": [
    {
      "id": "<PAGE_ID>",
      "time": 1502905976963,
      "messaging": [
        {
          "sender": {
            "id": "1254459154682919"
          },
          "recipient": {
            "id": "682498171943165"
          },
          "timestamp": 1502905976377,
          "message": {
            "quick_reply": {
              "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_GREEN"
            },
            "mid": "m_AG5Hz2Uq7tuwNEhXfYYKj8mJEM_QPpz5jdCK48PnKAjSdjfipqxqMvK8ma6AC8fplwlqLP_5cgXIbu7I3rBN0P",
            "text": "Green"
          }
        }
      ]
    }
  ]
}
```

## User Phone Number Quick Reply

![](https://scontent.fdac31-2.fna.fbcdn.net/v/t39.2365-6/23417458_1117232598379764_7436715136921894912_n.png?_nc_cat=103&ccb=1-7&_nc_sid=e280be&_nc_ohc=Y0Ic7thylOMQ7kNvwEA6qQj&_nc_oc=Adqn9sNZIWTv0iW7T-sdnVLJ8l6BF8wPkWDTq3as_HJXQbPld1ByaploU8osyVbtNPM&_nc_zt=14&_nc_ht=scontent.fdac31-2.fna&_nc_gid=eUvtHmF8XL36yNOlsyJ4OA&_nc_ss=7a30f&oh=00_Af1bQ9NIPqKYm2T_OdSBK9C0NtlUIagfzqU6yWczU0dWtQ&oe=6A002BEB)

The user phone number quick reply allows you to ask a user for their phone number. When the phone number quick reply is sent, the Messenger Platform will automatically pre-fill the displayed quick reply with the phone number from the user's profile information.

If the user's profile does not have a phone number, the quick reply will not be shown.

The bot will not receive the phone number until the user clicks the quick reply.

Choosing the quick reply transmits the information once and does not constitute permission to access the information in the future.

### Syntax

```
{
  "content_type":"user_phone_number"
}
```

### Webhook Event

When the user taps the quick reply, the phone number will be passed in the `payload` attribute of the `messages` webhook event.

```
{
  "object": "page",
  "entry": [
    {
      "id": "<PAGE_ID>",
      "time": 1502905976963,
      "messaging": [
        {
          "sender": {
            "id": "1254459154682919"
          },
          "recipient": {
            "id": "682498171943165"
          },
          "timestamp": 1502905976377,
          "message": {
            "quick_reply": {
              "payload": "<PHONE_NUMBER>"
            },
            "mid": "m_AG5Hz2Uq7tuwNEhXfYYKj8mJEM_QPpz5jdCK48PnKAjSdjfipqxqMvK8ma6AC8fplwlqLP_5cgXIbu7I3rBN0P",
            "text": "<PHONE_NUMBER>"
          }
        }
      ]
    }
  ]
}
```

## User Email Quick Reply

![](https://scontent.fdac31-1.fna.fbcdn.net/v/t39.2365-6/27807597_203144990422079_3327502058327638016_n.png?_nc_cat=110&ccb=1-7&_nc_sid=e280be&_nc_ohc=bHJin6l03pcQ7kNvwE3kENH&_nc_oc=AdrKbWL-nWEsNiSAwSqGiOrpAj7W59FwYMWREJR7NC-p061GFPVINI1MxoruLH8Ei80&_nc_zt=14&_nc_ht=scontent.fdac31-1.fna&_nc_gid=eUvtHmF8XL36yNOlsyJ4OA&_nc_ss=7a30f&oh=00_Af0cTTD0Xk70CJJUGlUGgkcD0vzYKHqVBKXM5q2K7E3z0w&oe=6A005CBA)

The user email quick reply allows you to ask a user for their email. When the email quick reply is sent, the Messenger Platform will automatically pre-fill the displayed quick reply with the email from the user's profile information.

If the user's profile does not have an email address, the quick reply will not be shown.

The bot will not receive the email until the user clicks the quick reply.

Choosing the quick reply transmits the information once and does not constitute permission to access the information in the future.

### Syntax

```
{
  "content_type":"user_email"
}
```

### Webhook Event

When the user taps the quick reply, the email address will be passed in the `payload` attribute of the `messages` webhook event.

```
{
  "object": "page",
  "entry": [
    {
      "id": "<PAGE_ID>",
      "time": 1502905976963,
      "messaging": [
        {
          "sender": {
            "id": "1254459154682919"
          },
          "recipient": {
            "id": "682498171943165"
          },
          "timestamp": 1502905976377,
          "message": {
            "quick_reply": {
              "payload": "<EMAIL_ADDRESS>"
            },
            "mid": "m_AG5Hz2Uq7tuwNEhXfYYKj8mJEM_QPpz5jdCK48PnKAjSdjfipqxqMvK8ma6AC8fplwlqLP_5cgXIbu7I3rBN0P",
            "text": "<EMAIL_ADDRESS>"
          }
        }
      ]
    }
  ]
}
```

## Properties

Property | Type | Description || `content_type` | String | Must be one of the following   * `text`: Sends a text button * `user_phone_number`: Sends a button allowing recipient to send the phone number associated with their account. * `user_email`: Sends a button allowing recipient to send the email associated with their account. |
| `title` | String | Required if `content_type` is 'text'. The text to display on the quick reply button. 20 character limit. |
| `payload` | String, Number | Required if `content_type` is 'text'. Custom data that will be sent back to you via the `messaging_postbacks` webhook event. 1000 character limit.   May be set to an empty string if `image_url` is set. |
| `image_url` | String | ***Optional.*** URL of image to display on the quick reply button for text quick replies. Image should be a minimum of 24px x 24px. Larger images will be automatically cropped and resized.   Required if `title` is an empty string. |

## Best Practices

Use quick replies to prompt for specific next steps.

Be brief — long quick replies will be truncated.

Don't use for actions you'd like to be permanent: quick replies disappear after the next message.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)