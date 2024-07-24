I've decided to turn this repo into a Python package,

Syntax to send a screenshot is:


image('put your webhook here or a webhook variable')

and to send text it would be:

message('webhook url', 'message text', (0, 0, 0) < last one is embed color NOT text color

Some variables you might care about

show_time              < Shows the time when a message is being sent

webhook_username       < Overrides the webhook name. Dependant on custom_webhook_user. Leaving this blank disables custom_webhook_user.

custom_webhook_user    < Allows you to have a custom webhook name

image_path             < The path to store the image with the name of the file (ex: "screenshots/Screenshot.png")

webhook_gui            < If webhook URL is left as blank a gui will appear asking the user to paste one

custom_gui             < Allows you to have a custom webhook gui

