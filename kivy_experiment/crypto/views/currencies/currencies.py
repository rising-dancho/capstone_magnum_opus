
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.clock import Clock, mainthread
from kivy.core.window import Window

from pycoingecko import CoinGeckoAPI
from threading import Thread

from widgets.cards import Watchlist, Asset
from kivy.properties import ListProperty


Builder.load_file('views/currencies/currencies.kv')
class Currency(BoxLayout):
    coins = ListProperty([])
    popular = ListProperty(['btc','eth','sol','bnb','avax','xmr'])

    def __init__(self, **kw) -> None:
        super().__init__(**kw)

        self.cg = CoinGeckoAPI()
        Clock.schedule_once(self.render, .2)

    def render(self, _):
        t1 = Thread(target=self.get_coins, daemon = True)
        t1.start()

    def get_coins(self):
        mkts =  self.cg.get_coins_markets(vs_currency="usd", per_page=100)
        self.coins = mkts

    @mainthread    
    def on_coins(self, inst, mkts):
        grid = self.ids.gl_currencies 
        popular = self.ids.gl_popular 
        popular.clear_widgets()
        grid.clear_widgets()

        for v in mkts:
            a = Watchlist()
            a.text = str(v['symbol']).upper()
            a.source = v['image'] # passing crypto coin images from here
            a.price = v['current_price']
            a.price_change = v['market_cap_change_percentage_24h']
            a.data = v
            grid.add_widget(a)

        for v in mkts:
            if str(v['symbol']) in self.popular:
                a = Asset()
                a.text = str(v['symbol']).upper()
                a.source = v['image'] # passing crypto coin images from here
                a.price = round(v['current_price'], 2) 
                a.price_change = v['market_cap_change_percentage_24h']
                a.data = v
                a.height = Window.height*.2
                popular.add_widget(a)
