# webdatacap

webdatacap is a flesk application based on python for getting users data

#### [Github](https://github.com/khashino/webdatacap)
#### [Docker](https://hub.docker.com/r/khashi1377/webdatacap)

## docker
first pull project
```
docker pull khashi1377/webdatacap
```
then just run 
```
docker run -d  --name webdatacap -p 80:80 khashi1377/webdatacap 
```

## Installation

Use the git to clone project.

```git
git clone https://github.com/khashino/webdatacap.git
```

install dependencies.

```pip
pip3 install -r requirements.txt
```
## Usage

#### run
```python
python3 main.py
```
#### then you can check:
```
http://localhost/
http://localhost/download/<anything>
```
by opening http://localhost/ you get this information
```
{"status": "success",
 "country": "Iran",
 "countryCode": "IR",
 "region": "07",
 "regionName": "Ostan-e Tehran",
 "city": "Tehrān",
 "zip": "",
 "lat": 35.7662, "lon": 51.4757, "timezone": "Asia/Tehran",
 "isp": "Iran Cell Service and Communication Company",
 "org": "IRANCELL",
 "as": "AS44244 Iran Cell Service and Communication Company",
 "query": "5.112.35.203",
 "platforn": "android",
 "browser": "chrome",
 "ip_address": "5.112.35.203",
 "timestamp": "2020-04-07 19:18:24.826394",
 "uas": "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-N960F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36" }
```
by open download page its a kind of fake page that ask users to signup and give you name and email and password that user typed
```
{"name" : "khashayar",
"mail" : "khashi.norouzi@yahoo.com",
"Pass" : "password"}
```

#### admin page:
```
http://localhost/admin
```
admin page just will open with private IP


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
