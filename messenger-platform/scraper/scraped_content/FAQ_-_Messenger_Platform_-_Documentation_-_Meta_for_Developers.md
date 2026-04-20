# FAQ - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/faq

# FAQ

This document provides answers to frequently asked questions.

## General

[How do I install a Messenger App?](#faq_1118717252087125)

Apps are installed from the app website using [Facebook Login](https://developers.facebook.com/docs/facebook-login/) and granting pages\_messaging permission to a particular Page. Authorized Apps will show up in **Page settings** inside **Advanced messaging**.

[Permalink](#faq_1118717252087125)

[Can my bot interact with more that one Facebook Page?](#faq_794706507548422)

Yes, a single Facebook app can subscribe to multiple pages. Once it goes for app review, like the permission pages\_messaging, the app can subscribe to receive webhooks on more than one page. It will be up to you to get the context of each webhook based on the payload.

[Permalink](#faq_794706507548422)

[Can I have more than one bot connected to a page?](#faq_756446964718979)

Yes, more than one app can be subscribed to a page. When multiple apps handle the same conversation is best to use the [Handover Protocol](https://developers.facebook.com/docs/messenger-platform/handover-protocol/) to handle which bot owns the thread at any given time.

[Permalink](#faq_756446964718979)

## General Data Protection Regulation (GDPR)

[Where can I get information on GDPR as it relates to the Messenger Platform?](#faq_2194463294115771)

To read FAQs on GDPR and the Messenger Platform, please visit [The Messenger Platform and the General Data Protection Regulation](https://www.facebook.com/business/m/messenger-and-the-gdpr).

[Permalink](#faq_2194463294115771)

## Entry Points

[How do I link a plugin click or my user account to a thread?](#faq_1450300814995685)

When using the [“Send to Messenger” Plugin](https://developers.facebook.com/docs/messenger-platform/plugin-reference/send-to-messenger), the **data-ref** parameter can be used by you as a pass-through-parameter to send through any information regarding the context of the click.

People may also discover your page through search in Messenger. In these cases, you won't have a pass-through-parameter. You can use the [account linking feature](https://developers.facebook.com/docs/messenger-platform/account-linking) to associate a thread to a user account on your site.

[Permalink](#faq_1450300814995685)

## One-time Notification API

[Is the one-time notification API a replacement for Subscriptions?](#faq_518175165499788)

No. Unlike subscriptions where a business can send multiple messages to people on a recurring basis, the one-time notification API limits the business to a single message per user request. If the person engages with the message, the standard messaging window will reopen.

[Permalink](#faq_518175165499788)

[Will Pages need to request special permission to use the One-time Notification API?](#faq_2448565868582746)

Yes. Pages interested in using the One-time Notification API need to apply for [permission](/docs/messenger-platform/send-messages/one-time-notification#permissions). Go to the **Advanced Messaging** section of your **Page Settings** and consent to the terms. A Page will be granted permission if the Page meets our criteria.

[Permalink](#faq_2448565868582746)

[What are some examples of common uses the API supports?](#faq_196246274797021)

Common uses of the API include various promotional and non-promotional use cases where the User explicitly requested a follow-up. Examples include:

* Back in stock alerts
* Collection launches
* Concert tickets going on sale
* Price drop alerts
* Train tickets available for purchase
* CSAT surveys

[Permalink](#faq_196246274797021)

[What are some examples of use cases the API does not support?](#faq_173363340631823)

Your Page is not allowed to send a notification on a topic for which the User has not agreed to receive a notification. Please see the [Usage](/docs/messenger-platform/send-messages/one-time-notification#usage) and [Restrictions and Limitations](/docs/messenger-platform/send-messages/one-time-notification#restrictions) sections of the One-time Notification guide for more information.

[Permalink](#faq_173363340631823)

[How many one-time notification requests can a Page send to a user?](#faq_3388285774521044)

A Page can send multiple requests however, the [24-hour policy](/docs/messenger-platform/send-messages/one-time-notification#summary) will be applied to all the requests being sent. We also have [controls in place](/docs/messenger-platform/send-messages/one-time-notification#usage) to prevent spamming users with multiple requests.

[Permalink](#faq_3388285774521044)

[Will the 24 hour standard messaging window re-open when a Page sends the opt-in follow-up message?](#faq_2628164980749203)

The 24 hour standard messaging window will open **only** if the user interacts with the opt-in message. The behavior is consistent with interactions with other elements in the Messenger experience.

[Permalink](#faq_2628164980749203)

[How will a Page know when a person has provided consent to be notified about a topic?](#faq_800614983783882)

Pages will need to subscribe to [message\_optins webhook](/docs/messenger-platform/reference/webhook-events/messaging_optins) to receive notifications about User consent.

[Permalink](#faq_800614983783882)

[Once a user asks to be notified, what does the Page need to do?](#faq_690320155039800)

Once a person asks to be notified, the Page will receive a token which is equivalent to a permission to send a single message to the person. The token can be used to send a message to the person outside the 24 hour window. The token can only be used once and unused tokens will expire within 1 year of creation.

[Permalink](#faq_690320155039800)

[Can a Page use a token to send another notification request to the User?](#faq_845302582578611)

Yes. However, while it is possible to send another notification request using an existing token, there is no clear benefit for the business to send these type of requests.

[Permalink](#faq_845302582578611)

[If a Page uses the token to send a message within the 24 hour standard messaging window, will the token expire?](#faq_617140938855649)

Token is for one-time use only. Once a token is used it can not be used again.

[Permalink](#faq_617140938855649)

[Will a Page be able to request a list of all tokens available for use?](#faq_596748474218298)

No. The API does not return tokens available to a Page.

[Permalink](#faq_596748474218298)

[Is the permission for the One-time Notification API provided at the app level or Page level?](#faq_265815877733359)

Page level. [Permissions](/docs/messenger-platform/send-messages/one-time-notification#permissions) for the One-time Notification API are given at the Page level.

[Permalink](#faq_265815877733359)

[Does the app need to specify a message tag for messages sent to the person using the One-time Notification API?](#faq_184400496130869)

No. The app does not need to specify any message tags when sending a message outside the 24-hour standard messaging window using this API.

[Permalink](#faq_184400496130869)

## Send/Receive API

[Why do I get an "Invalid ID" or "No matching user found" error when sending a message?](#faq_1077831102283110)

There are multiple reasons why this may happen:

* **You're using an ID from Facebook Login.** User IDs from Facebook Login are not intended to work with the Send/Receive API. Only user IDs obtained through authentication with the Messenger Platform will [work with the Messenger Platform](https://developers.facebook.com/docs/messenger-platform/send-api-reference#request).
* **You're using an ID with the incorrect Page Access Token.** User IDs for the Messenger Platform are scoped to a page and, therefore, are page specific. If you use a valid user ID but with a page access token that's associated with a different page, the call will not work. Be sure to use the user ID and page access token associated with the same page.
* **You're sending to a phone number that hasn't been recently verified.** When using the Send API with a phone number, we will only send messages if the [phone number has been **recently** verified](https://developers.facebook.com/docs/messenger-platform/send-api-reference#phone_number). Even if the phone number is shown as verified, but has not been recently verified, then the send may fail. Re-verify your phone number and wait 24 hours until trying again.

[Permalink](#faq_1077831102283110)

[Why can't I send messages to test platform users?](#faq_1060511397319219)

Here is a workaround to use a platform test user for your messenger platform integration:

1. From your app's [Roles page](https://developers.facebook.com/apps/89000000000000/roles/test-users/), create a new test user by clicking the Add button.
2. Toggle the **Authorize Test Users for This App?** option and grant permissions *"page\_messaging"*.
3. Use the Edit Button and get an access token for this user (using v4.0). Please save this for later.
4. Use the **Edit** button to login as the test user.
5. After logging in, create a page as the test user.
6. Use the user access token for the test user to get the page access token for this user. You can do this with the following call:

   ```
   https://graph.facebook.com/v4.0/me/accounts?access_token=[TEST_USER_ACCESS_TOKEN]
   ```

   ([Documentation](https://developers.facebook.com/docs/graph-api/reference/user/accounts/))
7. Use this page access token to link your Facebook Application with your Page:

   ```
   https://graph.facebook.com/v4.0/me/subscribed_apps?method=POST&access_token=[TEST_USER_PAGE_ACCESS_TOKEN]
   ```

   ([Documentation](https://developers.facebook.com/docs/messenger-platform/implementation#subscribe_app_pages))
8. After you have followed these steps you will receive RTU updates to your Test Page and be able to message your Test User from your Test Page.
   In addition to the above you can replace your access token with a long-lived token if they are expiring too quickly for your tests. Please follow the documentation [here](https://developers.facebook.com/docs/facebook-login/access-tokens/expiration-and-extension):

   ```
   GET /oauth/access_token?  
       grant_type=fb_exchange_token&           
       client_id={app-id}&
       client_secret={app-secret}&
       fb_exchange_token={short-lived-token}
   ```

[Permalink](#faq_1060511397319219)

[Can my app use both standard messaging and message tags to send messages?](#faq_110014459704061)

If your business tries to send an update message that falls under one of the approved use cases in message tags, we’d recommend you to still tag it using messaging\_type=MESSAGE\_TAG with an appropriate message tag. That way you don’t need to keep track of whether a conversation is still within under the 24-hour window in standard messaging.

[Permalink](#faq_110014459704061)

[What happens if my bot messages a person more than once beyond the 24-hour standard messaging window?](#faq_1821413868169699)

Under the standard messaging policy apps can't send messages outside the 24-hour window. The message will fail to be sent. If a message tag is used the message can be sent outside the 24 hour period as long as is one of the supported use cases and the app is in good standing.

[Permalink](#faq_1821413868169699)

[Is there a way to retrieve a list of PSIDs for all the people that have messaged my bot?](#faq_1828292257467693)

No, the Messenger Platform does not offer an API that returns a list of PSIDs for all the people that have opted in to receive messages from your bot.

[Permalink](#faq_1828292257467693)

## Webhooks

[Why am I not receiving a callback to my webhook?](#faq_1564982133798449)

There are 2 steps to receiving callbacks. First, make sure your webhook is setup properly (https://developers.facebook.com/docs/messenger-platform/webhook-reference#setup). There is an indicator when webhooks are properly setup.

Second, you must subscribe to each page. All pages that are subscribed to will be listed.

![](https://scontent.fdac31-2.fna.fbcdn.net/v/t39.2365-6/13695315_1141730795884980_248654944_n.png?_nc_cat=103&ccb=1-7&_nc_sid=e280be&_nc_ohc=H38TDtKKaLgQ7kNvwFodY6h&_nc_oc=AdrZtZXGHiZ6iwGyoLw8WLdDJAxb2LtND2hP0u25YDukYE1gpFeLxwS5J1XQCK8MRAQ&_nc_zt=14&_nc_ht=scontent.fdac31-2.fna&_nc_gid=t7Ym9POESh7M0rY3IQhssQ&_nc_ss=7a30f&oh=00_Af03btzPWuXJtNPhlnyPcxn2gKLjGseXWFiYHlTRqsR2Ig&oe=6A004EB6)

If calls to your webhook [fail for an extended period of time](https://developers.facebook.com/docs/messenger-platform/webhook-reference#unsubscribe), your app will be unsubscribed and you will have to re-add your webhook and re-subscribe your page.

[Permalink](#faq_1564982133798449)

[How do I verify that the webhook call is coming from Facebook for security reasons?](#faq_2051998055025355)

Calls to the webhook contain a field in the header named [X-Hub-Signature](https://developers.facebook.com/docs/messenger-platform/webhook-reference#security), which can be used to validate that the call came from Facebook.

[Permalink](#faq_2051998055025355)

[Why do I keep on getting developer alerts that my webhook has not been accepting updates, or keep getting the same webhook calls repeatedly?](#faq_144542125979728)

Make sure your webhook is [responding with a status code of 200](https://developers.facebook.com/docs/messenger-platform/webhook-reference#response). This communicates to us that the webhook was successfully received. If you do not return a 200, we will retry the call until successfully completed. Also, if a webhook doesn't return a 200 for an extended period of time, we will surface developer alerts.

Also, note that a successful status code is returned in a timely manner. A webhook call with timeout after 20 seconds. Be sure to architecture your code such that webhooks are processed asynchronously so that a successful status code can be returned immediately and processed separately.

[Permalink](#faq_144542125979728)

[How can I see Messenger webhook errors?](#faq_903932453303273)

There is a tool that shows recent webhook errors. If webhooks are failing to be delivered, Meta servers will unsubscribe your URL. To find the tool, go into your App dashboard > Messenger > Settings, inside the Webhooks card there is a button called **Show recent errors**

[Permalink](#faq_903932453303273)

## See Also

* See our [Facebook App Management FAQ](/docs/apps/management-faqs) for any questions about managing access to your Facebook apps.
* Visit our Help Center for articles on:
  + [Ads Creation for Messenger Bots](https://www.facebook.com/business/help/1420905584664062)
  + [Structured Messages for Messenger](https://www.facebook.com/business/help/1646890868956360)

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)