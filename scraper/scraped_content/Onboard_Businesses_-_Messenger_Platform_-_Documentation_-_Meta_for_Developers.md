# Onboard Businesses - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/marketing-messages-on-messenger/onboard-businesses

# Onboard Businesses with Marketing Message API for Messenger

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

This document shows you how to configure Facebook Login for Business to onboard businesses to your Marketing Messages on Messenger app.

**NOTE:** In this guide, **business** refers to the business portfolios onboarding to your app (your app's user).

## Choose Your Onboarding Flow

We provide two onboarding flows for Marketing Messages on Messenger. Please decide which one works for your business needs before starting integration. You can also integrate with both onboarding flows to serve different use cases.

Feature | Flow 1: Business Portfolio Flow (SUAT) | Flow 2: Asset-Based Flow (UAT) || **Admin Permission Required** | Business Portfolio permission | Full control permission for Pages and Ad Accounts |
| **Asset Requirement** | Ad Account and Page need to be **owned** by the same Business Portfolio | Ad Account and Page **does not** need to be owned by the same Business Portfolio |
| **Key Permission** | `paid_marketing_messages` | `marketing_messages_messenger` |
| **Access Token Type** | System-business access token (non-expiring) | User access token (short-lived, ~1 hour) |
| **Additional Features** | Enables subscriber automations | Enables subscriber automations |
| **Best For** | Businesses with Business Manager access | Admins managing Pages and Ad Accounts without Business Manager access |

**Recommendation:** Use Flow 1 (Business Portfolio Flow) if the admin for the Business is onboarding, as it provides higher level of authentication and the token doesn't expire. Use Flow 2 (Asset-Based Flow) if the admin for the business is not available or the Ad Account and Page are not owned by the same business.

## Before You Start

* Go to [Your App](https://developers.facebook.com/apps) > `Messenger` > `Messenger API Settings` > `Advanced` and accept Terms to use Marketing Message API for Messenger.
* Read our [Get Started Guide](https://developers.facebook.com/docs/marketing-messages-on-messenger/get-started) for more on setting up Marketing Message API for Messenger.
* Complete App Review for the following permissions before serving clients:
  + `ads_management`
  + `pages_messaging`
  + `paid_marketing_messages` or `marketing_messages_messenger`

## Flow 1: Business Portfolio Flow (SUAT)

This flow requires users to have Business Portfolio permission to onboard. It uses the `paid_marketing_messages` permission and generates a non-expiring system-business access token.

### Create a configuration

In the following steps, you are creating a login configuration that requires the business to select the following assets for sending marketing messages:

* Facebook Pages
* Meta business portfolio
* Meta ad account

**Note:** If the business does not have one of the required assets (Facebook Page, a Meta business portfolio, or a Meta ad account), the business can create any, or all, of these assets during the login flow.

|  |  |
| --- | --- |
| 1. In the Meta App Dashboard, click **Configurations** under Facebook Login for Business in the menu to the left. 2. Click **Create Configuration**. 3. **Add a name** for this configuration and click **Next**. 4. In the **Choose login variation** section, select **General** and click **Next**. 5. In the **Choose access token** section, select **System-business access token**. 6. In the **Choose token expiration** section, select **Never** and click **Next**. 7. In the **Choose assets** section, select **Pages** and then **Asset Required**, and **Ad accounts** and then **Asset Required**. 8. Click **Next**. 9. In the **Choose permissions** section, add the following permissions:    * `ads_management`    * `pages_messaging`    * `paid_marketing_messages` 10. Click **Create**. | [Launch the Graph API Explorer](/tools/explorer) |

Your Marketing Message API for Messenger login configuration for Flow 1 is complete.

## Flow 2: Asset-Based Flow (UAT)

This flow does not require Business Portfolio permission. Users can onboard their Ad Accounts and Pages as long as they have full control permission for those assets. It uses the `marketing_messages_messenger` permission.

### Create a configuration

In the following steps, you are creating a login configuration that allows your business to select the necessary assets for sending marketing messages:

* Facebook Pages
* Meta ad account

**Notes:**

* If your business does not have either a Facebook Page or a Meta Ad Account, you must create them **before** starting the onboarding process.
* The logged in user needs to have full control / manage permission for the Facebook Page and the Ad Account.
* The generated tokens in this flow will be short-lived tokens and will expire in about 1 hour. You can use instructions [here](https://developers.facebook.com/docs/facebook-login/guides/access-tokens/get-long-lived#long-lived-access-tokens) to get a long-lived token which expires in 60 days.

|  |  |
| --- | --- |
| 1. In the Meta App Dashboard, click **Configurations** under Facebook Login for Business in the menu to the left. 2. Click **Create Configuration**. 3. **Add a name** for this configuration and click **Next**. 4. In the **Choose login variation** section, select **General** and click **Next**. 5. In the **Choose access token** section, select **User access token** and click **Next**. 6. In the **Choose permissions** section, add the following permissions:    * `ads_management`    * `pages_messaging`    * `marketing_messages_messenger`      **Important:** Do NOT add `paid_marketing_messages` permission for this flow. 7. Click **Create**. | [Launch the Graph API Explorer](/tools/explorer) |

Your Marketing Message API for Messenger login configuration for Flow 2 is complete.

## Test your login flow

We recommend testing the login flow in Meta's Graph API Explorer.

|  |  |
| --- | --- |
| 1. On the right side of the explorer, select your marketing messages app from the **Meta App** dropdown menu. 2. Click **Configurations** then select your marketing messages configuration from the dropdown menu. The access token type, permissions, and assets required by this configuration are listed. 3. Click **Generate Access Token** to trigger the login flow. 4. After you complete the login flow in the pop-up window, a new access token is shown in the Graph API Explorer. | [Launch the Graph API Explorer](/tools/explorer) |

**For Flow 1:** Upon successful login, your app creates a non-expiring system business access token for the business.
**For Flow 2:** Upon successful login, your app creates a short-lived user access token (expires in ~1 hour). To get a long-lived token (expires in 60 days), follow the instructions [here](https://developers.facebook.com/docs/facebook-login/guides/access-tokens/get-long-lived#long-lived-access-tokens).

### View token details

Click the triangle icon to view the following access token information:

* App name and Meta ID
* Business ID (Flow 1 only)
* Validation status
* Scopes
* Graph domain

Click **Open in Access Token Tool** to view more information about this access token.

## Invoke the login dialog in your app

We recommend implementing the Javascript SDK from Meta in your web app to invoke the login dialog flow.

#### Embed your login button or URL in your web app

Set the `config_id` attribute to your configuration's ID in the `fb:login-button` element to invoke your configuration during login

```
<fb:login-button config_id="<CONFIG_ID>" onlogin="checkLoginState();">
</fb:login-button>
```

Use the JavaScript SDK from Meta's `FB.login()` method in your web app to use a specific configuration to get a system user access token.

* Set `config_id` to your configuration's ID
* Set `response_type` to `code` – authorization code grant type required for system user access tokens
* Set `override_default_response_type` to `true` – any response types passed in take precedence over the default types

#### Example code

```
FB.login(
  function(response) [
    console.log(response);
  ],
  [
    config_id: '<CONFIG_ID>',
    response_type: 'code',
    override_default_response_type: true
  ]
);
```

When your app user completes the login dialog flow, Meta redirects the user to your redirect URL and includes the authorization code. You must then exchange this code for an access token by performing a server-to-server call to Meta servers.

```
curl https://graph.facebook.com/<API_VERSION/oauth/access_token?
  client_id=<APP_ID>
  &client_secret=<APP_SECRET>
  &code=<AUTHORIZATION_CODE>
```

See [Exchanging Code for an Access Token](/docs/facebook-login/guides/advanced/manual-flow#exchangecode) for more information about this step.

## Best practices

Implement the following recommendations to help businesses discover and onboard to your app.

* Use "Marketing Messages" in the name for the marketing messages product in your app and explain its benefits.

**Marketing Messages on Messenger**

*Increase customer retention, and boost engagement and sales by sending personalized updates and promotions on Messenger.*

* Re-engage with customers anytime, beyond a 24-hour limit.
* Automatically get people to subscribe to marketing messages. Subscriptions do not expire.
* Send messages to everyone subscribed, or segment customers based on the subscription source or custom tag.
* Pay per message delivered and measure down-funnel conversions.

* Place the entry point to Marketing Messages in your app's primary navigation, or near the relevant messaging flows, with an informational banner or a contextual guidance card.
* Link your Marketing Messages onboarding flow to your app's **Get started** action button.
* When integrating both flows, provide clear guidance to help users choose the appropriate flow based on their permission level and business needs.

## Next steps

Now that you have onboarded businesses to your app, [get a list of subscribers](https://developers.facebook.com/docs/marketing-messages-on-messenger/increase-subscribers) to send paid marketing messages.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)