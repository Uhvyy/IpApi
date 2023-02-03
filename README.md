# IpApi
IpApi is a simple asyncio module for obtaining information about an IP address by using IP-API.

## Installation
```
pip install git+https://github.com/Uhvyy/IpApi
```

## Examples
Get all the information about the IP address
```py
from IpAPI import IpApi 

API = IpApi()
data = await API.get_all_info('1.1.1.1')

print(data)
```

## Methods
`check_connection` - checks connection to api.
`get_all_info` - get all the information about the IP address.
`is_hosting` - returns boolean value if the ip belongs to the hosting.
`is_proxy` - returns boolean value if the ip belongs to the proxy
`is_mobile` - returns boolean value if the ip belongs to the mobile

<sub>If you would like to modify this repository (including its code) in your own project, please be sure to credit!</sub>
