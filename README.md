## weechat-infohazard

A Python plugin for [weechat](https://weechat.org) that helps you control
information you don't want showing up in your buffers.

When active, this plugin replaces messages from nicks (on any server, for now)
with user-configurable text, so you won't see those messages, but you will see
that a message was sent, which may make the flow of conversations more
discernible than if you had put the nick on `/ignore`. For example:

```
03:14:15     pugnaci0us | x
03:14:42       niceuser | what a terrible thing to say!
03:15:37     pugnaci0us | x
```

I used to use the [`curiousignore.pl` plugin](https://weechat.org/scripts/source/curiousignore.pl/)
but wrote this one to replace it when I wanted to make some customizations

### Configuration

In your weechat's `plugins.conf`, define:

```
python.infohazard.cloaked_text = "[MESSAGE REDACTED]"
python.infohazard.ignore_nicks = "nick1; nick2"
```
