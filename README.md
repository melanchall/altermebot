![AlterMeBot Logo](https://github.com/melanchall/altermebot/blob/master/Resources/Images/logo.png)

[AlterMeBot](https://t.me/altermebot) provides a way for Telegram users to be called by aliases instead of mentions.

## Commands

Command|Description
---|---
`/alias <alias>`|Add the specified alias so you can be called with it in the current chat. Min length of alias is 2 and max length is 32. You can add up to 10 aliases.
`/list`|List all your aliases for the current chat.
`/remove <alias>`|Remove the specified alias so you cannot be called with it in the current chat.
`/clear`|Remove all your aliases in the current chat.
`/off`|Disable mentioning you by your aliases in the current chat. This command acts as "Don't disturb" sign on your room in a hotel. None of your aliases removed, bot just stops calling you until you resume mentioning with **/on** command.
`/on`|Enable mentioning you by your aliases in the current chat.
`/lang`|Switch bot's messages language. Buttons with the available languages will be displayed. As you press a button, all messages from the bot will be in selected language from this moment. At now two languages available: English and Russian.
`/help`|Show the help message describing available commands.

## How the bot works

Using `/alias` command you register a phrase that will trigger the bot to mention you in the current chat. At image below we register three aliases: _Sean_, _Human_ and _Tester_:

![Set aliases](https://github.com/melanchall/altermebot/blob/master/Resources/Images/set-aliases.png)

Once you've added all required aliases you can view the list of all your aliases for the current chat with `/list` command:

![List aliases](https://github.com/melanchall/altermebot/blob/master/Resources/Images/list-aliases.png)

Now every time the bot will see aliases in a chat message it will send mentions of users aliases were registered for. At image below the bot was triggered by _Sean_ word which is alias we've registered before:

![Bot triggered](https://github.com/melanchall/altermebot/blob/master/Resources/Images/triggered.png)

At any moment you can remove some alias with `/remove` command or all your aliases for the current chat with `/clear` command. At image below _Human_ alias was removed so we cannot be called by it anymore:

![Remove alias](https://github.com/melanchall/altermebot/blob/master/Resources/Images/remove-alias.png)
