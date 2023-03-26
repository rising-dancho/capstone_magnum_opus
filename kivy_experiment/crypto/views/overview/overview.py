
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.properties import ListProperty, StringProperty, NumericProperty

from kivy.garden.graph import LinePlot

from kivy.clock import Clock, mainthread
from threading import Thread
import json

from widgets.cards import Watchlist, Asset

Builder.load_file('views/overview/overview.kv')
class Overview(BoxLayout):
    
    assets = ListProperty([])
    watchlist = ListProperty([])
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .2) # run render funciton for the next 2 seconds 
    
    def render(self, _):
        t1 = Thread(target=self.get_data, daemon = True)
        t1.start()
    
    @mainthread
    def on_assets(self, inst, value):
        grid = self.ids.gl_assets
        grid.clear_widgets()

        for v in value:
            a = Asset()
            print(a.height)
            a.height = a.height * .65
            print(a.height)
            print(grid.parent.parent.parent.height)
            a.text = str(v['symbol']).upper()
            a.source = v['image']
            a.price = v['current_price']
            a.price_change = v['market_cap_change_percentage_24h']
            grid.add_widget(a)

    @mainthread
    def on_watchlist(self, inst, value):
        grid = self.ids.gl_watchlist
        grid.clear_widgets()

        for v in value:
            a = Watchlist()
            a.text = str(v['symbol']).upper()
            a.source = v['image']
            a.price = v['current_price']
            a.price_change = v['market_cap_change_percentage_24h']
            grid.add_widget(a)

    def get_data(self):
        self.assets = self.get_assets()
        self.watchlist = self.get_watchlist()

    def get_assets(self):
        assets = [
            {
                "symbol": "btc",
                "image": "",
                "current_price": 853.22,
                "market_cap_change_percentage_24h": 76.2
            },
            {
                "symbol": "eth",
                "image": "",
                "current_price": 443.25,
                "market_cap_change_percentage_24h": 57.8
            },
            {
                "symbol": "ltc",
                "image": "",
                "current_price": 275.23,
                "market_cap_change_percentage_24h": 19.4
            },
            {
                "symbol": "enj",
                "image": "",
                "current_price": 835.23,
                "market_cap_change_percentage_24h": 23.5
            },
            {
                "symbol": "dash",
                "image": "",
                "current_price": 632.53,
                "market_cap_change_percentage_24h": 48.6
            },
        ]
        return assets

    def get_watchlist(self):
        assets = [
            {
                "symbol": "btc",
                "image": "",
                "current_price": 853.22,
                "market_cap_change_percentage_24h": 6.26645
            },
            {
                "symbol": "eth",
                "image": "",
                "current_price": 443.25,
                "market_cap_change_percentage_24h": 7.8492
            },
            {
                "symbol": "ltc",
                "image": "",
                "current_price": 275.23,
                "market_cap_change_percentage_24h": 1.492
            },
            {
                "symbol": "enj",
                "image": "",
                "current_price": 835.23,
                "market_cap_change_percentage_24h": 2.50492
            },
            {
                "symbol": "dash",
                "image": "",
                "current_price": 632.53,
                "market_cap_change_percentage_24h": 3.60492
            },
        ]
        return assets

