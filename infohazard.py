try:
    import weechat
except ImportError:
    print("This script must be run under WeeChat.")
    print("Get WeeChat now at: http://www.weechat.org/")


SCRIPT_NAME    = "infohazard"
SCRIPT_AUTHOR  = "SnoopJ"
SCRIPT_VERSION = "0.1"
SCRIPT_LICENSE = "MIT"
SCRIPT_DESC    = "Control information you don't want shown in your buffer"

weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE, SCRIPT_DESC, '', 'utf-8')

version = weechat.info_get("version_number", "") or 0
if int(version) <= 0x00020800:
    msg = f"This plugin requires weechat > 2.8, found version {version}"
    raise RuntimeError(msg)


# TODO:
# * allow ignoring nicks on specific servers
# * allow ignoring hostmasks
# * allow log passthrough as config option?  - meh

IGNORE_NICKS = {nick.strip() for nick in weechat.config_get_plugin("ignore_nicks").split(';')}
IGNORED_MSG_TEXT = weechat.config_get_plugin("cloaked_text") or "x"

def maybe_ignore(data: str, modifier: str, modifier_data: str, msg: str):
    # NOTE: this layout changed after weechat version 2.8
    #plugin, buffer_name, rawtags = modifier_data.split(';', maxsplit=2)
    buffer_name, rawtags = modifier_data.split(';', maxsplit=2)
    tags = rawtags.split(',')

    is_action = any(t == "irc_action" for t in tags)
    is_privmsg = any(t == "irc_privmsg" for t in tags)
    nick = next((t for t in tags if t.startswith("nick_")), "")[5:]

    if is_privmsg and nick in IGNORE_NICKS:
        if is_action:
            result = "*\t" + nick + " " + IGNORED_MSG_TEXT
        else:
            result = nick + "\t" + IGNORED_MSG_TEXT
    else:
        # pass through unchanged
        result = msg

    return result


weechat.hook_modifier("weechat_print", "maybe_ignore", "")
