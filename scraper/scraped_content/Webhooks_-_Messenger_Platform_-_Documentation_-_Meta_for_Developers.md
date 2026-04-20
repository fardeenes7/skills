# Webhooks - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/webhooks

# Meta Webhooks for Messenger Platform

Meta Webhooks allows you to receive real-time HTTP notifications of changes to specific objects in the Meta social graph. For example, a notification can be sent when a person sends your Facebook Page or Instagram Professional account a message. Webhooks notifications allow you to **track incoming messages and message status updates**. Webhooks notifications also allow you to **avoid rate limits** that would occur if you were querying the Messenger Platform endpoints to track these changes.

To successfully implement Webhooks for Messenger or Instagram conversations, you will need to:

1. Create an endpoint on your server to receive and process your Webhooks notifications, JSON objects
2. Configure the Meta Webhooks product in your App Dashboard
3. Subscribe to the Meta Webhooks notifications you want to receive
4. Install your messaging app on the Facebook Page linked to your business or your Instagram Professional account

## Prerequisites

Before you start:

* Read and implemented the components needed for developing with Meta in the [Messenger Platform Overview](/docs/messenger-platform/overview)
* Publish your Meta app
* [Access requirements](/docs/graph-api/overview/access-levels)
  + **Standard Access** to receive notifications from people who have a role on your app, such as your app admins, developers or testers; or
  + **Advanced Access** to receive notifications from your customers, people who do not have a role on your app. Requires App Review.

## Configure Your Node.JS Server

