# Timetable bot
Telegram school timetable bot.

# How to add timetable.
Timetables are stored in a folder ```school_classes```. If you want to change timetable, change corresponding file in this directory.

# Deployment.

You can deploy this bot in Heroku or in the other cloud platforms.

For heroku deployment you need to do the next steps:
- Create new heroku application and connect it with your bot repository;
- Set ```BOT_TOKEN=<your BotFather token>```, ```HEROKU=true``` env variables;
- Install redis addon and specify ```REDIS_URL=<heroku redis url>``` env variable;
- Deploy application.
