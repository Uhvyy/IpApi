import aiohttp


class IpApi:
    """
    IpApi is a simple module for obtaining information about an IP address by using IP-API.
    """
    def __init__(self):
        self.url = 'http://ip-api.com/json/{}?fields=17002201&lang=ru'

    async def check_connection(self, ip: str) -> bool:
        """
        Check connection
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url.format(ip)) as response:
                data = await response.json()
                if not data['status']:
                    raise CreateRequestError(data['message'])
                else:
                    return True

    async def get_all_info(self, ip: str) -> dict:
        """
        Get all information about ip address
        """
        if await self.check_connection(ip):
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url.format(ip)) as response:
                    data = await response.json()
                    return data

    async def is_hosting(self, ip: str) -> bool:
        """
        Returns boolean value if the ip belongs to the hosting
        """
        if await self.check_connection(ip):
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url.format(ip)) as response:
                    data = await response.json()
                    return data['hosting']

    async def is_proxy(self, ip: str) -> bool:
        """
        Returns boolean value if the ip belongs to the proxy
        """
        if await self.check_connection(ip):
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url.format(ip)) as response:
                    data = await response.json()
                    return data['proxy']
    
    async def is_mobile(self, ip: str) -> bool:
        """
        Returns boolean value if the ip belongs to the mobile
        """
        if await self.check_connection(ip):
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url.format(ip)) as response:
                    data = await response.json()
                    return data['mobile']


class CreateRequestError(Exception):
    pass
