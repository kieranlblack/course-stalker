# Course Stalker
Script to check GA Tech class matrix every couple of seconds to see if positions in a set of classes have opened. Very useful during class registration as it is faster than Coursicle.
## Setting up Config
### Example Config
```yml
number: 1234567890
sms_gateway: '@vtext.com'
email: 'georgeburdell@gmail.com'
password: 'gojackets1!'
term: 202008
courses:
  - 87136 # linear 2
  - 87138 # marching band
```
| Key         | Value                                  |
| ----------- | -------------------------------------- |
| number      | phone number to send notifications to  |
| sms_gateway | [carrier gateway for sms](https://en.wikipedia.org/wiki/SMS_gateway#Email_clients) |
| email       | email address of account used for smtp |
| password    | password<sup>1</sup>                   |
| term        | current term<sup>2</sup>               |
| courses     | list of all courses to track           |

(1) For a gmail account I highly recommend generating an app password exclusively for this script. To do this go to Google Account > Security > Signing in to Google > App passwords. [Guide here](https://support.google.com/mail/answer/185833). \
(2) To find the current term go to oscar > Registration > Select Term. Open the developer console (f12) and navigate to the Network tab, ensure that network activity is being recorded then select the current term and click submit. In the activity on the Network tab there should be something with the name of `bwcklibs.P_StoreTerm`. Click on this and then scroll down in the Headers to find the form data. The number you want is the one right after `term_in`.

## Notes
- If not running on windows disable all the win10toast notifications.
- If you set the delay between each check lower than 3 seconds requests might not have enough time to complete which will break things.