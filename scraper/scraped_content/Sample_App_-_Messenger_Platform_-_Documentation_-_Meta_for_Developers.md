# Sample App - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/getting-started/sample-experience

# Sample Messenger Experience with Original Coast Clothing

Original Coast Clothing (OCC) is a fictional clothing brand that we created to showcase the key features of the Messenger Platform. This guide shows you how to download the code for this sample app on your local environment or remote server to learn more about the features Messenger has to offer.

In order to showcase the full Messenger experience with multiple entry points, our fictional business has the following features:

* An [automated Messenger experience](https://l.facebook.com/l.php?u=https%3A%2F%2Fm.me%2FOriginalCoastClothing%3Fref%3DDEVDOCS&h=AT4XOZvmSCceGv2roCb1h44k3zKu7OFQmnkd60fKpiCMHTCgxd5i3KyuJ24HFh_USRLuNizdEzrRQXji4uSUjjDvkyTzbewXyPhXgYPIrxeqPt9eMghtDQb70J54uZttO-Pa-XV8gSM0bw_m) for organic reach outs
* Lead Generation in Messenger with API enabled follow ups. [Inject this lead generation ad](https://www.facebook.com/ads/experience/confirmation/?experience_id=2170497373124589) to demo it.
* A [QR code](/docs/messenger-platform/discovery/m-me-links/) that triggers a promotional discount for [the summer collection](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.originalcoastclothing.com%2Fcollections%2Fsummer&h=AT4l2Qn8vJXnX1TCeFp-4RtTGJYXre3P6NKpLBHRb80OPcHg6b8i3Ikzhd6D0RVzXcbKulob8QQ9dCmJ9Mn2mXV-BriZi2yMWkmoWaDFbby4KqVnmzau4rzicpCOPOxPS1l74qq_B32Ml3F0),
* A [Facebook Page](https://www.facebook.com/OriginalCoastClothing/) with a [Click to Messenger Ad](/docs/messenger-platform/discovery/ads) displayed as a [Page post](https://www.facebook.com/permalink.php?story_fbid=567094500360701&id=542998526103632)
* An [Instagram experience](/docs/messenger-platform/instagram/sample-experience/)

![](https://lookaside.fbsbx.com/elementpath/media/?media_id=711744376097957&version=1775806213)[View the Messenger Experience with OCC](https://l.facebook.com/l.php?u=https%3A%2F%2Fm.me%2FOriginalCoastClothing%3Fref%3DDEVDOCS&h=AT5HOvnMEO5k-DHCr9u7djnvwuVsggCXgy7RIORiMCGzHioqUY1nOCwDRImQ2fezvPPVQgaXdns3bOJ4oeErgrr148PRK8iMuyMopqBUQkByUoljsWvoASTQrfNZPe48SndnBiA3J4AiD12NYh-nCssvcMW6uA)

### Platform Features

This sample app leverages the following features:

|  |  |
| --- | --- |
| * [Click To Messenger Lead Ads](/docs/messenger-platform/discovery/lead-generation-ads-in-messenger) * [Buttons](/docs/messenger-platform/send-messages/buttons) * [Get Started Button](/docs/messenger-platform/reference/messenger-profile-api/get-started-button) * [Persistent Menu](/docs/messenger-platform/reference/messenger-profile-api/persistent-menu) * [Personas](/docs/messenger-platform/send-messages/personas/) | * [Quick Replies](/docs/messenger-platform/send-messages/quick-replies) * [Templates](/docs/messenger-platform/send-messages/templates) * [User Profile API](/docs/messenger-platform/identity/user-profile/) * [Webhooks](/docs/messenger-platform/webhook) * [Welcome Page](/docs/messenger-platform/reference/messenger-profile-api/greeting) |

## Deploy this experience on Messenger

By the end of this guide, you'll have a full Messenger app running on your server, answering messages from your test Page.

### Before You Start

You will need:

* A [Facebook Page ID](/docs/pages) – This is the ID for your live Facebook Page or a test Page.
* A [Meta Developer Account](/docs/development/register)
* [Meta App ID](/docs/development/create-an-app)
* [Meta App Secret](/docs/development/create-an-app/app-dashboard/basic-settings#app-secret)
* A [Page Access Token](/docs/facebook-login/guides/access-tokens) requested from a person who can [`CREATE_CONTENT` task](/docs/facebook-login/guides/access-tokens#pagetokens) on the Page
* The [`pages_messaging`, `pages_show_list`, and `pages_manage_metadata` permissions](/docs/pages/overview/permissions-features#permissions)
* The [sample code](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffbsamples%2Foriginal-coast-clothing&h=AT4-CldXSYU-0BZeyPOxisvhleW2GdWhsF4rlq30tECZCHj41akWFdViht4WX4Qkm9mRwWZLgThdNYGimn1bpxmvPNvnnqVCCAl2FZ1u2TINHTT-3NQi7QFtJsPZfyBOzqp16cDYwMZRUaOU) located on GitHub

If you have separate development, staging, and production environments, each environment will need its own Meta App and Facebook Page.

## Local Environment Setup

To run the sample app on your local environment you will need [NodeJS](https://l.facebook.com/l.php?u=https%3A%2F%2Fnodejs.org%2F&h=AT7Ctz64MDDeYMiYRPaVUyN6rYk4hbf-TGotTx-FeDXJ60Wa-aNR6egL8jAdYBoFjTrnriyLPbpmofNEDQjJ-r9yRqDpfHiLKzbPSAx0e-GhYLmnLZVrIP0EVActXI_UIft0MfZwBP0a6Us-) 10.x or later.

### Step 1. Clone the Sample App Repository

Clone the `original-coast-clothing` repository on your local machine.

```
git clone https://github.com/fbsamples/original-coast-clothing.git
cd original-coast-clothing
```

### Step 2. Install the Code Dependencies

```
yarn install
```

### Step 3. Get an External Address

In order to receive messages, you need to be able to get incoming webhooks from our Servers.

If you need an external address, use [`ngrok`](https://l.facebook.com/l.php?u=https%3A%2F%2Fngrok.com%2Fdownload&h=AT7XeT9vDFo2qd8KJCZUhPpbgyorRgldG1c_UvU6z346h867C-tqO1vE-TbhO_vdueYQEf9D2hxfaknTvFoTB1qLbIg-Jfg4Pj5SoGUe9u6vi7o3FxW23OekASL9Qvd-mSibfQ_6hBvDgxoC) since it will provide an external https address that will tunnel into your NodeJS app.

**Install `ngrok`**

```
npm install -g ngrok
```

**Request a tunnel to your local server with your preferred port**

```
ngrok http 3000
```

The screen should show the `ngrok` status:

```
Session Status                online
Account                       Redacted (Plan: Free)
Version                       2.3.35
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://1c3b838deacb.ngrok.io -> http://localhost:3000
Forwarding                    https://1c3b838deacb.ngrok.io -> http://localhost:3000

Connections                   ttl     opn     rt1     rt5     p50     p90
0       0       0.00    0.00    0.00    0.00
```

Take note of the `https` URL of the external server that is fowarding to your local machine. In the above example, it is `https://1c3b838deacb.ngrok.io`.

### Step 4. Set Webhooks and Messenger Profile

**Copy the sample environment template in your app**

```
mv .sample.env .env
```

**Add your environmental values**

Edit the `.env` file to add the values for your Facebook App ID, your Facebook Page ID, your Page access token, and your App Secret. Set the value of `VERIFY_TOKEN` to a random string. Your app will use it to validate API calls.

### Step 5. Run Your App

```
node app.js
```

You should now be able to access the application in your browser at `http://localhost:3000`

### Step 6. Configure Your App

Run the following command to configure the webhooks subscription settings for your app and the Page Messenger Profile. Note that you need to use the value for `VERIFY_TOKEN` added in `.env` file.

`http://localhost:3000/profile?mode=all&verify_token=<VERIFY_TOKEN>`

### Step 7. Test Your App Setup

Send a message to your Page from Facebook or in Messenger, if your webhook receives an event, you have fully set up your app!

### Make a Code Change

Let's edit the file **locales/en\_US.json**, replacing the message under get\_started.welcome and change it from "Hi {{userFirstName}}! Welcome to Original Coast Clothing..." to something else.

Back on the first terminal, every time you change the code, you'll need to restart the NodeJS server. Let's stop the server with Ctrl-C and run it again, to reload the new code.

```
node app.js
```

Open your Messenger and message your Page the word "Hi", you should get the new message.

## Heroku Setup

A [Heroku instance](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevcenter.heroku.com%2Farticles%2Fheroku-cli&h=AT4CCWOJASqBOWEyDj1Inymi_mSUr1IOTbsE8uyr7RBnBjQ82FE85wZbgGKemh7mNs9oUA6UaE5ERcrh21M4PDMMr2Jfx8IZvYIpUD5clb6B_8Iii-eYdo9rrjHAFaAjWO0NrSk0-GSEVzMK) can be useful to host the production or staging environment for your business app or website.

### Step 1. Create a Heroku App

```
git init
heroku apps:create
# Creating app... done, ⬢ YOUR-APP-NAME
# Created http://YOUR-APP-NAME.herokuapp.com/ | git@heroku.com:YOUR-APP-NAME.git
```

### Step 2. Deploy the Code to Heroku

```
heroku git:remote -a YOUR-APP-NAME
git push heroku master
```

### Step 3. Set Environment Variables

Find the **Config Vars** of your app, in the your Heroku app dashboard under Settings. Add the values for your Facebook App ID, your Facebook Page ID, your Page access token, your App Secret, and create a `VERIFY_TOKEN`.

### Step 4. Set webhooks and Messenger Profile

You should now be able to access your app. Use the `VERIFY_TOKEN` that you created as config vars and call the **/profile** endpoint.

`https://YOUR-APP-NAME.herokuapp.com/profile?mode=all&verify_token=<VERIFY_TOKEN>`

***Optional***
The above URL will return the ids of personas uploaded. Since they are held in memory, you need to add those returned IDs as Config Vars, so they can persist after a reload.

```
heroku config:set PERSONA_BILLING=<PERSONA_ID> -a YOUR-APP-NAME
heroku config:set PERSONA_ORDER=<PERSONA_ID> -a YOUR-APP-NAME
heroku config:set PERSONA_SALES=<PERSONA_ID> -a YOUR-APP-NAME
```

### Step 5. Test Your App

Send a message to your Page from Facebook or in Messenger. If your webhook receives an event, you have fully set up your app!

## Troubleshooting

### Rerun app locally

After running ngrok, a new external address will be provided. Update the `APP_URL` address on the `.env` file, then run the NodeJS server.

```
node app.js
```

Update the webhook address on the Facebook App Settings by visiting `http://localhost:3000/profile?mode=webhook&verify_token=<VERIFY_TOKEN>`

### My Page only replies to me, but not someone else

The Facebook app is likely still in Development Mode. You can add someone as a tester of the app, if they accept, the app will be able to message them. Once ready, you may request the `pages_messaging` permission to be able to reply to anyone.

## Learn More

* [Webhooks Guide](/docs/graph-api/webhooks)
* [Facebook Pages API](/docs/pages)

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)