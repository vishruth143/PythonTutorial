import requests

res = requests.get('https://api-qat.onintranet.com/metrics/linegraph?folderName=SYS1-DATAPROVISION-DAILYPULL',
                   verify=False)
if res.status_code == 200:
    print('Success.')
else:
    raise ("Unable to connect to STT LINEGRAPH API URL. Getting the following error: " + res.text)