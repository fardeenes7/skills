# Send API - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/send-api

# Send API Reference

The Send API is the main API used to send messages to users, including text, attachments, templates, sender actions, and more.

## Creating

Create and send messages to your customers or people interested in your Facebook Page.

### Before You Start

You will need:

* A Page access token requested by a person who can perform the `MESSAGE` task on the Page
* The `pages_messaging` permission
* The message recipient must have sent your Page a message within the last 24 hours or agreed to receive messages from your Page outside of the standard 24 hour messaging window

### Limitations

* Message tags can not be used to send promotional content

Note that the Send API does not include `recipient_id` in the response for messages sent using `recipient.user_ref` or `recipient.phone_number` to identify the message recipient.

### Sample Request

To send a message to a person, send a `POST` request to the `/PAGE-ID/messages` endpoint with the `messaging_type` and `recipient` parameters set, and the message content.

*Formatted for readability.*

The following example is a response to a person's message where the message your Page is sending is text only.

```
curl -X POST "https://graph.facebook.com/v25.0/{PAGE_ID}/messages" \
      -d "recipient={'id':'{PSID}'}" \
      -d "messaging_type=RESPONSE" \
      -d "message={'text':'hello, world'}" \
      -d "access_token={PAGE_ACCESS_TOKEN}"
```

On success, your app will receive the following JSON response:

```
{
  "recipient_id": "PAGE-SCOPED-ID",
  "message_id": "AG5Hz2U..."
}
```

### Parameters

