# Button Template  - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/templates/button

# Button Template Reference

![](https://scontent.fdac31-1.fna.fbcdn.net/v/t39.2365-6/23204276_131607050888932_1057585862134464512_n.png?_nc_cat=106&ccb=1-7&_nc_sid=e280be&_nc_ohc=E5d8nRhpXzQQ7kNvwFe6ea2&_nc_oc=AdrF70PTeBUhe1PMFr0Kb99D_SqPyyTsdhkI8J1Gl53UCvtbkhnnm4_z32jsO9gHP6c&_nc_zt=14&_nc_ht=scontent.fdac31-1.fna&_nc_gid=05iFAjcoA6-xVAq6vVSukg&_nc_ss=7a30f&oh=00_Af27Tfyv2gvFmqXg0jReczE0ietIgST-AHNii1jkys7nqQ&oe=6A004636)

The button template allows you to send a structured message that includes text and buttons. For complete implementation details, see [Button Template](/docs/messenger-platform/send-api-reference/button-template).

## Request URI

```
https://graph.facebook.com/v25.0/me/messages?access_token={PAGE_ACCESS_TOKEN}
```

## Example Request

```
curl -X POST -H "Content-Type: application/json" -d '{
  "recipient":{
    "id":"{PSID}"
  },
  "message":{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"button",
        "text":"What do you want to do next?",
        "buttons":[
          {
            "type":"web_url",
            "url":"https://www.messenger.com",
            "title":"Visit Messenger"
          }
        ]
      }
    }
  }
}' "https://graph.facebook.com/v25.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
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

Property | Type | Description || `template_type` | String | Value must be `button` |
| `text` | String | UTF-8-encoded text of up to 640 characters. Text will appear above the buttons. |
| `buttons` | Array<button> | Set of 1-3 [buttons](/docs/messenger-platform/send-api-reference/buttons) that appear as call-to-actions. |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)