# verif-rdvs-pref
![](https://image.flaticon.com/icons/png/128/120/120567.png)![](https://www.herault.gouv.fr/var/ide_site/storage/images/design/dans-l-herault/166055-37-fre-FR/dans-l-Herault.png)
Un bot permettant de vérifier les disponibilités des rdvs sur [le site de la préfecture de l'hérault](http://www.herault.gouv.fr/booking/create/15253/0) et d’émettre des notifications.


# Installation
Requires `Python 3`.
1. Run : 
```bash
pip install -r requirements.txt
```
2. Download the chrome driver corresponding to your chrome version : https://chromedriver.chromium.org/downloads
3. Save the path to the chrome driver in a `chrome_driver.txt` file.

# Configuration
1. Run :
```bash
notify-run register
```

1. Save the endpoint in a `notify_endpoint.txt` file.
2. Open the endpoint with a browser and subscribe for notifications.

# Launch 
Run :
```bash
python  pref.py
```