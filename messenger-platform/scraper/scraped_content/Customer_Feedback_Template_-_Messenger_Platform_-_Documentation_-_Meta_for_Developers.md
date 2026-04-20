# Customer Feedback Template - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/send-messages/templates/customer-feedback-template

# Customer Feedback Template

This functionality is in development. Meta can change or remove this functionality at any time.

Messenger helps brands build lasting relationships through conversation. Whether you are talking to a loyal customer or someone brand new, Messenger lets businesses help customers with their pre and post purchase inquiries. Every interaction is an opportunity for the businesses to delight the customer. And, businesses now have more robust tools such as Customer Feedback Template to measure the experience they provide to their customers. With Customer Feedback Template businesses can:

1. **Increase response rates** for your customer feedback surveys with Messenger’s native customer feedback template.
2. **Aggregate customer satisfaction ratings across channels easily** with built-in Messenger templates such as Customer Satisfaction (CSAT), Net Promoter Score (NPS) and Customer Effort Score (CES) surveys.
3. **Reduce biases and inconsistency** in survey scores with optimized UX.

CSATCESNPS![](https://scontent.fdac31-1.fna.fbcdn.net/v/t39.2365-6/192379282_159923619437508_6420384473285754162_n.gif?_nc_cat=110&ccb=1-7&_nc_sid=e280be&_nc_ohc=9N45DOynf2sQ7kNvwEvayxS&_nc_oc=AdocitX6I6DIpC27iFS_ybCN4STH-YmusUr26kHtRR18UWcnq4xHRkgIQLgH_V04bj8&_nc_zt=14&_nc_ht=scontent.fdac31-1.fna&_nc_gid=Z0GoImd5ETirMR0EGjLXKw&_nc_ss=7a30f&oh=00_Af1pVOdB7OUgDF3CGo_xvlfDOJ3P0yg_iKcGSySGai1jhQ&oe=6A002AF7)![](https://scontent.fdac31-1.fna.fbcdn.net/v/t39.2365-6/192394645_784940269049775_2246604535870055803_n.gif?_nc_cat=111&ccb=1-7&_nc_sid=e280be&_nc_ohc=TwFqKffBkaAQ7kNvwHYvN5P&_nc_oc=Ado7bqmOLXg1HhuWzRbGdMqzTvO6VKsvr8K7tTDBmeixMdhKqSJWNQOJq3PbYmyUols&_nc_zt=14&_nc_ht=scontent.fdac31-1.fna&_nc_gid=Z0GoImd5ETirMR0EGjLXKw&_nc_ss=7a30f&oh=00_Af2Joxvj5Y19ZZPeSuJW-0cq_oo9wNwZGUmEu7Lyw18npg&oe=6A003D6A)![](https://scontent.fdac31-1.fna.fbcdn.net/v/t39.2365-6/192703940_158265832933445_2830539281971663398_n.gif?_nc_cat=105&ccb=1-7&_nc_sid=e280be&_nc_ohc=94r5s0Re4UYQ7kNvwEtK9go&_nc_oc=AdoIKkjfsVkcdq7H1i1-1ypTAIVd892l7Q_sBq5soIzOjNdzcruDEUbj86zb9b78L4w&_nc_zt=14&_nc_ht=scontent.fdac31-1.fna&_nc_gid=Z0GoImd5ETirMR0EGjLXKw&_nc_ss=7a30f&oh=00_Af36wePVakREPtWymqDCg44ne4t8tEThwotB8lmQxbV2kQ&oe=6A005CEC)

### Use case details:

**Allowed:**

* Post purchase feedback collection via NPS
* Post customer service conversation feedback collection via CSAT and CES

**Not allowed:**

* User research survey unrelated to a preceding interaction
* Promotional survey, any survey wording or content that are promotional in nature

## Flow Walkthrough

![](https://lookaside.fbsbx.com/elementpath/media/?media_id=775452453240997&version=1774310710)

A typical flow using the Customer Feedback template is shown above:

1. After a case has been completed the Customer Feedback template is triggered into the thread via the Send API (detailed in sections below). The template will have a title, disclaimer and a button to start the rating flow.
2. Tapping the button will trigger the bottom sheet to pop up which will have the configured scoring components.
3. A customer selects a score and can provide additional text if the business has configured the free-form text input (detailed in sections below). Once the scores are selected the Submit button pops up.
4. Customer completes feedback and taps the Submit button.
5. Feedback is sent to the business via the configured web-hook URL.
6. The bottom sheet collapses and the template in the thread will have the button replaced with Complete. An admin text will show that the feedback has been shared with the business.
7. Note: As long as the Submit button is not tapped, the customer can collapse and come back to give feedback provided the template has not expired (an expiry can be set for the template, detailed in sections below)

Details of the template and its setup is provided in the following sections.

## Score Types

We support the most commonly used scoring standards in the industry which include CSAT, NPS, CES as well as Free Form inputs.

Below are the various scoring options and their nomenclature for our API calls.

```
Score Type: CSAT
    type: "csat "
    default_title: "How would you rate your experience with <business>?"
    options: "one_to_five", "five_stars" (default if no option set), "five_emojis"
    payload: "1", "2", "3", "4", "5"
    
Score Type: NPS
    type: "nps"
    default_title: "How likely are you to recommend <business> to a friend?"
    options: "zero_to_ten" (also default if no option set)
    payload: "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
    
Score Type: CES 
    type: "ces"
    defaut_title: "Overall, how easy was it to solve your problem today?"
    options: "one_to_seven" (also default if no option set)
    payload: "1", "2", "3", "4", "5", "6", "7"
```

**CSAT(Customer Satisfaction Score)** will be able to support views with 1 to 5, 5 stars or 5 emojis, default if none is provided would be **“five\_stars”**. You can provide your own custom title for the question, if none is provided, the **default\_title** will be chosen. Note: default\_titles will be translated and localized to the locale of the user. Custom titles will not be translated, you would have to perform the translation yourselves if needed.

Selecting a score in any of the view formats will translate to a numeric score from 1 to 5 which will be the value that would be sent to your web-hook. That is what the payload fields show above. An example CSAT view using five\_stars is shown below.

![](https://scontent.fdac31-2.fna.fbcdn.net/v/t39.2365-6/104114593_540263709976958_4941858584795044930_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=VsBE9WrkNLsQ7kNvwEoxFtv&_nc_oc=AdpKoj1maedsp6-pKS83V6s8ExLoUs05lQJrWP08W83G67wS2WwI9hQs_zvwXze-UsU&_nc_zt=14&_nc_ht=scontent.fdac31-2.fna&_nc_gid=Z0GoImd5ETirMR0EGjLXKw&_nc_ss=7a30f&oh=00_Af3zreo9EtTVi228YUV1ip2dPUIDHg-tCze8fjLUFQPQmQ&oe=6A0059D1)

**NPS(Net Promoter Score)** will be able to support views with numbers from 0 to 10, default if none is provided would be **“zero\_to\_ten”**.. You can provide your own custom title for the question, if none is provided, the **default\_title** will be chosen. Note: default\_titles will be translated and localized to the locale of the user. Custom titles will not be translated, you would have to perform the translation yourselves if needed.

Selecting a score will translate to a numeric score from 0 to 10, which will be the value that would be sent to your web-hook. An example NPS view is shown below.

![](https://scontent.fdac31-2.fna.fbcdn.net/v/t39.2365-6/103631685_656826515174329_6652044623311997817_n.png?_nc_cat=100&ccb=1-7&_nc_sid=e280be&_nc_ohc=ykSRuU1GnwUQ7kNvwEHeAdJ&_nc_oc=AdqSwPAq-2qtI4W08ty90DO3n5CUPKNoOeQ3QBeGj02jiygl1ZS2BI-xU1f4wIQ2ToM&_nc_zt=14&_nc_ht=scontent.fdac31-2.fna&_nc_gid=Z0GoImd5ETirMR0EGjLXKw&_nc_ss=7a30f&oh=00_Af0JrOvU7K1OudjZVE8znCnI-GYQr4DjJ1Z6Af7CTURYvQ&oe=6A00448B)

**CES(Customer Effort Score)** will be able to support views with numbers from 1 to 7, default if none is provided would be **“one\_to\_seven”**. You can provide your own custom title for the question, if none is provided, the **default\_title** will be chosen. Note: default\_titles will be translated and localized to the locale of the user. Custom titles will not be translated, you would have to perform the translation yourselves if needed.
Selecting a score will translate to a numeric score from 1 to 7, which will be the value that would be sent to your web-hook. An example CES view is shown below.

![](https://scontent.fdac31-1.fna.fbcdn.net/v/t39.2365-6/102468843_552125318756128_3061439580152725875_n.png?_nc_cat=105&ccb=1-7&_nc_sid=e280be&_nc_ohc=HpHS2eib4IwQ7kNvwFw91gb&_nc_oc=AdpdUT7sFm2Zg5nQnnjjuznjXS778_4tvwV1JCRr4AgxfnPYFN9I5sW1oB2G0ORWq-4&_nc_zt=14&_nc_ht=scontent.fdac31-1.fna&_nc_gid=Z0GoImd5ETirMR0EGjLXKw&_nc_ss=7a30f&oh=00_Af2QopZfYKJF-Y5YQ6Jr0RZZR5kK8ahNQQemC4lDtc85Ug&oe=6A005041)

**Optional Free Form Input Field**: To each of the score types you can also attach an additional free-form input. This input can be optionally set and can be used if you need text feedback in addition to the score a customer selects. Please note, a customer can choose to submit a score without providing text feedback. **Also, the form input has a character limit of 400**. Below is an example for a CSAT score type with five\_stars and the additional free-from input.

![](https://scontent.fdac31-1.fna.fbcdn.net/v/t39.2365-6/103264941_339812680321966_5268255617441433079_n.png?_nc_cat=106&ccb=1-7&_nc_sid=e280be&_nc_ohc=rWbfBSH-UvkQ7kNvwF3zuOZ&_nc_oc=AdrSklGfreWZhqxC4-34Cw4ZJr-91Na2MA2K2I50565rr6gnp1zkgoYi2pSQ-NOIYhU&_nc_zt=14&_nc_ht=scontent.fdac31-1.fna&_nc_gid=Z0GoImd5ETirMR0EGjLXKw&_nc_ss=7a30f&oh=00_Af1LqjkxVIReCwh9ZtdKyVYPHvXYYaYB9R1tO25XcTLQZQ&oe=6A0057DC)

## Score Labels

For each of the scoring options you can also set the score labels to clearly define the level of the lowest value and the highest value in the template. The values that you can use are below. Please note, some values are default for certain score options, provided in parentheses below. For e.g. if no score label for CSAT is provided, it will take neg\_pos as the default. You could also choose "none" if you would like to not show any labels at all.

```
"neg_pos" = Negative - Positive (default value for CSAT)
"hard_easy" = Hard - Easy (default value for CES)
"dis_sat" = Very Dissatisfied - Very Satisfied
"unlike_like" = Very Unlikely - Very Likely (default value for NPS)
"poor_great" = Poor - Great
"none" = ""
```

For eg. a CSAT five\_stars score option with *neg\_pos* set would show the Negative and Positive indicators as below.

![](https://scontent.fdac31-1.fna.fbcdn.net/v/t39.2365-6/103782756_396685794556196_3062528507879611930_n.png?_nc_cat=111&ccb=1-7&_nc_sid=e280be&_nc_ohc=xDh_wDOmFyAQ7kNvwE6_4EW&_nc_oc=Adp5yAa2DrHM4v46aUaksFlKnSBfsfBzy-BpyRYO4qwrRRcnjoSAnZvTsY1vy6Smo34&_nc_zt=14&_nc_ht=scontent.fdac31-1.fna&_nc_gid=Z0GoImd5ETirMR0EGjLXKw&_nc_ss=7a30f&oh=00_Af3PnIvP48N2P4P6FPdLsNhxlaPDkv4j3tGHxB_efkdTeQ&oe=6A004738)

## 24 hour restriction

The standard messaging window for sending the template to a user is 24 hours after the user's last message. We encourage you to send the template within the 24 hour window for better customer experience and response rates. We also recognize that sometimes surveys will need to be sent outside this window. For that, you can use the [message-tag](https://developers.facebook.com/docs/messenger-platform/send-messages/message-tags#sending): **CUSTOMER\_FEEDBACK** while sending the template. This tag allows you to send the template within 7 days after the user's last message.
Please note, the tag can only be used with the customer feedback template. Use in any other form is prohibited and will fail.

## API details:

### Sending a template to the thread:

With the specific nomenclature out of the way, let us now look at the API that can be used to send the Customer Satisfaction Template to a thread.

A call should be made to the Send API with the following POST structure. Example values filled in:

```
  curl -X POST -H "Content-Type: application/json" -d '{
  "recipient": {
    "id": "<PSID>"
  },
  "message": {
    "attachment": {
      "type": "template",
      "payload": {
        "template_type": "customer_feedback",
        "title": "Rate your experience with Original Coast Clothing.", // Business needs to define. 
        "subtitle": "Let Original Coast Clothing know how they are doing by answering two questions", // Business needs to define. 
        "button_title": "Rate Experience", // Business needs to define. 
        "feedback_screens": [{
          "questions":[{
            "id": "hauydmns8", // Unique id for question that business sets
            "type": "csat",
            "title": "How would you rate your experience with Original Coast Clothing?", // Optional. If business does not define, we show standard text. Standard text based on question type ("csat", "nps", "ces" >>> "text")
            "score_label": "neg_pos", // Optional
            "score_option": "five_stars", // Optional
            "follow_up": // Optional. Inherits the title and id from the previous question on the same page.  Only free-from input is allowed. No other title will show. 
            {
              "type": "free_form", 
              "placeholder": "Give additional feedback" // Optional
            }
          }]
        }],
        "business_privacy": 
        {
            "url": "https://www.example.com"
         },
        "expires_in_days" : 3 // Optional, default 1 day, business defines 1-7 days
      }
    }
  }
}' "https://graph.facebook.com/v7.0/me/messages?access_token=<PAGE_ACCESS_TOKEN>"
```

### API Properties:

Property | Type | Description || `id` | String | *Required*. The `PSID` of the customer. |
| `attachment.type` | String | *Required*. Must be "template". |
| `template_type` | String | *Required*. Must be "customer\_feedback". |
| `title` | String | *Required*. Defines the main title of the template that gets sent to the thread with the button to open the feedback form. **Max 65 chars allowed. No URLs.** |
| `subtitle` | String | *Required*. Defines the sub-title of the template that gets sent to the thread with the button to open the feedback form. **Max 80 chars allowed. No URLs.** |
| `button_title` | String | *Required*. Defines the button title for the button that will open the feedback form. **Max 20 chars allowed. No URLs.** |
| `feedback_screens` | Array<`Objects`> | *Required*. This is an array of objects. Each object represents 1 page. Please note we only support one page and one question per page right now. If multiple pages or multiple questions per page are set, we will throw an error back. |
| `questions` | Array<`question`> | *Required*. Each page may have up to 1 questions. This is an array of objects. Each object represents 1 question. |
| `question.id` | String | *Required*. Alphanumeric. Maximum 80 characters. Must be unique throughout the entire form. You shall use these as the unique identifiers of the questions which would be sent back in the response to help you tie context back to your system. Ids should be alpha numeric and can contain any number of underscores(\_) for e.g. banjkkl\_\_2345 is a valid id, abnj-4567 is not a valid id due to the “-”. |
| `question.type` | String | *Required*. The type of the question. Currently supported values include: "csat", "nps", "ces", "free\_form. Please check Score Types section above for more details. |
| `question.title` | String | *Optional*. You can provide your own custom title for the question, if none is provided, the default\_title will be chosen. Please check Score Types section above for more details. Note: default\_titles will be translated and localized to the locale of the user. Custom titles will not be translated, you would have to perform the translation yourselves if needed. **Min 5 chars and Max 85 chars allowed. No URLs.** |
| `question.score_label` | String | *Optional*. Field to define the level labels for low and high values. Please check Score Level Indicators section above for details. Values include 'neg\_pos', 'hard\_easy', 'dis\_sat', 'unlike\_like','poor\_great' |
| `question.score_option` | String | *Optional*. Field to define the score selector views. For e.g. values include '1\_to\_5', 'five\_stars', 'five\_emojis' for csat type. Please check Score Types section above for more details. |
| `question.follow_up` | `Object` | *Optional*. Object to set a free form input. Inherits the title and id from the previous question on the same page. Only free-from input is allowed. |
| `question.follow_up.type` | String | *Required*. Set value as 'free\_form'. |
| `question.follow_up.placeholder` | String | *Optional*. Placeholder to be shown inside the free form text input. Defaults to **"Give additional feedback"**, if none provided. **Max 65 chars allowed. No URLs.** |
| `business_privacy` | `Object` | *Required*. Object to provide your privacy policies in the template. |
| `business_privacy.url` | String | *Required*. The link to your hosted privacy policy. Example, the "privacy policy" link in the screenshots. You only need to provide the URL, and the link text will be automatically generated in the template. |
| `expires_in_days` | Integer | *Optional*. Set the time for template expiration in minutes. You can set a value between 1 to 7. Unit is days. If no value is set then a default of 1 day would be set. |

![](https://scontent.fdac31-2.fna.fbcdn.net/v/t39.2365-6/103260056_2779439025617991_1201279550415615271_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=b6z3IjuFR94Q7kNvwHNS9jZ&_nc_oc=AdrvdbINczwE8nIh89ndI4XtMtXl_x0C49LM4n1fYv0ghZkwUifb_tKH2gK3uZ0IZdA&_nc_zt=14&_nc_ht=scontent.fdac31-2.fna&_nc_gid=Z0GoImd5ETirMR0EGjLXKw&_nc_ss=7a30f&oh=00_Af2IS86EOFfZ7Jt2mmsnGX0AJsfHv-TSlqw3E-GZQGvdSg&oe=6A0055F4)

### Restrictions:

Please re-note the following restrictions that apply to the template.

* A template can have:
  + 1 title + 1 scoring component + 1 free-form input box
  + 1 title + 1 scoring component
  + 1 title + 1 free-form input
* A template CANNOT have:
  + More than 1 title
  + More than 1 scoring component

Please check individual field restrictions in the API properties table above.

### Receiving data on submission:

After the template is sent in thread, you shall wait and expect the customer to fill in the information and submit it. Your web-hook server will receive a “**messaging\_feedback**” event (i.e., an event that contains the submitted data) once the customer submits the feedback. Please ensure you have subscribed to the “**messaging\_feedback**” webhook subscription for your app and page in the app dashboard.

Note: The customer will have the time; set in the **expires\_in\_days** field of the send request (default 1 day, if not set) to fill the template and submit the feedback. The form will auto-expire after the set time, after which the in-thread entry point will no longer be available.

The received feedback event will be as below:

```
  {
  "object": "page",
  "entry": [{
    "time": <timestamp>,
    "messaging": [{
      "sender": {
        "id": "<PSID>"
      },
      "recipient": {
        "id": "<page_id>"
      },
      "messaging_feedback": {
        "feedback_screens": [{
          "screen_id": 0,
          "questions": {
            "hauydmns8": {
              "type": "csat",
              "payload" : "5",
              "follow_up": {
                "type": "free_form",
                "payload" : "I am very satisfied!"
              }
            }
          }
        }]
      }
    }]
  }]
}
```

### Receive Event Properties:

Property | Type | Description || `time` | Integer | The timestamp when the customer submits the feedback. |
| sender `id` | String | The customer `PSID`. |
| recipient `id` | String | The page `ID` of your business page. |
| `messaging_feedback` | `Object` | The standard key of a “messaging\_feedback” event. This holds an array of feedback\_screens with an array of object of feedback question responses. |
| `messaging_feedback.feedback_screens` | Array<`Objects`> | Holds feedback by the customer. Each object represents a form page of your original request, with customer feedbacks. Each object has a key “screen\_id”, which is the form page index, and a key “questions”, which holds your question ids and customer answers. The objects are present in the same sequence as your original request. |
| `feedback_screens.questions` | `Object` | Holds questions in a form page. Each object has the key as the question id, and the value answered by the customer. |
| `question.<id>` | String | question.id set in the Send API request, as a key to the responses submitted by the customer. |
| `question.<id>.type` | String | Defines the type of the scoring mechanism used. For e.g csat, nps, ces etc |
| `question.<id>.payload` | String | Score value selected by the customer. |
| `question.<id>.follow_up` | `Object` | Object that stores the value of the free form text input if set. |
| `follow_up.type` | String | Will be set to free\_form to identify free form responses vs other responses. |
| `follow_up.payload` | String | Free form text feedback provided by the customer. |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)