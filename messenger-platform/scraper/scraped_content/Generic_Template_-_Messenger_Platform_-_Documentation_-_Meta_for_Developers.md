# Generic Template  - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/templates/generic

# Generic Template Reference

![](https://scontent.fdac31-2.fna.fbcdn.net/v/t39.2365-6/22880422_1740199342956641_1916832982102966272_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=K-lOZK7Cl2EQ7kNvwET-BLN&_nc_oc=AdrQRz3Q7t4nuzudZVgC2sxwAe326PyFioSof_EVnSQi1gIv3hwLW57OjEbWtsjUmRk&_nc_zt=14&_nc_ht=scontent.fdac31-2.fna&_nc_gid=2pUfzZCtURZ0vwpf9MJn8g&_nc_ss=7a30f&oh=00_Af1kPQIxzYEk81bi5M73XOoHaaITX6Oz9WID_BkG1okPiQ&oe=6A003204)

The generic template allows you to send a structured message that includes an image, text and buttons. A generic template with multiple templates described in the [`elements`](#elements) array will send a horizontally scrollable carousel of items, each composed of an image, text and buttons. For complete implementation details, see [Generic Template](/docs/messenger-platform/send-api-reference/generic-template/).

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

Property Name | Type | Description || `template_type` | String | Value must be `generic` |
| `elements` | Array<[`element`](#elements)> | An array containing 1 [element](#elements) object that describe the media in the message. A maximum of 1 element is supported. |
| `sharable` | Boolean | ***Optional.*** Set to `true` to enable the native share button in Messenger for the template message. Defaults to `false`. |

### `message.attachment.payload.elements`

The generic template supports a maximum of 10 elements per message. At least one property must be set in addition to `title`.

Property Name | Type | Description || `title` | String | The title to display in the template. 80 character limit. |
| `subtitle` | String | ***Optional.*** The subtitle to display in the template. 80 character limit. |
| `image_url` | String | ***Optional.*** The URL of the image to display in the template. |
| `default_action` | Object | ***Optional.*** The default action executed when the template is tapped. Accepts the same properties as [URL button](/docs/messenger-platform/send-api-reference/url-button), except `title`. |
| `buttons` | Array<[`button`](/docs/messenger-platform/reference/buttons)> | ***Optional.*** An array of [buttons](/docs/messenger-platform/send-api-reference/buttons) to append to the template. A maximum of 3 buttons per element is supported. |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)