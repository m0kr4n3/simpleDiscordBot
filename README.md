# a simple discord bot written with python

It has 3 commands for initiation with Discord API:
 * !hello (it says hello)
 * !create_channel channel_name (it creates a text channel in the server and it requires `admin` role)
 * !mul a b (multiplies a and b)


# Usage
1. Clone the repo
```bash
git clone https://github.com/m0kr4n3/SimpleDiscordBot
cd SimpleDiscordBot/
```
2. Install requirements
```bash
pip3 install -r requirements.txt
```
3. Create a discord application and get an Application token, check out the [documentation](https://discord.com/developers/docs/intro)
4. Set your `DISCORD_TOKEN` and `DISCORD_GUILD` in .env file like that :
```
# .env
DISCORD_TOKEN={your-bot-token}
DISCORD_GUILD={your-guild-name}
```

4. Run the [bot.py](./bot.py)
```bash
python3 bot.py
``` 

Enjoy !


