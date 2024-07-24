This repo was *supposed* to be put on pypi but im too dumb

**Syntax to send a screenshot is:**


image('put your webhook here or a webhook variable')

*and to send text it would be:*

message('webhook url', 'message text', (0, 0, 0)) < last one could be rgb values or built in presets

*to send an error it looks like this:*

error("error message", (0, 0, 0)) < Just like messages the rgb could be replaced by presets

**Some variables you might care about**

show_time              < Shows the time when a message is being sent

webhook_username       < Overrides the webhook name. Dependant on custom_webhook_user. Leaving this blank disables custom_webhook_user.

custom_webhook_user    < Allows you to have a custom webhook name

image_path             < The path to store the image with the name of the file (ex: "screenshots/Screenshot.png")

webhook_gui            < If webhook URL is left as blank a gui will appear asking the user to paste one

custom_gui             < Allows you to have a custom webhook gui

default_webhook_url    < Set to nothing by default but *should* have the webhook URL

user_id                < Should hold the user's discord ID, for pings when you use 'error'.

defualt_embed_color    < The default embed color

image_path             < Set to nothing, should be set to a path of a blank png or just an empty folder.