Your server must be able to process two types of HTTPS requests: [Verification Requests](#verification-requests) and [Event Notifications](#event-notifications). Since both requests use HTTPs, your server must have a valid TLS or SSL certificate correctly configured and installed. Self-signed certificates are not supported.

The sections below explain what will be in each type of request and how to respond to them.

The code samples shown here are taken from our [sample app located on GitHub](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffbsamples%2Foriginal-coast-clothing%2Fblob%2Fmain%2Fapp.js&h=AT4_umR1hT3pb1PYSsKwhy534HsB8xze2unwlg5K46ST3oPHdxPkLBokgFWCKkFu1aJYUPNnIqyvr_b7phseajzsivk1JYy3CPmeQqbHeNdfo0K4ieH36iIghMPzj0Qf0Uz-Ls0WbVtdOBM4). Visit GitHub to see the complete example and more information about setting up your webhooks server.

### Create an Endpoint

To create an endpoint to receive webhooks notifications from the Messenger Platform, the `app.js` file may look like the following:

```
// Create the endpoint for your webhook

app.post("/webhook", (req, res) => {
  let body = req.body;

  console.log(`\u{1F7EA} Received webhook:`);
  console.dir(body, { depth: null });
    
...
```

This code creates a `/webhook` endpoint that accepts `POST` requests and checks that the request is a webhook notification.

### Return a `200 OK` response

The endpoint must return a `200 OK` response, which tells the Messenger Platform the event has been received and does not need to be resent. Normally, you will not send this response until you have completed processing the notification.

#### Respond to Event Notifications

Your endpoint should respond to all notifications:

* with a `200 OK HTTPS` response
* within 5 or less seconds

The following code will be in the `app.post` in your `app.js` file and may look like the following:

```
...
  // Send a 200 OK response if this is a page webhook

  if (body.object === "page") {
    // Returns a '200 OK' response to all requests
    res.status(200).send("EVENT_RECEIVED");
...
    // Determine which webhooks were triggered and get sender PSIDs and locale, message content and more.
...
  } else {
    // Return a '404 Not Found' if event is not from a page subscription
    res.sendStatus(404);
  }
});
```

### Verification Requests

Anytime you configure the Webhooks product in your App Dashboard, we'll send a `GET` request to your endpoint URL. Verification requests include the following query string parameters, appended to the end of your endpoint URL. They will look something like this:

#### Sample Verification Request

```
GET https://www.your-clever-domain-name.com/webhooks?
  hub.mode=subscribe&
  hub.verify_token=mytoken&
  hub.challenge=1158201444
```

#### Validating Verification Requests

Whenever your endpoint receives a verification request, it must:

* Verify that the `hub.verify_token` value matches the string you set in the **Verify Token** field when you [configure the Webhooks product](#subscribe-to-meta-webhooks) in your App Dashboard (you haven't set up this token string yet).
* Respond with the `hub.challenge` value.

Your `app.js` file may look like the following:

```
// Add support for GET requests to your webhook
app.get("/webhook", (req, res) => {
  
// Parse the query params
  let mode = req.query["hub.mode"];
  let token = req.query["hub.verify_token"];
  let challenge = req.query["hub.challenge"];

  // Check if a token and mode is in the query string of the request
  if (mode && token) {
    // Check the mode and token sent is correct
    if (mode === "subscribe" && token === config.verifyToken) {
      // Respond with the challenge token from the request
      console.log("WEBHOOK_VERIFIED");
      res.status(200).send(challenge);
    } else {
      // Respond with '403 Forbidden' if verify tokens do not match
      res.sendStatus(403);
    }
  }
});
```

Parameter | Sample Value | Description || `hub.mode` | `subscribe` | This value will always be set to `subscribe`. |
| `hub.challenge` | `1158201444` | An `int` you must pass back to us. |
| `hub.verify_token` | `mytoken` | A string that we grab from the **Verify Token** field in your app's App Dashboard. You will set this string when you complete the Webhooks configuration settings steps. |

**Note:** [PHP converts periods (.) to underscores (\_) in parameter names](http://l.facebook.com/l.php?u=http%3A%2F%2Fwww.php.net%2Fmanual%2Fen%2Flanguage.variables.external.php&h=AT5fsdiknNChR-S8MUN8vtwPsi7VwyR-u4daE_SuQJzQCipN551cTjFmcNQ9XVudlfWdc6l4HlR7xOIPTkoRrUJ-rOZQdUe1zOwR3Xog473L8B-JGbcP_bLywMrWX-li8oq3XfQ7Pvg4DFda8yKvEAARmozD7Q).

If you are in your App Dashboard and configuring your Webhooks product (and thus, triggering a Verification Request), the dashboard will indicate if your endpoint validated the request correctly. If you are using the Graph API's `/app/subscriptions` endpoint to configure the Webhooks product, the API will respond with success or failure.

### Event Notifications

When you configure your Webhooks product, you will subscribe to specific `fields` on an `object` type (for example, the `messages` field on the `page` object). Whenever there's a change to one of these fields, we will send your endpoint a `POST` request with a JSON payload describing the change.

For example, if you subscribed to the `page` object's `message_reactions` field and a customer reacted to a message your app sent, we would send you a `POST` request that would look something like this:

```
{
  "object":"page",
  "entry":[
    {
      "id":"<PAGE_ID>",
      "time":1458692752478,
      "messaging":[
        {
          "sender":{
          "id":"<PSID>"
          },
          "recipient":{
            "id":"<PAGE_ID>"
          },
          ...
        }
      ]
    }
  ]
}
```

#### Payload Contents

Payloads will contain an object describing the change. When you [configure the webhooks product](#subscribe-to-meta-webhooks), you can indicate if payloads should only contain the names of changed fields, or if payloads should include the new values as well.

We format all payloads with JSON, so you can parse the payload using common JSON parsing methods or packages.

**Note:** You will not be able to query historical webhook event notification data, so be sure to capture and store any webhook payload content that you want to keep.

### Validate Payloads

We sign all Event Notification payloads with a **SHA256** signature and include the signature in the request's 'X-Hub-Signature-256' header, preceded with 'sha256='. You don't have to validate the payload, but you should and we strongly recommend that you do.

To validate the payload:

1. Generate a **SHA256** signature using the payload and your app's **App Secret**.
2. Compare your signature to the signature in the `X-Hub-Signature-256` header (everything after `sha256=`). If the signatures match, the payload is genuine.

Please note that we generate the signature using an *escaped unicode* version of the payload, with lowercase hex digits. If you just calculate against the decoded bytes, you will end up with a different signature. For example, the string `äöå` should be escaped to `\u00e4\u00f6\u00e5`.

The `app.js` file may look like the following:

```
// Import dependencies and set up http server
const express = require("express"),
  bodyParser = require("body-parser"),
  { urlencoded, json } = require("body-parser"),
  app = express().use(bodyParser.json());
    
    ...


// Verify that the callback came from Facebook.
function verifyRequestSignature(req, res, buf) {
  var signature = req.headers["x-hub-signature-256"];

  if (!signature) {
    console.warn(`Couldn't find "x-hub-signature-256" in headers.`);
  } else {
    var elements = signature.split("=");
    var signatureHash = elements[1];
    var expectedHash = crypto
      .createHmac("sha256", config.appSecret)
      .update(buf)
      .digest("hex");
    if (signatureHash != expectedHash) {
      throw new Error("Couldn't validate the request signature.");
    }
  }
}
```

#### Webhooks Delivery Retry

If a notification sent to your server fails, we will immediately try a few more times. Your server should handle deduplication in these cases. If, after 15 minutes, we are still unable to deliver notifications, an alert is sent to your developer account.

If delivery of a notification continues to fail for 1 hour, you will receive a **Webhooks Disabled** alert, and your app will be unsubscribed from the webhooks for the Page or Instagram Professional account. Once you have fixed the issues you will need to subscribe to the Webhooks again.

If multiple messages are sent by the user when the application fails, they may not be delivered in the order they were sent. To ensure chronological order of message delivery, applications should always use the webhook **timestamp** field included in the webhook.

### Test Your Webhooks

To test your webhook verification run the following cURL request with your verify token:

```
curl -X GET "localhost:1337/webhook?hub.verify_token=YOUR-VERIFY-TOKEN&hub.challenge=CHALLENGE_ACCEPTED&hub.mode=subscribe"
```

If your webhook verification is working as expected, you should see the following:

* `WEBHOOK_VERIFIED` logged to the command line where your node process is running.
* `CHALLENGE_ACCEPTED` logged to the command line where you sent the cURL request.

To test your webhook send the following cURL request:

```
curl -H "Content-Type: application/json" -X POST "localhost:1337/webhook" -d '{"object": "page", "entry": [{"messaging": [{"message": "TEST_MESSAGE"}]}]}'
```

If your webhook is working as expected, you should see the following:

* `TEST_MESSAGE` logged to the command line where your node process is running.
* `EVENT RECEIVED` logged to the command line where you sent the cURL request.

## Subscribe to Meta Webhooks

Once your webhooks server endpoint, or sample app is ready, go to your app's [Meta App Dashboard](/apps) to subscribe to Meta Webhooks.

In this example we will use the dashboard to configure a Webhook and subscribe to the `messages` field. Any time a customer sends your app a message, a notification will be sent to your webhooks endpoint.

1. In the App Dashboard, go to **Products > Messenger > Settings**.
   * Some Messenger Platform webhooks are not available for Instagram messaging. If you are only implementing webhooks for Instagram and know the webhooks available for Instagram messaging, you can subscribe to webhooks here. To only view and subscribe to webhooks for Instagram messaging, you can go to **Instagram settings**.
2. Enter your endpoint's URL in the **Callback URL** field and add your verification token to the **Verify Token** field. We will include this string in all [Verification Requests](#verification-requests). If you are using one of our sample apps, this should be the same string you used for your app's `TOKEN` config variable.
3. Subscribe to fields for which you would like to be send notifications and click **Save**.
4. The last step is to subscribe to individual fields. Subscribe to the `messages` field and send a test Event Notification.
   * If your endpoint is set up correctly, it should [validate the payload](#validate-payloads) and execute whatever code you have set it up to do upon successful validation. If you are using our [sample app](/docs/graph-api/webhooks/sample-apps), load the app's URL in your web browser. It should display the payload's contents.

You can change your Webhooks subscriptions, verify token, or API version at any time using the App Dashboard.

**Note:** It is recommended that you use the latest API version to receive all information available for each webhook.

You can also do this programmatically by using the [`/app/subscriptions` endpoint](/docs/graph-api/reference/application/subscriptions).

#### Available Messenger Platform Fields

Messaging Webhooks Field | Description || `message_deliveries` | A notification is sent when a message that was sent by your business has been [delivered to a customer](/docs/messenger-platform/webhook-reference/message-delivered). Only available for Messenger conversations. |
| `message_echoes` | A notification is sent when [your business has sent a message](/docs/messenger-platform/webhook-reference/message-echo). This separate webhook field is available only for Messenger conversations. For Instagram Messaging conversations, the message echo notifications are included with the `message` webhook field subscription. |
| `message_edits` | A notification is sent when [a customer edits a previously-sent message](/docs/messenger-platform/reference/webhook-events/message-edit). Only availalbe for Messenger conversations. |
| `message_reactions` | A notification is sent when [a customer reacts to a message sent by your business.](/docs/messenger-platform/reference/webhook-events/message-reactions) |
| `message_reads` | A notification is sent when [a customer reads a message sent by your business, for Messenger conversations.](/docs/messenger-platform/webhook-reference/message-read) See `messaging_seen` for Instagram Messaging conversations. |
| `messages` | A notification is sent when your business has [received a message from a customer](/docs/messenger-platform/webhook-reference/message-received) from any conversation entry point. For Instagram Messaging, this subscription will also include notifications when your Instagram Professional account has sent a message since there is no separate `message_echoes` subscription field for Instagram Messaging. |
| `messaging_account_linking` | A notification is sent when a [customer links or unlinks their Messenger account from their account with your business.](/docs/messenger-platform/webhook-reference/account-linking) Only available for Messenger conversations. |
| `messaging_feedback` | A notification is sent when a person has [submitted feedback for your business.](https://developers.facebook.com/docs/messenger-platform/send-messages/templates/customer-feedback-template) Only available for Messenger conversations. |
| `messaging_game_plays` | A notification is sent when a person has played [a round of an Instant Game.](/docs/messenger-platform/reference/webhook-events/messaging_game_plays/) Only available for Messenger conversations. |
| `messaging_handovers` | A notification is sent when [a change has occurred during the Handover Protocol](/docs/messenger-platform/reference/webhook-events/messaging_handovers) |
| `messaging_optins` | A notification is sent when a customer has [clicked a Messenger plugin, accepted a message request using customer matching, or has opted in to receive messages via the checkbox plugin.](/docs/messenger-platform/reference/webhook-events/messaging_optins) Only available for Messenger conversations. |
| `messaging_policy_enforcement` | A notification is sent when [a policy enforcement warning has been sent or a policy enforcement action has been taken on the app associated with the Page.](/docs/messenger-platform/webhook-reference/policy-enforcement) |
| `messaging_postbacks` | A notification is sent when [a customer clicks a postback button, Get Started button, or persistent menu item for Messenger conversations or an Icebreaker option or Generic Template button for Instagram Messaging conversations.](/docs/messenger-platform/webhook-reference/postback-received) |
| `messaging_referrals` | A notification is sent when [a customer resumes a conversation with the Page by clicking an ig.me or m.me link, or an ad.](/docs/messenger-platform/webhook-reference/referral) |
| `messaging_seen` | A notification is sent when [a customer reads a message sent by your business, for Instagram Messaging conversations.](/docs/messenger-platform/webhook-reference/message-read) See `messaging_reads` for Messenger conversations. |
| `messenger_template_status_update` | A notification is sent when [a utility message template's review status has change](https://developers.facebook.com/docs/messenger-platform/send-messages/template/utility-messaging). |
| `response_feedback` | A notification is sent [when a customer provides feedback on a message sent by your business by clicking the feedback buttons](/docs/messenger-platform/reference/webhook-events/response_feedback). |
| `send_cart` | A notification is sent when your business has received a message from a customer, when the message contains cart/order information. Only available for Messenger conversations. |
| `standby` | A notification is sent when [a conversation is idle for an app during the Handover Protocol](/docs/messenger-platform/reference/webhook-events/standby) |

## Connect Your App

You will need to connect your Webhooks app to your Page and subscribe your Page to the Webhooks notifications you want to receive.

### Add the App

You can connect an app to a Page in the [Meta Business Suite > All Tools > Business Apps](https://business.facebook.com/).

**Note:** You will need to subscribe all messaging apps for your business to the messaging webhooks.

### Subscribe your Page

You will need to subscribe your Page to the Webhooks notifications you want to receive.

#### Requirements

* A Page access token requested from a person who can perform the [`MODERATE` task](/docs/pages/overview#tasks) on the Page being queried
* The [`pages_messaging` and `pages_manage_metadata` permissions](/docs/pages/overview/permissions-features#permission-dependencies)

To subscribe to a Webhooks field, send a `POST` request to the Page's [subscribed\_apps](/docs/graph-api/reference/page/subscribed_apps) edge using the Page's acccess token.

```
curl -i -X POST "https://graph.facebook.com/<PAGE_ID>/subscribed_apps
  ?subscribed_fields=messages
  &access_token=<PAGE_ACCESS_TOKEN>"
```

#### Sample Response

```
{
  "success": "true"
}
```

To see which app's your Page has installed, send a `GET` request instead:

#### Sample Request

```
curl -i -X GET "https://graph.facebook.com/<PAGE_ID>/subscribed_apps
  &access_token=<PAGE_ACCESS_TOKEN>"
```

#### Sample Response

```
{
  "data": [
    {
      "category": "Business",
      "link": "https://my-clever-domain-name.com/app",
      "name": "My Sample App",
      "id": "&lt;APP_ID>",
      "subscribed_fields": [
        "messages"
      ]
    }
  ]
}
```

If your Page has not installed any apps, the API will return an empty data set.

#### Graph API Explorer

You can also use the [Graph API Explorer](/tools/explorer) to send the request to subscribe your Page to a Webhooks field.

1. Select your app in the **Application** dropdown menu.
2. Click the **Get Token** dropdown and select **Get User Access Token**, then choose the `pages_manage_metadata` permission. This will exchange your app token for a User access token with the `pages_manage_metadata` permission granted.
3. Click **Get Token** again and select your Page. This will exchange your User access token for a Page access token.
4. Change the operation method by clicking the `GET` dropdown menu and selecting `POST`.
5. Replace the default `me?fields=id,name` query with the Page's **id** followed by `/subscribed_apps`, then submit the query.

## Next Steps

* [Send a test message](/docs/messenger-platform/get-started/)  – Learn how to use the platform to send a message.
* [Tour our sample app](/docs/messenger-platform/getting-started/sample-experience)  – Download code for our sample app to learn more about the features Messenger Platform has to offer.

## See Also

* Learn how to get notifications when a conversation is passed from one app to another using the [Conversation Routing API](/docs/messenger-platform/conversation-routing)
* Learn more about [Meta Webhooks for the Graph API](/docs/graph-api/webhooks)

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)