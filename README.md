# pinbot

An easy self-hosted pinbot to get pin things in the right places.

I'm not sure why but I'm creating a Dockerfile for this. Make sure to change the appropriate environment variables. Or use an envfile. Probably should use an envfile or pass it in during the Docker run portion.

| Variable | Explanation|
| -------- | -----------|
| DISCORD_KEY | The Discord bot key you can get on the Discord application manager|
| PIN_CHANNEL | The ID of the Discord channel you want to send pins to | 
