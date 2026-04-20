# Get started - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/marketing-messages-on-messenger/get-started

# Get Started with Marketing Message API for Messenger

This guide provides an overview of the integration steps for the Marketing Message API for Messenger, enabling businesses to send paid marketing messages.

The Marketing Message API for Messenger is available exclusively to [**tech providers**](https://developers.facebook.com/docs/development/release/tech-providers/) with an existing app that has successfully completed [Meta App Review](/docs/app-review) for the following permissions:

* ads\_management
* pages\_messaging
* paid\_marketing\_messages or marketing\_messages\_messenger

  

Currently, tech providers can only serve **businesses** located in the following regions:

|  |  |  |  |
| --- | --- | --- | --- |
| * Australia * Brazil * Chile * Colombia * Hong Kong | * India * Indonesia * Israel * Malaysia * Mexico | * New Zealand * Peru * Philippines * Saudi Arabia * Singapore | * Taiwan * Thailand * United Arab Emirates * United States * Vietnam (VN) |

In addition, messages can be sent to **users/subscribers** in all regions **except**:

|  |
| --- |
| * European Union * Japan * South Korea * Australia * United Kingdom |

  

The Marketing Message API for Messenger is only available for Web applications.

## Preparation

Prepare the following items to ensure a smooth integration with the Marketing Message API for Messenger:

* A [Meta developer account](https://developers.facebook.com/docs/development/register/)
* A [Facebook Page](https://www.facebook.com/business/help/473994396650734), [Meta business portfolio](https://www.facebook.com/business/help/1710077379203657)(optional), and a [Meta ad account that is eligible for marketing messages in Ads Manager](https://www.facebook.com/business/help/407323696966570) to use as test accounts. Ensure the ad account has a payment method set up. Follow this [guide](https://www.facebook.com/business/help/354027251751870) for setting up payment.
* You must have an established **Business type** [Meta app](https://developers.facebook.com/docs/development/create-an-app).
  + Your app must be in [Live mode](https://developers.facebook.com/docs/development/build-and-test/app-modes/) for testing the product.
  + Your app must have these 3 required features:
    - [Messenger product](https://developers.facebook.com/docs/messenger-platform/) configured with the Facebook Page you intend to use.
    - [Facebook Login for Business](https://developers.facebook.com/docs/facebook-login/facebook-login-for-business/)
    - [Ads Management Standard Access](https://developers.facebook.com/docs/features-reference/ads-management-standard-access/)
  + Your app must have **Advanced access** for 3 required permissions:
    - `ads_management`
    - `pages_messaging`
    - `paid_marketing_messages` or `marketing_messages_messenger`
* A server that can receive [Messenger webhook event notifications](https://developers.facebook.com/docs/messenger-platform/webhooks/#event-notifications).
* The app should be owned by a Meta business portfolio that is different from the one associated with your test accounts (Facebook Page, Meta business portfolio, and Meta ad account).

## Integration overview

The following steps outline the typical integration flow for supporting businesses in sending paid Marketing Messages:

Step | Summary || 1: Onboarding | Create a new Facebook Login for Business configuration in the [Meta App Dashboard](/apps) to onboard businesses using your app. This new configuration asks businesses for the required permissions, access tokens, assets, and to sign the Terms of Service. |
| 2: Get a list of existing subscribers | **Businesses can only send Marketing Messages to people who have opted in to receive them.**  Get a list of a business' subscription tokens that represent people who have opted in to receive Marketing Messages from that business. |
| 3: Sending messages | You will need to support businesses in composing and sending of Marketing Messages by building a UI in your app. Once you're ready to send the Marketing Message campaign, select one of two API options:   * [A simplified endpoint](https://developers.facebook.com/docs/marketing-messages-on-messenger/send-messages) - **our recommended option** which is easier to integrate with and covers most marketing messages needs, or * [A traditional endpoint that uses the Marketing API](https://developers.facebook.com/docs/marketing-messages-on-messenger/additional-resources/send-messages-mapi). |
| 4: Monitor results | Integrate with Meta's insights and basic campaign management APIs to allow businesses using your app to view metrics for marketing message campaign performance. |
| 5: Grow marketing messages audience  (Optional but recommended) | This step is optional if the onboarded business already has the required number of subscribers who have agreed to receive marketing messages from the business. However, we strongly encourage that your app users continue to keep growing their subscriber base.   * Multiple options are available to increase subscribers, such as turning those who clicked Click-to-Messenger ads into subscribers. |

## Next Steps

Now that you understand the integration steps, you can begin the [onboarding process](https://developers.facebook.com/docs/marketing-messages-on-messenger/onboard-businesses).

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)