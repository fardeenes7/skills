# Buttons - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/send-messages/buttons

# Buttons

Most [message templates](/docs/messenger-platform/send-messages/templates/), as well as the [persistent menu](/docs/messenger-platform/reference/messenger-profile-api/persistent-menu), support buttons that invoke different types of actions. These buttons allow you to easily offer the message recipient actions they can take in response to the template, such as opening the Messenger webview, starting a payment flow, sending a postback message to your webhook, and more.

For message templates, buttons are defined by objects in the `buttons` array. For the persistent menu, buttons are defined by objects in the `call_to_actions` array.

## URL Button

![](https://scontent.fdac31-2.fna.fbcdn.net/v/t39.2365-6/17531046_119179685297959_5232300000901332992_n.png?_nc_cat=108&ccb=1-7&_nc_sid=e280be&_nc_ohc=mgLkEpX44kMQ7kNvwExsEcD&_nc_oc=Adoqvfx6S-7js7lD2FoYvCvk6SvFMNtWauS77PFA0Rd_42uB4FhXLELuKYS12B_Wy-Y&_nc_zt=14&_nc_ht=scontent.fdac31-2.fna&_nc_gid=krWk2Po7iK7Iw0U7zGs0rg&_nc_ss=7a30f&oh=00_Af36a87-wadkQZJhT84pvVpcxeatFS_pWibroLv7K6Q6QQ&oe=6A003AEA)

The URL Button opens a web page in the [Messenger webview](/docs/messenger-platform/webview). This allows you to enrich the conversation with a web-based experience, where you have the full development flexibility of the web. For example, you might display a product summary in-conversation, then use the URL button to open the full product page on your website.

### App Links

If the site contains [App Links](https://developers.facebook.com/docs/applinks/metadata-reference/), the button will launch the specified native app.

[The Facebook Crawler](https://developers.facebook.com/docs/sharing/webmasters/crawler/) needs to read the app link metatags for the redirect to work. Note that if you just implemented the tags in your website, you can request a new scrape with the [Sharing Debugger Tool](https://developers.facebook.com/tools/debug/sharing/). After the crawler has scraped the site, new URL buttons sent should follow the redirect behavior.

### Supported Usage

The URL button is supported for use with the following:

* Persistent menu
* Generic template
* List template
* Button template
* Media template

### Messenger Extensions SDK - Required Domain Whitelisting

To display a webpage with the [Messenger Extensions SDK](/docs/messenger-platform/webview/extensions) enabled in the Messenger webview you **must** allowlist the domain, including sub-domain, in the [`whitelisted_domains` property of your bot's Messenger Profile](/docs/messenger-platform/reference/messenger-profile-api/domain-whitelisting). This ensures that only trusted domains have access to user information available via SDK functions.

For more information on allowlisting domains, see the [`whitelisted_domains` reference](/docs/messenger-platform/reference/messenger-profile-api/domain-whitelisting).

### Button Format

For a complete list of button properties, see the [URL button reference](/docs/messenger-platform/reference/buttons/url).

```
{
  "type": "web_url",
  "url": "<URL_TO_OPEN_IN_WEBVIEW>",
  "title": "<BUTTON_TEXT>",
}
```

## Postback Button

The postback button sends a [`messaging_postbacks`](/docs/messenger-platform/reference/webhook-events/messaging_postbacks) event to your webhook with the string set in the `payload` property. This allows you to take an arbitrary actions when the button is tapped. For example, you might display a list of products, then send the product ID in the postback to your webhook, where it can be used to query your database and return the product details as a structured message.

### Supported Usage

The postback button is supported for use with the following:

* Persistent menu
* Generic template
* List template
* Button template
* Media template

### Button Format

For a complete list of button properties, see the [postback button reference](/docs/messenger-platform/reference/buttons/postback).

```
{
  "type": "postback",
  "title": "<BUTTON_TEXT>",
  "payload": "<STRING_SENT_TO_WEBHOOK>"
}
```

## Call Button

![](https://scontent.fdac31-1.fna.fbcdn.net/v/t39.2365-6/23204380_457498987984596_8630782823361413120_n.png?_nc_cat=105&ccb=1-7&_nc_sid=e280be&_nc_ohc=70b8OsGZZkUQ7kNvwEnxaEj&_nc_oc=AdpNEhr5IhJR1kCBzCkLyD3bD8iSI3ntnM38mg9ozrk4LM2KuXyEsx4gPZtvgds-85E&_nc_zt=14&_nc_ht=scontent.fdac31-1.fna&_nc_gid=krWk2Po7iK7Iw0U7zGs0rg&_nc_ss=7a30f&oh=00_Af2QPW2T3OBnUuj6myqRrp7Pa5y1OQMaD7erpz-SuDYyiw&oe=6A004CF3)![](https://scontent.fdac31-1.fna.fbcdn.net/v/t39.2365-6/23083335_129855331000571_3474293560784715776_n.png?_nc_cat=111&ccb=1-7&_nc_sid=e280be&_nc_aid=0&_nc_ohc=ErHh0Rxp2VMQ7kNvwFlXqUN&_nc_oc=AdoRfMsY-CbdJRnTDEzDrVt7pxjVv5T1T03ntiXqkWTvlXqiudYhkBvdoGKrKEMa6A8&_nc_zt=14&_nc_ht=scontent.fdac31-1.fna&_nc_gid=krWk2Po7iK7Iw0U7zGs0rg&_nc_ss=7a30f&oh=00_Af2Muw179BWkdbhZzbrDX_iM2LJVa1M3F98Y5Bz4bSaZlg&oe=6A005921)

The call button dials a phone number when tapped. Phone number should be in the format `+<COUNTRY_CODE><PHONE_NUMBER>`, e.g. `+15105559999`.

### Supported Usage

The call button is supported for use with the following:

* Generic template
* List template
* Button template
* Media template

### Button Format

For a complete list of button properties, see the [call button reference](/docs/messenger-platform/reference/buttons/call).

```
{
  "type":"phone_number",
  "title":"<BUTTON_TEXT>",
  "payload":"<PHONE_NUMBER>"
}
```

## Log In Button

The log in button is used in the [account linking flow](/docs/messenger-platform/account-linking), which lets you link the message recipient's identity on Messenger with their account on your site by directing them to your web-based login flow for authentication.

For more on using the log in button for account linking, see [Account Linking](/docs/messenger-platform/account-linking).

### Supported Usage

The log in button is supported for use with the following:

* Generic template
* List template
* Button template
* Media template

### Button Format

For a complete list of button properties, see the [log in button reference](/docs/messenger-platform/reference/buttons/login).

```
{
  "type": "account_link",
  "url": "<YOUR_LOGIN_URL>"
}
```

## Log Out Button

The log out button is used in the [account linking flow](/docs/messenger-platform/account-linking) to unlink the message recipient's identity on Messenger with their account on your site.

For more on using the log out button for account unlinking, see [Account Linking](/docs/messenger-platform/account-linking).

### Supported Usage

The log out button is supported for use with the following:

* Generic template
* List template
* Button template
* Media template

### Button Format

For a complete list of button properties, see the [log out button reference](/docs/messenger-platform/reference/buttons/logout).

```
{
  "type": "account_unlink"
}
```

## Game Play Button

![](https://scontent.fdac31-1.fna.fbcdn.net/v/t39.2365-6/16327315_1837847789814647_3597160501970206720_n.png?_nc_cat=106&ccb=1-7&_nc_sid=e280be&_nc_ohc=KhGHuO2gRYAQ7kNvwHeV0tA&_nc_oc=Adq4j30ngahsb9S9iCMgWbj9h6Y3R3W_VWthVjRUX884xsKBHLfFyfN_k3AjEDMMgjo&_nc_zt=14&_nc_ht=scontent.fdac31-1.fna&_nc_gid=krWk2Po7iK7Iw0U7zGs0rg&_nc_ss=7a30f&oh=00_Af3-nfrszW-vDlVu_8dnGFzSwOAa5ggzB15NTKPH32HOLA&oe=6A0032A5)![](https://scontent.fdac31-1.fna.fbcdn.net/v/t39.2365-6/17531113_183051362203851_4281206186423877632_n.png?_nc_cat=105&ccb=1-7&_nc_sid=e280be&_nc_ohc=Wer8Kx1a-HcQ7kNvwGLnN-K&_nc_oc=AdruQ5R0eQ-wbDiL3t5Mihlxl0OvMUN_QV-BjOE0PsE_SLopcP1IBuebstY69vGcXE8&_nc_zt=14&_nc_ht=scontent.fdac31-1.fna&_nc_gid=krWk2Po7iK7Iw0U7zGs0rg&_nc_ss=7a30f&oh=00_Af382Hd6rMbc85nc8CoR55ujWXsFKU7Y8s7NhrMSgxCrnA&oe=6A005453)

The game play button launches an Instant Game that is associated with your Facebook Page. To customize how your game is opened, you can set a `payload` property in the request that will be sent to the game on launch, as well as an optional `game_metadata.player_id` or `game_metadata.context_id` property, which allows your bot to start the game in a specific context against a single player or an existing group.

### Button Format

The `payload` property should be serialized JSON. It is deserialized by the Instant Games SDK.

For a complete list of button properties, see the [Game Play Button Reference](/docs/messenger-platform/reference/buttons/game-play).

```
{
  "type":"game_play",
  "title":"Play",
  "payload":"{<SERIALIZED_JSON_PAYLOAD>}",
  "game_metadata": { // Only one of the below
    "player_id": "<PLAYER_ID>",
    "context_id": "<CONTEXT_ID>"
  }
}
```

Refer to [Game Play webhook event](/docs/messenger-platform/reference/webhook-events/messaging_game_plays/) for the event that will be sent to the bot when a user finishes a game round.

## Best Practices

Use buttons to prompt for follow-up or further interaction with a particular message.

Start with a verb to help people understand the action they're taking.

Use URL buttons for tasks that you want completed on your website (ex: purchases, account linking, etc.). Make it clear you’re sending people outside of Messenger.

Send a response after someone taps a callback button. This confirms that you've processed or completed their action (ex: canceling a reservation, answering a question).

Don't use buttons when their action depends on the current state of the bot, since they'll be permanently available in the thread.

Don't use more than 1-3 words or add punctuation. Try to keep your text under 20
characters, including spaces.

Don't rely on URLs for every button. The more interactions you can build within Messenger, the more seamless your experience will be.

Don't use a single callback button. Where's only one button to choose from, people often think it's a continuation of your message text and don't understand it's an action you want them to take.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)