# Shad0w + Kiriyn (Sniper)

### SK Sniper

Kiriyn and Shad0w, Play on words of Chearful Ninja, this is a Selenium based web parser that aims to set up an account, ping a tempmail service, and then use that email too set up a Mojang account. Then, solve the captcha, and recieve the email, and then post the account details to a textfile.



# The Methodology of the Sniper

This is a Chearful Ninja esque blocking sniper. It is meant to spam hundreds of Mojang Accounts at the same time, trying to redeem gift codes for the account name, right when it drops on nameMC. It requires NO prior account, and NO token. The way it works, is first you need hundreds of Mojang accounts. This is done with the automated script which creates these accounts. The second part, is actually spamming the accounts, this is done with a spammer script which is much more time intensive.


## Mojang Account Creator

The Mojang account creator uses Temp-Mail to retreive emails, and then fills out the form on Mojang's website to create accounts. It is unfortunatly limited by reCaptcha technology, but in the future, AntiCaptcha or 2Captcha could be used to break this. Unfortunatly Buster will not work, as Google doesn't allow hearing tests when it thinks data is automated.

### Tasks

[x] **Set up temp-mail address** Or custom mail webserver (Since I want this to be a dockerfile that can be ported anywhere, tempmail is probably more desiarable)
[x] **Fill out Mojang Forms** This should be as simple as using selenium to fill forms!
[ ] **Solve Captcha** Mojang uses rampant ReCaptchas around its site, and a microservice to solve them, would be great!
[x] **Recieve Email** Continue to parse the email client, and recieves the email and retrieves its code.
[x] **Authenticate Account** Authenticate the account, and sign in, both with selenium.
[x] **Add Account Details Too Server** Ping a Server with Account Details, once account activated

*Note: The Mojang account creator was finished almost immediatly, and apart from reCaptcha removal, works perfectly if you want, reCaptcha removal can be manually added later!* 

## Spam Bot

### Tasks

## Team

### Shad0w7#0320 - Lead Programmer

Guy that learns 2 million different languages for no reason

### Kiriiiii#3268 - Head of Minecraft

Idea Man and the guy with contacts
