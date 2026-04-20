# messaging_referrals  - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messaging_referrals

# `messaging_referrals` Webhook Event Reference

This callback will occur when the user already has a thread with the bot and user comes to the thread from:

* Following an [m.me link with a referral parameter](/docs/messenger-platform/referral-params)
* Clicking on a [Messenger Conversation Ad](/docs/messenger-platform/guides/ads)

For tracking referrals in new threads, refer to [Postback Event](/docs/messenger-platform/webhook-reference/postback-received).

To start receiving these events you need to subscribe to `messaging_referrals` in the webhook settings for your app.

### Contents

* [Examples](#examples)
  + [m.me Links](#m-me)
  + [Ad Referral](#ads)
* [Properties](#properties)

## Examples

### m.me Link

```
{
  "sender": {
    "id": "<PSID>"
  },
  "recipient": {
    "id": "<PAGE_ID>"
  },
  "timestamp": 1458692752478,
  "referral": {
    "ref": <REF_DATA_PASSED_IN_M.ME_PARAM>,
    "source": "SHORTLINK",
    "type": "OPEN_THREAD",
  }
}
```

### Ad Referral

```
{
  "sender": {
    "id": "<PSID>"
  },
  "recipient": {
    "id": "<PAGE_ID>"
  },
  "timestamp": 1458692752478,
  "referral": {
    "ref": <REF_DATA_IF_SPECIFIED_IN_THE_AD>,
    "ad_id": <ID_OF_THE_AD>,
    "source": "ADS",
    "type": "OPEN_THREAD",
    "ads_context_data": {
      "ad_title": <TITLE_OF_THE_AD>,
      "photo_url": <URL_OF_THE_IMAGE_FROM_AD_THE_USER_IS_INTERESTED_IN>,
      "video_url": <THUMBNAIL_URL_OF_THE_VIDEO_FROM_THE_AD>,
      "post_id": <ID_OF_THE_POST>,
      "product_id": <PRODUCT_ID>,
      "flow_id": <ID_OF_THE_PARTNER_APP_WELCOME_MESSAGE_FLOW>
    }
  }
}
```

For more information about the flow ID, please refer to [Welcome Message Flows](https://developers.facebook.com/docs/messenger-platform/ads/ads-welcome-message-flows).

## Properties

### `sender`

`sender` Field | Description || `id` *string* | The Page-scoped ID for the person who sent a message to your business |

### `recipient`

`recipient` Field | Description || `id` *string* | The ID for your Facebook Page |

### `referral`

Property | Type | Description || `source` | String | The source of the referral. Supported values:   * `ADS` * `SHORTLINK` |
| `type` | String | The referral type. Currently supports `OPEN_THREAD`. |
| `ref` | String | The optional `ref` attribute set in the referrer. Only alphanumeric characters as well as -, \_, and = are supported. |
| `referer_uri` | String | The URI of the site where the message was sent. |
| `ads_context_data` | Object | The data contaning information about the CTM ad, the user initiated the thread from. |

### `ads_context_data`

Property | Type | Description || `ad_title` | String | Title of the Ad. |
| `photo_url` | String | [Optional] Url of the image from the Ad the user is interested. |
| `video_url` | String | [Optional] Thumbnail url of the the video from the ad. |
| `post_id` | String | ID of the post. |
| `product_id` | String | [Optional] Product ID from the Ad the user is interested. |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)