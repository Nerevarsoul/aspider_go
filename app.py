import asyncio

import uvloop
from aspider import AttrField, TextField, Item, Spider


class GameItem(Item):
    user = TextField(css_select='td.User')


class DragonSpider(Spider):
    start_urls = ['https://www.dragongoserver.net/show_games.php?uid=71438&finished=1']
    headers = {
        'Cookie': 'cookie_handle= guest; cookie_sessioncode=6A76225BDFBAE51A8770B5EAE04327BB92B24C0F6',
    }
    
    async def parse(self, res):
        print(res.__dict__)
        items = await GameItem.get_items(html=res.html)
        print(items)
        for item in items:
            print(item)


if __name__ == '__main__':
    DragonSpider.start()

