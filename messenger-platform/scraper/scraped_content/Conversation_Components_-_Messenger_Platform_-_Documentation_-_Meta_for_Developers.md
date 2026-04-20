# Conversation Components - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/introduction/conversation-components

# Conversation Components

Conversations are a lot more than simple text messages when you are building a bot on the Messenger Platform. In addition to text, the Platform allows you to send rich-media, like audio, video, and images, and provides a set of structured messaging options in the form of message templates, quick replies, buttons and more. This is intended to be an overview of the components that are available for you to create your Messenger experience in-conversation.

In addition to these conversation components, the Messenger Platform supports a full webview that allows you to enrich your in-conversation Messenger experience by extending it to the web. For more information on using the webview, see [Webview](/docs/messenger-platform/webview).

### Available Conversation Components

* [Text Messages](#text_messages)
* [Assets & Attachments](#attachments)
* [Message Templates](#templates)
* [Quick Replies](#quick_replies)
* [Sender Actions](#sender_actions)
* [Welcome Screen](#welcome_screen)
* [Persistent Menu](#persistent_menu)

## Text Messages

![](https://scontent.fdac31-1.fna.fbcdn.net/v/t39.2365-6/13503471_1613963512265939_694041731_n.png?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=9QpJ4bE6z-AQ7kNvwHibMkn&_nc_oc=AdrMul2oKDoz7yylEI9YS4ML1eNcjIOXNqzqbV21gjz_KwfelrdnmBurq4v_kuSlVdE&_nc_zt=14&_nc_ht=scontent.fdac31-1.fna&_nc_gid=8pjHMAo7fDOdLLicabABjg&_nc_ss=7a30f&oh=00_Af0vNMEPkBV9lnzV6NVo0SdrRcvWw8Uu4GWoB6L1NvOGag&oe=6A002FF7)

Simple text is the foundation of any experience on Messenger, and is one of the most important tools at your disposal if you goal is to create a conversational experience. Try processing text messages with the Messenger Platform's [built-in natural language processing (NLP)](/docs/messenger-platform/built-in-nlp) feature to handle all kinds of interactions with simple text.

[Sending Text →](/docs/messenger-platform/send-messages#sending_text)

## Assets & Attachments

In addition to text, the Messenger Platform allows you to send rich media assets as standalone messages or attached to structured [message templates](#templates). Supported asset types included the following:

* Audio
* Video
* Images
* Files

Assets may be sent from a URL or your file system. For assets you intend to send multiple times, you may upload them in advance with the [Attachment Upload API](/docs/messenger-platform/reference/attachment-upload-api/) or upload them the first time they are sent with the [Send API](/docs/messenger-platform/send-messages/saving-assets#send_api) to eliminate the time and bandwidth overhead of uploading with each send. Saved assets are sent with an `attachment_id` that is assigned when they are uploaded.

[Saving Assets →](/docs/messenger-platform/send-messages/saving-assets)[Sending Attachments →](/docs/messenger-platform/send-messages#sending_attachments)

## Message Templates

![](https://scontent.fdac31-1.fna.fbcdn.net/v/t39.2365-6/14235537_178238889274354_2098325353_n.png?_nc_cat=110&ccb=1-7&_nc_sid=e280be&_nc_ohc=cQfyB-i3FEsQ7kNvwFe5ek5&_nc_oc=Adpcepxb-kDEp587lnPPeKiqzkYA5TuK-oi0gbBkcH_R2DRE-K-uIlbfnynB9hR5-bA&_nc_zt=14&_nc_ht=scontent.fdac31-1.fna&_nc_gid=8pjHMAo7fDOdLLicabABjg&_nc_ss=7a30f&oh=00_Af1oxUZc38XvtoneKt0Litfb1pXh2SaUMYIJhi1J3Unmtg&oe=6A004392)

Message templates are structured message types intended to support different use cases, and are useful for presenting information in-conversation that would be difficult to render or sloppy-looking with simple text. Templates also support [buttons](/docs/messenger-platform/send-messages/buttons) that extend their functionality.

The following message templates are available:

* [Generic template](/docs/messenger-platform/send-messages/templates#generic)
* [Button template](/docs/messenger-platform/send-messages/templates#button)
* [Receipt template](/docs/messenger-platform/send-messages/templates#receipt)
* [Airline templates](/docs/messenger-platform/send-messages/template/airline)
* [Media Template](/docs/messenger-platform/send-messages/templates#media)

Message templates also support a set of buttons that add functionality, such as opening the webview, sending a postback to your webhook, sharing content, and more.

[Sending Message Templates →](/docs/messenger-platform/send-messages/templates)[Using Buttons →](/docs/messenger-platform/send-messages/buttons)

## Quick Replies

![](https://lookaside.fbsbx.com/elementpath/media/?media_id=668002490333314&version=1776079002)

Quick Replies allow you present a preset set of options to the message recipient, which appear prominently above the composer. When a quick reply is tapped, the set is replaced with a single text message that is sent to your webhook. You may also add an image to a Quick Reply.

[Sending Quick Replies →](/docs/messenger-platform/send-messages/quick-replies)

## Sender Actions

![](https://scontent.fdac31-1.fna.fbcdn.net/v/t39.2365-6/13480169_570751053131489_689799179_n.png?_nc_cat=111&ccb=1-7&_nc_sid=e280be&_nc_ohc=5Mfg1IkThSUQ7kNvwF7c3VQ&_nc_oc=AdqAVgmVAaiHf4adBc8Jv1MpZaAmU68wdH14CFchceAEcT_lrmupBLBMEGq1jDIDlSo&_nc_zt=14&_nc_ht=scontent.fdac31-1.fna&_nc_gid=8pjHMAo7fDOdLLicabABjg&_nc_ss=7a30f&oh=00_Af1zA6NL9xCDwzvxzHCoxUBYKtSt4g-Sk2kcfiJLEpgCnQ&oe=6A004A24)

An important aspect of creating a Messenger bot is setting expectations. Sender actions are an important tool for accomplishing this that gives you the ability to programmatically control the standard Messenger typing, and read receipt indicators in-conversation. For example, when you begin processing a message, you might set the read receipt indicator so the person interacting with your bot knows their message has been seen, then you might set the typing indicator to show them that a response is in-progress.

[Using Sender Actions →](/docs/messenger-platform/send-messages/sender-actions)

## Welcome Screen

![](https://scontent.fdac31-1.fna.fbcdn.net/v/t39.8562-6/121107394_353229089217270_1561647597250596467_n.png?_nc_cat=106&ccb=1-7&_nc_sid=f537c7&_nc_ohc=NR1MR_WYsHQQ7kNvwHM-ejK&_nc_oc=Adp0Ao9vnaL1rehbug10Dhhs9EH5wHUvj2GidVU-Oi5eT3aOqO29MaXWfEzqzfSgLw4&_nc_zt=14&_nc_ht=scontent.fdac31-1.fna&_nc_gid=8pjHMAo7fDOdLLicabABjg&_nc_ss=7a30f&oh=00_Af0uUbaQjIzoArZVoVU3DBdTCbN1HOtzU9EBSwga8_bIfw&oe=69EBE4C5)

The welcome screen is the first thing people see when they start a new conversation with your Messenger bot, and includes the name, description, profile picture and cover photo from your Facebook Page. You may also set optional [greeting text](/docs/messenger-platform/reference/messenger-profile-api/greeting) for the welcome screen, which can be used to introduce the purpose of your bot.

A conversation with your bot begins when the [get started button](/docs/messenger-platform/reference/messenger-profile-api/get-started-button) is tapped.

[Configuring the Welcome Screen →](/docs/messenger-platform/discovery/welcome-screen)

## Persistent Menu

![](https://lookaside.fbsbx.com/elementpath/media/?media_id=2284308045168297&version=1775093763)

The persistent menu is an always-on user interface element that helps people discover and more easily access your bot's functionality throughout the conversation. This menu should contain top-level actions that a person can enact at any point. You may also optionally make the persistent menu the only way to interact with your bot by disabling the composer.

[Setting the Persistent Menu →](/docs/messenger-platform/send-messages/persistent-menu/)

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)