# slack-status-update

To run it use:

```bash
python slack-update.py
```

But first create a file called `config.py` into the same folder and put it in:

```python
xoxp_token = "xoxp-1-2-3-4"
text = "...coming home to your shelter..."
emoji = ":notes:"
```

Where the content `text` will be your status and `emoji` the name of the _emoji_ to display.

Finally the content of `xoxp_token` must be your _legacy token_, that you obtain it from your Slack account (https://api.slack.com/custom-integrations/legacy-tokens).