Parameter | Description || `message` *object* | The type of message your Page is sending. Either `text` or `attachment` must be set when using this parameter.   * `attachment` object – Previews the URL. Used to send messages with media or Structured Messages. `text` or `attachment` must be set.    + `type` – Type of attachment. Can be `audio`, `file`, `image`, `template`, or `video`. Maximum file size is 25MB   + `payload` – An object containing a [template content](/docs/messenger-platform/reference/templates#attachment) or [file content](/docs/messenger-platform/reference/attachment-upload-api#attachment) * `metadata` – A string of additional data you want to pass in the `message_echo` webhook. Must be less than 1000 characters * `quick_replies` – An array of quick replies to be sent in a message * `text` – A message containing text only. Must be UTF-8 and less than 2000 characters. |
| `messaging_type` *enum* Required | The type of message being sent   * `RESPONSE` – Message is in response to a received message. This includes promotional and non-promotional messages sent inside the [24-hour standard messaging window](/docs/messenger-platform/policy-overview#24hours_window). For example, use this tag to respond if a person asks for a reservation confirmation or an status update. * `UPDATE` – Message is being sent proactively and is not in response to a received message. This includes promotional and non-promotional messages sent inside the the [24-hour standard messaging window](/docs/messenger-platform/policy-overview#24hours_window). * `MESSAGE_TAG` – Message is non-promotional and is being sent outside the [24-hour standard messaging window](/docs/messenger-platform/policy-overview#24hours_window) with a [message tag](/docs/messenger-platform/send-messages/message-tags). The message must match the allowed use case for the tag. |
| `notification_type` *enum* | Type of push notification a person will receive   * `NO_PUSH` – No notification * `REGULAR` (default) – Sound or vibration when a message is received by a person * `SILENT_PUSH` – On-screen notification only |
| `recipient` *object* Required | The person who will receive the message your Page is sending   * `id` – The Page-scoped ID for the person that is used to send a message in response to a message received by your Page within the last 24 hours or for a person who has agreed to receive messages from your Page outside the standard 24 hour messaging window * `user_ref` – The reference for the person that is used to send a message in response to a Checkbox Plugin * `comment_id` – The ID for the comment that is used to send a message as a Private Reply in response to a visitor Comment on your Page Post * `post_id` – The ID for the Page Post that is used to send a message as a Private Reply in response to a visitor Post on your Page |
| `sender_action` *enum* | The action icon shown in the messaging window representing the action taken by the Page on a message the Page has received from a person.   * `typing_on` – Display the typing bubble when the Page is preparing a response * `typing_off` – Do not display the typing bubble * `mark_seen` – Display the seen icon for messages that have been seen by the Page   Can only be sent with the `recipient` parameter. Cannot be sent with the `message` parameter but must be sent as a separate request. |
| `tag` *enum* | A tag that enables your Page to send a message to a person outside the standard 24 hour messaging window.   * `ACCOUNT_UPDATE` – Tags the message you are sending to your customer as a non-recurring update to their application or account.   [View the allowed uses.](#message-tag-usages) *Not available for Instagram Messaging API.* * `CONFIRMED_EVENT_UPDATE` – Tags the message you are sending to your customer as a reminder fo an upcoming event or an update for an event in procgres for which the customer is registered.   [View the allowed uses.](#message-tag-usages) *Not available for Instagram Messaging API.* * `CUSTOMER_FEEDBACK` – Tags the message you are sending to your customer as a   [Customer Feedback Survey](/docs/messenger-platform/send-messages/templates/customer-feedback-template). Customer feedback surveys must be sent within 7 days of the customer's last message.   [View the allowed uses.](#message-tag-usages) *Not available for Instagram Messaging API.* * `HUMAN_AGENT` – **Required for Instagram Messaging API.** When this tag is added to a message being sent to a person, it allows a human agent to respond to the person's message. Messages can be sent within 7 days of the person's message. Human agent support is for issues that cannot be resolved within the standard messaging window.   [View the allowed uses.](#message-tag-usages)   + Apps will need to apply for the `Human Agent` permission via the Developer App dashboard. Navigate to App dashboard -> App review -> Permissions & Features -> Human Agent. Apps that were previously approved for beta access to the Human Agent permission do not need to re-apply for access. `Human Agent` is only available to apps that have completed the app review process. Your app must be approved before you can use the human agent tag. During app review submission, please provide clear instructions and a demonstration for how you intend to leverage the human agent tag in your experiences. * `POST_PURCHASE_UPDATE` – Tags the message you are sending to your customer as an update for a recent purchase made by the customer.   [View the allowed uses.](#message-tag-usages) *Not available for Instagram Messaging API.* |
| `reply_to` *object* | The message in the chat that your Page is replying to   * `mid` – The message id of the specific message in the chat that your Page is replying to. This can be the id of a message that either the user or the Page has sent. The page should have received a message from the user within the last 24 hours. |

### Message Tag Usages

#### Upcoming Changes

Effective April 27th, 2026, all API requests containing the Message Tags CONFIRMED\_EVENT\_UPDATE, ACCOUNT\_UPDATE, and POST\_PURCHASE\_UPDATE will receive error code 100.

The following table lists the types of messaging for each message tag.

Message Tag | Usage || `ACCOUNT_UPDATE` | Allowed Usages  * A notification for a change in status for an application, such as for a credit card or job application * A notification for suspicious activity, such as fraud alerts  Disallowed Usages (non-exhaustive)  * Promotional content, including but not limited to deals, promotions, coupons, and discounts   Recurring content (e.g., statement is ready, bill is due, new job listings) * Prompts to any survey, poll, or reviews unrelated to a preceding interaction in Messenger   *Not available for Instagram Messaging API.* |
| `CONFIRMED_EVENT_UPDATE` | Allowed Usages  * A reminder for an upcoming class, appointment, or event that a user has scheduled * A confirmation for a user's reservation or attendance to an accepted event or appointment * A notification for a user's transportation or scheduled trip, such as arrival, cancellation, baggage delay, or other travel status changes  Disallowed Usages (non-exhaustive)  * Promotional content, including but not limited to deals, offers, coupons, and discounts * Content related to an event the user has not signed up for (e.g., reminders to purchase event tickets, cross-sell of other events, tour schedules, etc) * Messages related to past events * Prompts to any survey, poll, or reviews unrelated to a preceding interaction in Messenger   *Not available for Instagram Messaging API.* |
| `CUSTOMER_FEEDBACK` | Allowed Usages  * A survey for purchase support feedback * A survey for event feedback * Product reviews  Disallowed Usages (non-exhaustive)  * The tag can only be used with the Customer Feedback Template. Use in any other form is prohibited and will fail.   *Not available for Instagram Messaging API.* |
| `HUMAN_AGENT` | Allowed Usages  * Human agent support for issues that cannot be resolved within the 24 hour standard messaging window, such as resolving issues outside normal business hours or issues requiring more than 24 hours to resolve  Disallowed Usages (non-exhaustive)  * Automated messages * Content unrelated to user inquiry   **Required for Instagram Messaging API.** |
| `POST_PURCHASE_UPDATE` | Allowed Usages  * A confirmation for a transaction, such as invoices or receipts * A status update for a shipment, such as product in-transit, shipped, delivered, or delayed * A status update requiring a user to take action for an order that the user placed, such a declined credit card, backorder items, or other order updates that require user action  Disallowed Usages (non-exhaustive)  * Promotional content, including but not limited to deals, promotions, coupons, and discounts * Messages that cross-sell or upsell products or services * Prompts to any survey, poll, or reviews unrelated to a preceding interaction in Messenger   *Not available for Instagram Messaging API.* |

## Reading

You can't perform this operation on this endpoint.

To get information about conversations your Page are a part of visit the [Page Conversations Reference](/docs/graph-api/reference/page/conversations/).

## Updating

You can't perform this operation on this endpoint.

## Deleting

You can't perform this operation on this endpoint.

## See Also

* [Error codes](/docs/messenger-platform/send-api-reference/errors)
* [Rate Limits](/docs/messenger-platform/overview/rate-limiting)
* [High Volume Messaging](/docs/messenger-platform/overview/rate-limiting)

### Developer Support

* Use the [Meta Status tool](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F&h=AT5hHbgPgtCnbl1Tt2b0iS_Gb2sOg45eSdnxjpUu1pM3JwpBd1RTBI22mDnO4-v38cqwxDZGcDzu4_kXM0Bw1p4bqULgk4t1zuU5Yw69lfYilybGlPCW5CZplbGgym8IWBSpuzmPv8qaQhPB) to check for the status and outages of Meta business products.
* Use the [Meta Developer Support tool](/support) to report bugs and view reported bugs, get help with Ads or Business Manager, and more.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)