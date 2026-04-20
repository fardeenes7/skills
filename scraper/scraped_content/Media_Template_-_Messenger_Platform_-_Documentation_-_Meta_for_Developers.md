# Media Template - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/templates/media

# Media Template Reference

![](https://scontent.fdac31-2.fna.fbcdn.net/v/t39.2365-6/23666967_188506161716866_2869776016224550912_n.png?_nc_cat=101&ccb=1-7&_nc_sid=e280be&_nc_ohc=7Gwg0489wTIQ7kNvwHU4IEO&_nc_oc=AdoMMZ9h9myTbWu5WKP5NiXDATjT9KTc8xBr_e-D5ExRVnS3u6KU0MLyhMHbVYZ43Uo&_nc_zt=14&_nc_ht=scontent.fdac31-2.fna&_nc_gid=1mZ19azP7l5JTynnnNtR5g&_nc_ss=7a30f&oh=00_Af1VcD3oH9wc_uckJLyEq8zDxsMC6JYn6AxPbbf4Ox5h7Q&oe=6A003E5B)![](https://scontent.fdac31-2.fna.fbcdn.net/v/t39.2365-6/23065701_1942345712696886_5686788878908784640_n.png?_nc_cat=100&ccb=1-7&_nc_sid=e280be&_nc_ohc=pNiLgtBaRvsQ7kNvwEaDJf6&_nc_oc=Adqu7AdsKLso639LzRi-1rcg7Yf7jml4M1RZoqNKNN_LrTGhV1B-0SNbi_RL5s9hNxM&_nc_zt=14&_nc_ht=scontent.fdac31-2.fna&_nc_gid=1mZ19azP7l5JTynnnNtR5g&_nc_ss=7a30f&oh=00_Af3P3IrlrWS1_nCrYe1320DaGJ6fKOCc5GFohL5k1m6Lyw&oe=6A00555F)

The media template allows you to send a structured message that includes an image or video, and an optional button. For complete implementation details, see [Media Template](/docs/messenger-platform/send-api-reference/media-template).

## Request URI

```
https://graph.facebook.com/v25.0/me/messages?access_token={PAGE_ACCESS_TOKEN}
```

## Example Request

### Send with Attachment ID

```
curl -X POST -H "Content-Type: application/json" -d '{
  "recipient":{
    "id":"<PSID>"
  },
  "message":{
    "attachment": {
      "type": "template",
      "payload": {
         "template_type": "media",
         "elements": [
            {
               "media_type": "<image|video>",
               "attachment_id": "<ATTACHMENT_ID>"
            }
         ]
      }
    }    
  }
}' "https://graph.facebook.com/v25.0/me/messages?access_token=<PAGE_ACCESS_TOKEN>"
```

### Send with Facebook URL

```
curl -X POST -H "Content-Type: application/json" -d '{
  "recipient":{
    "id":"<PSID>"
  },
  "message":{
    "attachment": {
      "type": "template",
      "payload": {
         "template_type": "media",
         "elements": [
            {
               "media_type": "<image|video>",
               "url": "<FACEBOOK_URL>"
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

Property Name | Type | Description || `template_type` | String | Value must be `media` |
| `elements` | Array<[`element`](#elements)> | An array containing 1 [element](#elements) object that describe the media in the message. A maximum of 1 element is supported. |
| `sharable` | Boolean | ***Optional.*** Set to `true` to enable the native share button in Messenger for the template message. Defaults to `false`. |

### `message.attachment.payload.elements`

Property Name | Type | Description || `media_type` | String | The type of media being sent - `image` or `video` is supported. |
| `attachment_id` | String | The attachment ID of the image or video. Cannot be used if `url` is set. |
| `url` | String | The URL of the image. Cannot be used if `attachment_id` is set. |
| `buttons` | Array | An array of [button](/docs/messenger-platform/send-api-reference/buttons) objects to be appended to the template. A maximum of 3 button is supported. |

## Error Codes

Error Code | Description || 2018173 | Failed to generate preview url |
| 2018175 | Media Preview Failed |
| 2018182 | Media Type not valid |
| 2018183 | Attachment Id is missing |
| 2018184 | Media Template Facebook Media URL Is Not Supported |
| 2018185 | Non facebook url in url param |
| 2018186 | Unable to get photo or video from facebook url |
| 2018187 | Either URL or attachment id is required |
| 2018188 | External URL is not supported |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)