# Twitter Bot + CRON

> This bot was created to feed the twitter
> account of [#AprendizajeLibre] with tweets
> stored in a text file

### Version
1.0.1

### Tech
We use the following libraries:
* [Twython] - Python wrapper for the Twitter API

### Installation
You need *Python2.7*, and *pip* to be previously installed:
```sh
$ pip install twython
```
some times you need sudo privileges to execute

Then you have to clone the repository
```sh
$ git clone [git-repo-url] /path/to/repo
```
And finally you have to ask for a twitter accestoken
1. To use this method, you have to register a cellphone number to the Twitter account that you want to automate.

2. Create a Twitter App, following this steps:

    * Follow this link [twitter developers]
    * Click on "Create New App"
    * Fill the form and accept use terms.
    * Once created, go to the tab "Permissions" and change the permissions to "Read, Write and Access direct messages"
    * And finally go to "Keys and Access Tokens" and click over "Create My Access Token"
![Image of Yaktocat](https://4.bp.blogspot.com/-FAejW_SRvII/VsKL6p0ngEI/AAAAAAAAF3U/xqKC2Ah4K6g/s1600/App%2BTwitter.png)

3. Fill the infotmation 
    ``` python
    # Claves de la aplicacion Twitter
    app_key = "Consumer key"
    app_secret = "Consumer secret"
    oauth_token = "Access token"
    oauth_token_secret = "Access token secret"
    ```
#### Adding excecution to CRON
Execute the following command:
```sh
$ crontab -e
```
The next lines, are an example of [crontab schedule syntax] that executes the bot every 30 minutes from 17 to 22 hours every day.
```sh
*/30 17-22 * * 1-7 /path/to/repo/bot.sh
```


Special thanks to:
-------------
* [PythonDiario]


   [Twython]: <https://pypi.python.org/pypi/twython/>
   [#AprendizajeLibre]: <http://www.aprendizajelibre.org/>
   [twitter developers]: <https://apps.twitter.com/>
   [crontab schedule syntax]: <http://linux.die.net/man/5/crontab>
   [PythonDiario]: <http://www.pythondiario.com/2016/02/enviar-tweets-con-python-y-twython.html>
