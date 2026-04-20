# Templates - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/templates

# Message Templates

![](https://lookaside.fbsbx.com/elementpath/media/?media_id=700974233679772&version=1751710035)![](https://lookaside.fbsbx.com/elementpath/media/?media_id=2391319097810789&version=1751710035)![](https://lookaside.fbsbx.com/elementpath/media/?media_id=447994142698870&version=1774561169)

Message templates offer a way for you to offer a richer in-conversation experience than standard text messages by integrating buttons, images, lists, and more alongside text a single message. Templates can be use for many purposes, such as displaying product information, asking the message recipient to choose from a pre-determined set of options, and showing search results.

## Available Templates

The following templates are available for sending structured messages:

* [Generic Template](/docs/messenger-platform/reference/template/generic)
* [Button Template](/docs/messenger-platform/reference/template/button)
* [Media Template](/docs/messenger-platform/reference/template/media)
* [Receipt Template](/docs/messenger-platform/reference/template/receipt)

## Request URI

```
https://graph.facebook.com/v25.0/me/messages?access_token={PAGE_ACCESS_TOKEN}
```

## Example Request

```
curl -X POST -H "Content-Type: application/json" -d '{
  "recipient":{
    "id":"<PSID>"
  },
  "message":{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"generic",
        "elements":[
           {
            "title":"Welcome!",
            "image_url":"https://raw.githubusercontent.com/fbsamples/original-coast-clothing/main/public/styles/male-work.jpg",
            "subtitle":"We have the right hat for everyone.",
            "default_action": {
              "type": "web_url",
              "url": "https://www.originalcoastclothing.com/",
              "webview_height_ratio": "tall"
            },
            "buttons":[
              {
                "type":"web_url",
                "url":"https://www.originalcoastclothing.com/",
                "title":"View Website"
              },{
                "type":"postback",
                "title":"Start Chatting",
                "payload":"DEVELOPER_DEFINED_PAYLOAD"
              }              
            ]      
          }
        ]
      }
    }
  }
}' "https://graph.facebook.com/v25.0/me/messages?access_token=<PAGE_ACCESS_TOKEN>"
```

## Example Response

```
{
  "recipient_id": "1254477777772919",
  "message_id": "AG5Hz2Uq7tuwNEhXfYYKj8mJEM_QPpz5jdCK48PnKAjSdjfipqxqMvK8ma6AC8fplwlqLP_5cgXIbu7I3rBN0P"
}
```

## Properties

### `recipient`

Description of the message recipient. All requests must include one of the following properties to identify the recipient.

Property | Type | Description || `recipient.id` | String | Page Scoped User ID (PSID) of the message recipient. The user needs to have interacted with any of the [Messenger entry points](/docs/messenger-platform/product-overview/entry-points) in order to opt-in into messaging with the Page. Note that [Facebook Login](/docs/facebook-login) integrations return user IDs are app-scoped and will not work with the Messenger platform. |
| `recipient.user_ref` | String | Used for the [checkbox plugin](/docs/messenger-platform/discovery/checkbox-plugin) |
| `recipient.post_id` | String | Used for [Private Replies](https://developers.facebook.com/docs/messenger-platform/discovery/private-replies) to reference the visitor post to reply to. |
| `recipient.comment_id` | String | Used for [Private Replies](https://developers.facebook.com/docs/messenger-platform/discovery/private-replies) to reference the post comment to reply to. |

### `message`

Description of the message to be sent.

Property | Type | Description || `message.attachment` | Object | An object describing attachments to the message. |

### `message.attachment`

Property | Type | Description || `type` | String | Value must be `template` |
| `payload` | Object | [`payload`](#payload) of the template. |

### `message.attachment.payload`

Property | Type | Description || `template_type` | String | Value indicating the template type `generic`, `button`, `media`, `receipt`, etc |
| `...` | Mixed | The rest of `message.attachment.payload` properties depend on the template type. See [Available templates](#available_templates). |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)