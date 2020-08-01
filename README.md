# Shad0w + Kiriyn (Sniper)

### SK Sniper

Kiriyn and Shad0w, Play on words of Chearful Ninja, this is a Selenium based web parser that aims to set up an account, ping a tempmail service, and then use that email too set up a Mojang account. Then, solve the captcha, and recieve the email, and then post the account details to a textfile.



# The Methodology of the Sniper

This is a Chearful Ninja esque blocking sniper. It is meant to spam hundreds of Mojang Accounts at the same time, trying to redeem gift codes for the account name, right when it drops on nameMC. It requires NO prior account, and NO token. The way it works, is first you need hundreds of Mojang accounts. This is done with the automated script which creates these accounts. The second part, is actually spamming the accounts, this is done with a spammer script which is much more time intensive.

[xinabox Video](https://www.youtube.com/watch?v=dojcW7xYznM)

## Mojang Account Creator

The Mojang account creator uses Temp-Mail to retreive emails, and then fills out the form on Mojang's website to create accounts. It is unfortunatly limited by reCaptcha technology, but in the future, AntiCaptcha or 2Captcha could be used to break this. Unfortunatly Buster will not work, as Google doesn't allow hearing tests when it thinks data is automated.

### Tasks

- [x] **Set up temp-mail address** Or custom mail webserver (Since I want this to be a dockerfile that can be ported anywhere, tempmail is probably more desiarable)
- [x] **Fill out Mojang Forms** This should be as simple as using selenium to fill forms!
- [ ] **Solve Captcha** Mojang uses rampant ReCaptchas around its site, and a microservice to solve them, would be great!
- [x] **Recieve Email** Continue to parse the email client, and recieves the email and retrieves its code.
- [x] **Authenticate Account** Authenticate the account, and sign in, both with selenium.
- [x] **Add Account Details Too Server** Ping a Server with Account Details, once account activated

*Note: The Mojang account creator was finished almost immediatly, and apart from reCaptcha removal, works perfectly if you want, reCaptcha removal can be manually added later!* 

## Spam Bot

The Mojang Spammer will log into different tabs, from list.txt, and open many tabs of reCaptcha, then you load all the accounts by loading all the reCaptchas, and once you are finished, then it is loaded and ready to snipe the name you have specified

### Tasks

- [ ] **NameMC Check Loaded Name** Basically just scrape NameMC for the name
- [ ] **Open many tabs of Mojang.com** Basically just spam the tab open
- [ ] **Fill out Mojang Forms** Go through it and load all of them with info and load the Captcha
- [ ] **Solve Captcha** Mojang uses rampant ReCaptchas around its site, and a microservice to solve them, would be great!
- [ ] **Load Sites** Load all of the websites with the name, and get ready to click the button to authenticate them
- [ ] **Authenticate Account** Right when time comes, go through and click create account really fast
- [ ] **Check if Name taken on NameMC** Check NameMC if the name was taken, or not
- [ ] **Check if Blocked by Self** Check if the name was blocked by self, for each tab which failed, close it

# Team

### Shad0w7#0320 - Lead Programmer

![Shad0w Profile](https://crafatar.com/avatars/a1ad5f17157f44f595b1cd7cddac86a7?size=200&overlay)

Guy that learns 2 million different languages for no reason

### Kiriiiii#3268 - Head of Minecraft

![Kiriyn Profile](https://crafatar.com/avatars/db14003f1f684fef8ca6c10c6efb5a25?size=200&overlay)


Idea Man and the guy with contacts
