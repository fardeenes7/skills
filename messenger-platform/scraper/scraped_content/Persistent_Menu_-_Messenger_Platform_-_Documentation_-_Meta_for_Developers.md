# Persistent Menu - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/send-messages/persistent-menu

# The Persistent Menu

This documents shows you how to programmatically add the Persistent Menu to your messaging experience.

|  |  |
| --- | --- |
| How It Works The Persistent Menu allows you to create and send a menu of the main features of your business, such as hours of operation, store locations, and products, is always visible in a person's Messenger conversation with your business.  The Persistent Menu feature is not supported when Messenger is accessed via the Facebook Mobile Browser (the in-app browser within the Facebook app).  When a person clicks an item in the menu, a `postback` webhook notification is sent to your serve. The webhook notification contains information about what item was select and by whom. This item selection action opens the standard messaging window. You have 24 hours to respond to the person. |  |

If [Commands](/docs/messenger-platform/reference/messenger-profile-api/commands) are set, they will take priority over the Persistent Menu.

## Requirements

For the persistent menu to appear, the following must be true:

* The person must be running Messenger v106 or above on iOS or Android.
* The Facebook Page the Messenger bot is subscribe to must be published.
* The Messenger bot must be set to "public" in the app settings.
* The Messenger bot must have the `pages_messaging` permission.
* The Messenger bot must have a [get started button](/docs/messenger-platform/discovery/welcome-screen#set_postback) set.

## Supported Buttons

The persistent menu is composed of an array of [buttons](/docs/messenger-platform/send-messages/buttons). The following button types are supported in the persistent menu:

* `web_url`: Specifies the item is a [URL button](/docs/messenger-platform/send-api-reference/url-button).
* `postback`: Specifies the item is a [postback button](/docs/messenger-platform/send-api-reference/postback-button).

## Setting the Persistent Menu

To set the persistent menu, send a `POST` request to the [Messenger Profile API](/docs/messenger-platform/reference/messenger-profile-api) to set the `persistent_menu` property of your bot's Messenger profile.

We allow up to 20 buttons in the `call_to_actions` array.

```
{
    "persistent_menu": [
        {
            "locale": "default",
            "composer_input_disabled": false,
            "call_to_actions": [
                {
                    "type": "postback",
                    "title": "Talk to an agent",
                    "payload": "CARE_HELP"
                },
                {
                    "type": "postback",
                    "title": "Outfit suggestions",
                    "payload": "CURATION"
                },
                {
                    "type": "web_url",
                    "title": "Shop now",
                    "url": "https://www.originalcoastclothing.com/",
                    "webview_height_ratio": "full"
                }
            ]
        }
    ]
}
```

## Disabling the Composer

You may disable the composer to make the persistent menu the only way for a person to interact with your Messenger bot. This is useful if your bot has a very specific purpose or set of options.

To do this, set `"composer_input_disabled":true` when you create the persistent menu.

## Localization

You may provide default and localized button text for the persistent menu that will be displayed based on a person's locale.

To do this, specify a separate object in the `persistent_menu` array for each locale. To specify the locale for each object, set the `locale` property to a [supported locale](/docs/messenger-platform/messenger-profile/supported-locales):

```
{
  "locale":"default",
  "call_to_actions":[...]
},
{
  "locale: "zh_CN",
  "call_to_actions":[...]
}
```

## User level menu

You can override the Page level persistent menu with a user level setting. This allows your app to dynamically control:

* The click to action buttons on the menu for the user.
* The visibility of the composer for the user.

To enable or disable the user level setting a different endpoint called `custom_user_settings` is used. This endpoint supports POST, GET and DELETE calls.

The same configurations available for the Page level persistent menu apply at user level. The main difference is that a `psid` param is needed to indicate the user that this override applies to.

**NOTE:** The update of user level persistent menu happens in realtime, while the update of page level persistent menu can take up to 24 hours.

The user level settings are rate limited to 10 calls per user per 10 min.

### Example of POST Request

This will override the current page level settings for this user.

```
curl -X POST -H "Content-Type: application/json" -d '{
  "psid": "<PSID>",
  "persistent_menu": [
        {
            "locale": "default",
            "composer_input_disabled": false,
            "call_to_actions": [
                {
                    "type": "postback",
                    "title": "Talk to an agent",
                    "payload": "CARE_HELP"
                },
                {
                    "type": "postback",
                    "title": "Outfit suggestions",
                    "payload": "CURATION"
                },
                {
                    "type": "web_url",
                    "title": "Shop now",
                    "url": "https://www.originalcoastclothing.com/",
                    "webview_height_ratio": "full"
                }
            ]
        }
    ]
}' "https://graph.facebook.com/v25.0/me/custom_user_settings?access_token=<PAGE_ACCESS_TOKEN>"
```

### Example of GET Request

This will retrieve the current user and page level settings. If there are no user level settings only the page level ones will return.

```
curl -X GET "https://graph.facebook.com/v25.0/me/custom_user_settings?psid=<PSID>&access_token=<PAGE_ACCESS_TOKEN>"
```

Result

```
{
    "data": [
      {
        "user_level_persistent_menu": [
            {
              "locale": "default",
              "composer_input_disabled": false,
              "call_to_actions": [
                  {
                      "type": "postback",
                      "title": "Talk to an agent",
                      "payload": "CARE_HELP"
                  },
                  {
                      "type": "postback",
                      "title": "Outfit suggestions",
                      "payload": "CURATION"
                  },
                  {
                      "type": "web_url",
                      "title": "Shop now",
                      "url": "https://www.originalcoastclothing.com/",
                      "webview_height_ratio": "full"
                  }
              ]
            }
        ],
        "page_level_persistent_menu": [
          Original Page Menu...
        ]  
      }
  ]
}
```

### Example of DELETE Request

This will remove the user level settings, leaving the Page level menu if set.

```
curl -X DELETE 'https://graph.facebook.com/v25.0/me/custom_user_settings?psid=<PSID>&params=[%22persistent_menu%22]&access_token=<PAGE_ACCESS_TOKEN>'
```

## Best Practices

Like buttons, menu items can produce a webview or postback. Keep in mind that second-level menu is not supported.

Use the menu for entry points into your bot's functionality.

Be descriptive: your menu lets people know what your bot can do. It instantly lets users know what they can reach your bot for in the future.

Be selective to represent the core functions of your bot and try to limit menu items to 5 for best user experience.

Don't expect the menu to contain user-specific data: it's the same for everyone who uses your bot, though it can be localized.

Don't put a "Menu" button in the menu that sends the user a message containing a menu. Just put that content directly in the menu — that's what it's for!

Don't put generic actions like "Restart" in the menu.

Don't use prime menu real estate for secondary, "colophon" style info like about, terms of service, privacy policy, or "powered by", neglecting to expose your bot's main functionality.

### Developer Support

* Use the [Meta Status tool](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F&h=AT4FEF7y0H-isMHF80qI-Uh-HxRzAQVpwBFcdt209Xp8juKpHG56jF5Dhc648migKKLdpjSHO4wjH7qkxEMrDk_SpY09vYAyoOpdkqsh_uHkuSHLhDBvWGNkc-RhXxYsVvN3AZDZasTBPuDJ) to check for the status and outages of Meta business products.
* Use the [Meta Developer Support tool](/support) to report bugs and view reported bugs, get help with Ads or Business Manager, and more.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)