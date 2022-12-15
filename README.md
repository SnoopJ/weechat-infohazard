## weechat-infohazard

A Python plugin for [weechat](https://weechat.org) that helps you control
information you don't want showing up in your buffers.

I used to use the [`curiousignore.pl` plugin](https://weechat.org/scripts/source/curiousignore.pl/)
but wrote this one to replace it when I wanted to make some customizations

### Configuration

In your weechat's `plugins.conf`, define:

```
python.infohazard.cloaked_text = "[MESSAGE REDACTED]"
python.infohazard.ignore_nicks = "nick1; nick2"
```
