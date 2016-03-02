from pyoanda import Client, PRACTICE

client = Client(
    environment=PRACTICE,
    account_id="{{ACCOUNT_ID}}",
    access_token="{{ACCOUNT_TOKEN}}"
)


events = client.get_events()
for chunk in events.iter_content(2054):
    print chunk
