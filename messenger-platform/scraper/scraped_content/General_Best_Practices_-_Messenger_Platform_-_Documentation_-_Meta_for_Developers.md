# General Best Practices - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/introduction/general-best-practices

# General Best Practices

Designing a Messenger experience is different from designing apps for mobile or the web. Some universal UX principles apply, of course, but the tools and expectations are very different, even compared to other messaging platforms.

Interactions that might be challenging to design for a traditional app can be easy here, but the reverse can be true as well. To help you begin thinking about how to approach designing and building the experiences you want to create in Messenger, we have gathered some best practices and guidelines based on our experiences that we hope you will consider as you begin working with the Messenger Platform.

## Access Token Management

Page Access tokens with `pages_messaging` permission are required to interact with the Messenger platform. A valid Page Access token fundamentally grants permission to an app to impersonate a Page. Page access token usually backed by an user, this means that the user controls the access and can terminate that access at any time.

For stable productions apps a Page Access Token backed by an user poses the risk that certain user actions can invalidate the access token and therefore break the app. To prevent disruptions it is recommended to use a [stable access token backed by a system user](https://developers.facebook.com/docs/facebook-login/business-login-direct/). This effectively makes the Access Token backed by a business rather than an individual. To create one, both the app and the Page, need to be owned by the same business.

Another best practice is to handle the [Graph API error code](https://developers.facebook.com/docs/graph-api/using-graph-api/error-handling/): `190`. Indicating that the Access token is no longer valid. A notification should be implemented by the business to warn the appropriate Page/App Admins on the need to issue a new token to re-enable the app capability to impersonate the Page.

```
{
    "error": {
        "message": "Access token is no longer valid",
        "type": "OAuthException",
        "code": 190,
        "fbtrace_id": "ANtXl05DDie3Dau970_10Ah"
    }
}
```

## Secure your Send API Calls and Webhooks

Production apps are strongly recommended to secure both you API calls and incoming Webhook to prevent attacks and mitigate security breaches of your existing access tokens.

App Secret is a property of Apps than can be fetched on the App Dashboard **Settings** > **Basic** menu. In the same menu the App Admin can **Reset** the App Secret to a new one. App secrets are used as:

* Secure Webhooks with a signature HTTP Header called `X-Hub-Signature`
* Secure API with a signature param called `appsecret_proof`
* Identify App Access Tokens in the context of App API Calls

### Secure Webhooks

Incoming webhooks can be secured with the App Secret by validating the provided signature. Every incoming webhooks has an HTTP Header `X-Hub-Signature`. This signature of the incoming payload can be used to verify that the sender knows the app secret and the intended receipient is your APP. This can help ignore webhook injection attacks and prevent confusion when the same Callback URL is set for different apps. [Learn how to validate incoming webhooks](https://developers.facebook.com/docs/messenger-platform/webhook/#security)

### Secure API calls

You can add an extra layer of security to your API calls by enabling the **Require App Secret** setting in the app dashboard and including the `appsecret_proof` parameter in your API calls. [Learn how to set and implement App Secret Proof](/docs/graph-api/guides/secure-requests/#appsecret_proof)

## Design Strategy

Whether using automation or implementing live messaging, it’s important to define the experience you want to create for yourself and the people you’re interacting with on Messenger. Before any messages get sent, take the time to:

* **Determine your goals.** Do you want to design around utility, delight or a mixture of both? Understanding your strategy and what you want to accomplish will help you create the best experience.
* **Decide what you want people to do.** What actions do you want people to take? Are there multiple tasks you want them to complete? How are those tasks completed outside of Messenger? Determine all the paths people can navigate when designing your interactions.
* **Plan how you’ll evolve.** Once people complete your tasks, what are some ways you can keep the interaction going? Consider how you can expand your capabilities to grow your experience and extend your lifecycle.

Focus on doing a couple things really well; doing too much creates confusion and dilutes your experience.

## Conversation vs. GUI

All Messenger experiences are conversational to some degree. Every interaction you build with the Messenger Platform is perceived as an extension of the chat experience, which has become familiar to anyone with a mobile phone. This can make conversations in Messenger feel far more human and familiar than interactions with a mobile or web app, even if the replies from your bot are completely automated. After all, what could be more human than a conversation? Add the built-in natural language processing features of **[Wit.ai](https://l.facebook.com/l.php?u=https%3A%2F%2Fwit.ai%2F&h=AT47QOOefva-pOnVyXRrrYBkN6KN7oySxJ8L4uWO4GMcWnQ2LRdME_q7FG9RFdJIuNlcbH2FOFpYRBJE-ha5PSN1Ni5DGmRb_1RWB044GQlLIf2Oq3Aa_hVB90hJ2SjSHsx7bWZf5jPmIH-H)** to this, which allow you to automatically parse and interpret intents from received messages, and exchanges with your Messenger bot really begin feeling like true conversations.

But for the people interacting with your app, typing out every request and response can be far more tedious than clicking a button or selecting from a list, especially when there are only two or three reasonable options. Decades of advancement in graphical user interfaces (GUIs) have shown how powerful it can be to *directly manipulate* objects in a UI: tapping an image to open it, pinching a map to zoom in, etc.

Luckily, Messenger also gives you an entire spectrum of components ranging from pure text messages on the one hand, to full GUIs on the other. This gives you flexibility to mix and match to create just the right interactions that combine the simplicity and humanity of chat with the interactive power of a GUI in one experience.

![](https://scontent.fdac31-1.fna.fbcdn.net/v/t39.8562-6/121104704_372291410815000_4348014391920160819_n.png?_nc_cat=105&ccb=1-7&_nc_sid=f537c7&_nc_ohc=919HFUqFkbkQ7kNvwHi9BCY&_nc_oc=AdomJxeQGaq-NRsw2WH_o8X0z-4fdQDBjKftqCAWGFppSa-izy7yTGfcf4KfKDgw-Tk&_nc_zt=14&_nc_ht=scontent.fdac31-1.fna&_nc_gid=PcWE8DFikZmMIT6h2BL8ew&_nc_ss=7a30f&oh=00_Af2iF38Kl4-KlzBI1C6maB0Jwt-3rrKICjjZyRon1hYiHA&oe=69EBB7F0)

## Design Principles

The following are some design principles to think about when building your Messenger app. They are by no means exhaustive, but are a great starting point.

### Be Brief

Most people will use your bot on a phone, where distractions abound: the physical environment, other apps, even other threads in Messenger. Expect interruptions. Expect people to forget what they were doing. The easiest way to address this is to keep interactions short. When that is not possible, consider how to maintain and reestablish context.

### Avoid Modality

Your bot is in a *modal* state when it is expecting a specific set of responses. For example, you might present a person with a search result and be tempted to automatically treat the next message sent as a refinement. But what if the person is interrupted mid-task? What if they decide to interrupt *you* mid-task while the search is being performed? This is a recipe for confusion and frustration. One solution is to keep exchanges brief, and leave the bot in its usual state rather than an interim one.

### Mix Conversation and GUI

The Messenger Platform offers a range of conversation components, from pure text messages to structured templates to full GUI interactions in the webview. Each has its strengths and weaknesses depending on your use case. When building an experience in Messenger, carefully consider what format will create the most straightforward, intuitive experience. Often, the answer will be a combination of conversational and UI interactions.

### Observe Conversational Norms

Be deliberate about language, editorial voice, length of messages, and even how fast your bot responds. If your Messenger bot supports both automated and human interactions, be clear about what is happening to avoid creating a jarring or confusing experience. For example, do not disguise an automated interaction as a real person.

### Embrace Structure

While recognizing free-form typed responses can be valuable, it can also be challenging to implement and tedious for people interacting with your bot. Make use of [buttons](/docs/messenger-platform/send-messages/buttons), [quick replies](/docs/messenger-platform/send-messages/quick-replies), and the [persistent menu](/docs/messenger-platform/send-messages/persistent-menu) to structure user input. This can help streamline interactions and clearly communicate expectations.

### Be Predictable

Provide a confirmation when a request is processed. Use the [typing indicator](/docs/messenger-platform/send-api-reference/sender-actions) to let people know when your bot is in-progress. Provide clear opt-in functionality for subscriptions. Do not change what you deliver, or when, without consent.

### Notify with care

Not every message needs a push notification. Increase the impact of your notifications by being deliberate.

### Fail Gracefully

If you do not understand a request, reiterate your capabilities: highlight help functionality, or use buttons, quick replies, and the persistent menu to clarify. Treat each failure as feedback, and remember people will often respond to your bot in unexpected ways.

### Do Not Create a Separate Entity

In general, it is best to tie the identity of your Messenger bot to your existing Facebook Page, rather than creating a new one. This ensures people will have an easier time finding it and feeling confident it is you or your business.

## Language & Editorial Voice

Because your interactions take place on Messenger, a platform built around conversations, the words you use go far in explaining the experience your bot provides and why people should use it.

These writing best practices will help you continually build trust as people discover and get to know your experience on Messenger. The more people understand how to interact with you, the more likely you are to keep them engaged.

### Preserve Your Voice

While you are using platform tools to reach people on Messenger, you own your interactions. Your voice is your personality; continue to use it with a tone that feels natural and human.

* **Do** rely on familiarity. Continue to use terms and phrases that people already know and have come to associate with you.
* **Do not** create a new personality. This creates confusion and people will wonder if they are interacting with the right brand.

### Set Expectations

Based on the goals and tasks you outlined, write in a way that lets people know exactly what they can do and what you want them to do. Be as descriptive as possible to communicate the core features of your Messenger bot.

* **Do** let people know how often you will reach out or respond. Knowing your availability and level of responsiveness helps people understand your timing.
* **Do not** imply that you offer live messaging if you do not support it (or never will). Be direct about your capabilities so people respond accordingly.

### Provide Context

To build understanding of your bot's experience, use content to guide people every step of the way: tell them what stage they are at, what is being asked of them, and what will happen next.

* **Do** confirm actions people take. It will make people feel like your bot is “listening” and make your experience even more reliable.
* **Do not** keep people waiting. If someone asks for something, acknowledge their request and let them know if and when you can deliver.

## Writing Interactions

Before you interact with people in Messenger, pretend you have already had a conversation and start building a library of prompts and responses. Think about how you want the interaction to go, and all the possible ways it could actually go. Once you have done this, try to do the following:

### Create a List of Keywords

What terms are associated with your brand? What vernacular might people use to talk about or to you? Identifying all possible language triggers and variations can define the help commands, prompts and responses you build.

* **Do** think internationally when developing this list. Consider how definitions could change based on location, language, and culture. Think about how translation will impact the length of your messages.
* **Do not** make up words, introduce new terminology, or use slang. Subtle nuances do not translate well in writing, so it is best to keep things simple as people learn how to interact with your Messenger bot.

### Map out Interactions

Based on the tasks, expectations, and context you want to establish, write out all of the prompts and responses you want to send. Consider the available message types as you write. For example, consider how word choice and placement is impacted by whether a message is text-only or includes a button.

* **Do** center what you write around intent: what you want to accomplish, the actions you want people to take, and what people may want from you. This also makes it easier for you to set expectations and provide context.
* **Do** write multiple versions of each message. This creates a diverse experience and helps you avoid repetition and interaction fatigue. People will stop engaging if your bot always says the same thing.
* **Do not** make your conversations one-sided. Your goals may differ from the people you are talking to. Consider how they might reply and what they might ask of you, and prepare responses accordingly.
* **Do not** use standalone questions. This could imply free form interaction and encourage people to respond in ways you do not support. If you do pose questions, add buttons with specific answers to the message for people to choose from.

Every interaction is an opportunity to evaluate and make improvements to your existing experience and the messages that drive it. Use people’s responses to determine how and where to expand your capabilities.

## Marketing Messages ([Recurring Notifications](/docs/messenger-platform/changelog#may-10--2023))

You should send people high-quality Marketing Messages that they expect to receive, in order to create a high-quality user experience.

Users should expect the Marketing Messages they receive. You can set this expectation by ensuring that:

* Your opt-in request, including the title and image, encompasses the types of Marketing Messages users expect to receive, such as order updates, product recommendations, certain offers
* When sending more than one opt-in request to a user, each opt-in request should clearly state the different, specific types of Marketing Messages the user expects to receive

Marketing Messages should be relevant and tailored to use cases that a user is likely to find valuable

Users can provide feedback on your messaging experience, including blocking your messaging, which may result in restricting your use of Marketing Messages. You should regularly review your opt-in requests and Marketing Messages to see if they meet the best practices above. If your use of Marketing Messages has been rate limited or feature limited, look for ways to make your messaging experience more valuable and relevant for users.

## Tips for Sounding Conversational

Being conversational is a style of writing. It does not impact the experience you build, the message types you use, or what you are actually communicating. While being conversational encourages the use of everyday, colloquial language, it does not mean your messages should be written so casually that you sacrifice communicating core capabilities, misrepresent utility, or break trust.

When determining whether to apply a conversational tone to your existing voice, consider who you are interacting with and the task you are asking them to complete. If you are talking to a business audience or asking someone to confirm personal information, being too casual may create a feeling of caution and discourage people from interacting with you.

A conversational tone should support an experience, not define it. If you want to try applying it to your interactions, the following are some simple ways to implement it without changing the meaning of your messages:

### Use the Active Voice

In an active sentence, the subject of the sentence is doing something. In a passive sentence, something is being done to the subject (making the subject passive). Active voice is also more direct and helps with brevity. “Breaking news is delivered by CNN” is not as clear, short or simple as, “CNN delivers breaking news.”

### Use Contractions

An easy way to make your messages feel conversational is to use shortened versions of words or groups of words. For example, “We cannot wait to get started” feels robotic, whereas “We can’t wait to get started” feels light and casual.

### Standardize Usage of the First and Second Person

Standardize who is speaking in your messages and decide between first person singular (“I” as if an individual is speaking) or first person plural (“We” or “Spring” as if the company is speaking). Use second person (you, your, you're) to address people, so you are talking *to* them and not *at* them.

### Check Your Grammar

While you may be communicating more informally than you are used to, do not break the basic rules of writing. You want to be casual, but you also want to be taken seriously. Proper spelling, capitalization and sentence structure keep the focus on your experience and clarify what you are actually trying to say.

### Be Thoughtful About Punctuation

How and where you use periods, ellipses, exclamation points and the like also plays a part in defining your experience on Messenger. Be mindful of how each impacts your overall tone, but do not be afraid to use punctuation to convey enthusiasm, suspense or other emotions in your messages.

### Consider Your Tone

Writing conversationally does not mean creating an entirely new brand. Your voice is your personality and your tone is how you express that personality. Conversational simply means being more personal in your interactions. Not sure if you are succeeding? Say your responses out loud to hear how they sound when you speak.

Here is an example of how the tone of an order confirmation can differ across delivery channels without changing what is being communicated:

Website | Email | Messenger || Your order has been processed. This is a summary of your purchase:   * Running shoes * Cashmere sweater   We will update your account when these items have shipped. | We received your order. Your purchase includes:   * Running shoes * Cashmere sweater   A confirmation email will be sent once these items have shipped. | Thanks for your order! We'll let you know when your running shoes and cashmere sweater have shipped. |

Writing is best when it is authentic and relatable. You know your brand and experience best, so use your own judgement, do what feels right for you and the audience, and do not be afraid to make adjustments along the way.

## Updates and Alerts

Keep people up-to-date with messages that are timely and relevant to your experience. If an action is completed, follow up with messages confirming the activity and communicate any necessary next steps. If you're building a subscription model, strive to send your updates at the same time each day.

Let people know you’ve processed their information or request. Send receipts for purchases, verify answers to questions, acknowledge preferences, etc.

Give people a way to explicitly opt-in. Be specific about what they’ll receive and how often, and give them a way to opt out or update their preferences.

Don't change the type of info you send without consent. If people signed up for a specific alert, honor their preferences.

Push notifications give people a preview of your updates and alerts, and let them know when you send a new message, even when they’re not in Messenger. Notifications are also an easy way to get people to re-engage.

Be proactive. Tell people who’ve opted into your experience when there’s a message waiting for them.

Consider going “silent”. If you send a lot of messages, silence the notifications for the ones that aren’t time-sensitive.

Don't send too many. If people get overwhelmed by excessive notifications, they may decide to ignore the conversation entirely or block your activity.

## Fail States

While some tools can automate your interactions, remember that you're still communicating with humans. This means that messages and intent are open to interpretation. Be transparent when you receive requests that you don't understand or recognize. Ask for clarification and communicate how you can/can't help.

Re-educate people. If they ask for something outside your experience, reiterate your capabilities, tell people about help commands or use buttons to offer options and redirect them.

Look at each failure as a piece of feedback that tells you what’s working, what isn’t and how you can evolve the way you communicate on Messenger.

Don't expect perfection. No matter how much you plan, anticipate, or respond, people are going to miss details, ask the unexpected, see how much they can get away with and, as a result, get frustrated.

Don't send multiple, identical failure messages. Reduce friction by limiting the number of failure responses people receive and by varying the language in each message.

Your interactions are your opportunity to keep people engaged. Whether they’re used to start a conversation or keep it going, use them to continually set expectations about how your experience works and the value it provides.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)