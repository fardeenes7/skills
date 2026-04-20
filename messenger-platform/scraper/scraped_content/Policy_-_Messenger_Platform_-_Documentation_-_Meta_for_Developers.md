# Policy - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/policy

# Messenger Platform and IG Messaging API policy

Our [Developer Policies](/devpolicy) apply to Messenger Platform and Instagram Messaging API and are designed to help people and businesses connect effectively through Messenger and Instagram to achieve meaningful outcomes. At the heart of this is the understanding that people and businesses need a seamless, reliable way to get something done — whether it is getting a question answered, making a purchase, or communicating important and relevant updates. People expect businesses to respond quickly, and businesses that respond to user messages faster can see better business outcomes. The policies and requirements are designed to encourage businesses and developers to:

1. Respond to customers in a timely fashion when they reach out
2. Share important updates that are personally relevant to their customers

The following is an overview of standard messaging, message tag, and news messaging policies. For complete details on applicable policies, see the [Platform Terms](/terms) and [Developer Policies](/devpolicy).

* **Standard Messaging** — Businesses have up to 24 hours to respond to a user. Messages sent within the 24-hour window may contain promotional content. People expect businesses to respond quickly, and businesses that respond to users in a timely manner achieve better outcomes. Responding to people's messages as soon as possible is highly encouraged.
* **Message Tags** — Enable businesses to send important and personally relevant 1:1 updates to users outside the 24-hour standard messaging window. A number of message tags are available to support certain use cases. Some tags are available on both Messenger Platform and IG Messaging API, while others are applicable only to Messenger Platform. The message tags include a Human Agent tag that allows businesses to manually respond to user messages within a 7-day period. Learn more [here](/docs/messenger-platform/send-messages/message-tags).
* **One-time Notification** — Enable businesses to request a user to send one follow-up message after the 24-hour messaging window has ended. Learn more [here](/docs/messenger-platform/send-messages/one-time-notification). One-time notifications are not available for IG Messaging API.
* **News messaging** — Only Pages registered with the [News Page Index (NPI)](https://www.facebook.com/help/publisher/316333835842972) are allowed to send non-promotional news messages. News messaging is not available for IG Messaging API.
* **Sponsored Messages** — [Sponsored messages](/docs/messenger-platform/discovery/ads/sponsored-messages) allow businesses to send promotional content outside the standard messaging window. Sponsored messages are not available for IG Messaging API.

#### Informing users about your automated experience

When required by applicable law, automated chat experiences must disclose that a person is interacting with an automated service:

* at the beginning of any conversation or message thread,
* after a significant lapse of time, or
* when a chat moves from human interaction to automated experience.

Automated chat experiences that serve the following groups should pay special attention to this requirement:

* California market or California users
* German market or German users

Disclosures may include but are not limited to: “I’m the [Page Name] bot,”“You are interacting with an automated experience,” “You are talking to a bot,” or “I am an automated chatbot.”

Even where not legally required, we recommend informing users when they’re interacting with an automated chat as best practice, as this helps manage user expectations about their interaction with your messaging experience.

Visit our [Developer Policies](/devpolicy/#messengerplatform) for more information.

## Standard messaging

Businesses have up to 24 hours to respond to a user. Messages sent within the 24-hour window may contain promotional content. Users have the option to block or mute a conversation with a business at any time.

Here are examples of the user actions that open the 24-hour standard messaging window on Messenger Platform:

* User sends a message to the Page
* User clicks a call-to-action button like Get Started within a Messenger conversation
* User clicks on a Click-to-Messenger ad and then starts a conversation with the Page
* User starts a conversation with a Page via a plugin, such as [Send to Messenger plugin](/docs/messenger-platform/discovery/send-to-messenger-plugin) or the [Checkbox plugin](/docs/messenger-platform/discovery/checkbox-plugin)
* User clicks on an m.me link with a ref parameter on an existing thread
* User reacts to a message (see [Replies and Reactions](/docs/messenger-platform/webhook/reply_and_reactions))

For information on how you may be able to send messages outside the 24-hour messaging window, see [Message Tags](/docs/messenger-platform/send-api-reference/tags) and [Sponsored Messages](/docs/messenger-platform/discovery/ads/sponsored-messages).

## Message tags

Message tags enable sending important and personally relevant updates to users outside the 24-hour standard messaging window, for a set of approved use cases. For complete details on allowed use cases, see the list of supported [message tags](/docs/messenger-platform/send-messages/message-tags). Use of tags outside of approved use cases may result in restrictions on your ability to send messages. Some message tags are available only for Messenger Platform and not IG Messaging API.

## One-time notification

Messenger Platform's [One-Time Notification API (Beta)](/docs/messenger-platform/send-messages/one-time-notification) allows a page to send a time-sensitive and personally relevant notification for use cases (such as back-in-stock alerts) where someone has explicitly requested to receive a one-time follow-up message. Once the user asks to be notified, the page receives a token equivalent to a permission to send a single message to the user. The token can only be used once and expires within 1 year of creation. Learn more [here](/docs/messenger-platform/send-messages/one-time-notification). One-time Notification is not available for IG Messaging API.

## Private replies

When users create a post comment or a visitor post on a Page, [Private Replies](/docs/messenger-platform/discovery/private-replies) allows the Page to send a single message as a reply using Messenger Platform. Private replies are currently allowed within 7 days of the referenced user action. Along with the message sent, the user also receives a reference to their post comment or visitor post. For private replies using Instagram Messaging API, see [Private Replies](/docs/messenger-platform/instagram/features/private-replies).

## News messaging

News messages allow news publishers to send regular news updates to their subscribers in Messenger. This feature is only available for registered news Pages under the [News Page Index (NPI)](https://www.facebook.com/help/publisher/316333835842972) and is not available for Instagram Messaging API. Pages registered with the News Page Index don't need to apply for news messaging permission.

News messaging applies to news content only, and must not be used for promotional content, including but not limited to subscription offers, deals, coupons, discounts, or content produced by or that promotes a third party (such as branded content or affiliate marketing). To send news messages, NPI-registered pages need to use the `NON_PROMOTIONAL_SUBSCRIPTION` message tag. Use of news messaging outside of these approved use cases may result in restrictions on your ability to send news messages.

## Sponsored messaging

[Sponsored Messages](/docs/messenger-platform/discovery/ads/sponsored-messages) allow businesses to reengage with people who have an open conversation with their Page in Messenger. Sponsored messages can be sent outside the 24-hour standard messaging window and can include both promotional and non-promotional content. Sponsored messages are annotated in the conversation with the word "Sponsored" above the message.

Sponsored message content must comply with [advertising policies](https://www.facebook.com/policies/ads/). For more information on sending sponsored messages, see [Sponsored messages](/docs/messenger-platform/discovery/ads/sponsored-messages). Sponsored messages are not available for IG Messaging API.

## Responsiveness requirements

To ensure the best user experience possible, the Messenger Platform requires automated bots to respond to all user input within a specific amount of time.

### Responsiveness policy

* Automated bots must respond to **any and all input** from the user. "Any input" is defined as freeform text, quick replies, CTA buttons, and persistent menu clicks. The Get Started (welcome screen) button is excluded from this requirement.
* Automated bots that have disabled the composer must still respond to any other available inputs.
* Automated bots must respond to user input **within 30 seconds**. This ensures your bot's experience feels like a continuous conversation.

### Which bots does this apply to?

The Messenger Platform's responsiveness policy applies to all bots that are identified as "automated" (not "hybrid" or "human") that are submitted for approval via the App Dashboard.

Messenger Platform categorizes bots into three types depending on how the bot communicates with its audience. When your bot was launched on Messenger, you, or another page admin defined your bot type in the App Dashboard or Discover submission form:

* **Automated bots:** All responses from the bot are programmed ahead of time. The bot doesn't require any manual intervention in order to function. For example, a bot that provides news and weather updates.
* **Manual Reply:** All responses from the bot are provided by live representatives. For example, a bot for a business that communicates with its customers through third-party CRM software. People who message the bot don't get a response until someone from the business responds manually.
* **Hybrid bots:** Bots that incorporate both automated and human interactions. For example, a bot for an airline that lets you check your flight status instantly (automated) but can also connect you to a customer service representative to make changes to your reservation (human).

## Accepting Page Contact Terms to use Custom Labels

In order to use the Custom Labels API, businesses (Page admins) need to accept the *Page Contact Terms*. These terms describe Meta's data practices for the Custom Labels created by the business.

Follow these steps to prepare for this requirement and avoid any business disruption:

1. Provide an option within your tools to inform Page admins that they need to accept the Page Contact Terms if the business wants to add, edit, or delete labels for any of their customers. Provide an interstitial or dialog within your app and have the page admins or business click on a call-to-action button that redirects the page admin to the Page Contact Terms landing page. Here is suggested copy for the interstitial or dialog box:

*[Partner to translate as appropriate]*
*Hi Page name, to use labels that sync with your Facebook Page Inbox, you must first accept the Page Contact Terms. You can continue to create, update, and delete labels once you have accepted these terms.*

1. Call the custom labels endpoint. If the Page hasn't accepted the terms, the API call returns an error with a link to the Page Contact Terms. When the API returns an error, you can surface a pop-up in your tool as suggested in step 1. The Page needs to accept the Page Contact Terms only once when they are using labels via your platform.

## Policy violation notifications

If a Page is restricted from sending messages due to a violation of Developer Policies, the Page receives an explanation of the policy violation in an email sent to the Page Support Inbox for the app. To ask questions about a policy violation notification, respond to this email and a Policy team member may respond.

To access the Page Support Inbox, click **Page Support Inbox** in the left sidebar of your Page settings.

If your bot is found to be in violation of the responsiveness policy, all Page admins are notified through the Page Support Inbox. That message links to this documentation and provides instructions for bringing your bot into compliance.

### Responding to policy violations

* If your bot is intended to provide an automated experience, adhere to the [responsiveness requirements](#responsiveness_policy).
* If your bot is a [hybrid or human experience](#what_bots), update your bot's response setting in **Page Settings** > **Advanced Messaging**.

If you don't respond or make the appropriate changes within 7 days, your bot's ability to send messages may be limited. If you have questions after being notified, respond via the Page Support Inbox. Expect a response within 3 business days.

## Platform terms and community standards

These terms and policies outline the allowed usage of the Platform, including the Messenger Platform. Review these terms and policies for details on what and how you can build on the Platform.

* [Platform Terms](/terms)
* [Developer Policies](/devpolicy)
* [Community Standards](https://www.facebook.com/communitystandards)

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)