# Shad0w + Kiriyn (Mojang Account Creator)

### Selenium Based Mojang Account Spammer

Kiriyn and Shad0w, Play on words of Chearful Ninja, this is a Selenium based web parser that aims to set up an account, ping a tempmail service, and then use that email too set up a Mojang account. Then, solve the captcha, and recieve the email, and then post the account details to a textfile.

### Tasks
1. **Set up temp-mail address** Or custom mail webserver (Since I want this to be a dockerfile that can be ported anywhere, tempmail is probably more desiarable)
1. **Fill out Mojang Forms** This should be as simple as using selenium to fill forms!
1. **Solve Captcha** Mojang uses rampant ReCaptchas around its site, and a microservice to solve them, would be great!
1. **Recieve Email** Continue to parse the email client, and recieves the email and retrieves its code.
1. **Authenticate Account** Authenticate the account, and sign in, both with selenium.
1. **Add Account Details Too Server** Ping a Server with Account Details, once account activated
