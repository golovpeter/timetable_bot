# Timetable bot
Telegram school timetable bot.

# How to add timetable
Timetables are stored in a folder ```school_classes```. If you want to change timetable, change corresponding file in this directory.

# Deployment

You can deploy this bot in Heroku or in the other cloud platforms.

For Heroku deployment you need to do the next steps:
- Create new Heroku application and connect it with your bot repository;
- Set ```BOT_TOKEN=<your BotFather token>```, ```HEROKU=true``` env variables;
- Install Heroku redis addon and specify ```REDIS_URL=<heroku redis url>``` env variable;
- Deploy application.

# Monitoring tools
- [Health check monitoring](https://uptimerobot.com/)
- [Heroku Redis moniroting](https://data.heroku.com/)
