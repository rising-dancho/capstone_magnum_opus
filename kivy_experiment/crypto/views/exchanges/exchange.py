from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.clock import Clock, mainthread
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivy.properties import ColorProperty, ObjectProperty, BooleanProperty, ListProperty, StringProperty, NumericProperty

from pycoingecko import CoinGeckoAPI
from threading import Thread

from widgets.cards import Watchlist, Asset

Builder.load_file('views/exchanges/exchange.kv')
class Exchange(BoxLayout):
    coins = ListProperty([])
    popular = ListProperty(['btc', 'eth', 'doge', 'ltc', 'dash', 'shib'])
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.cg = CoinGeckoAPI()

        Clock.schedule_once(self.render, .2)

    def render(self, _):
        exchanges = [
            {
                "id": "35235",
                "title": "KRAKEN",
                "source": "assets/imgs/kraken.png",
                "connected": True,
                "keys": {
                    "key": "/sk12162sZfc6L7kohoUg7dpPOQfV88ejSwNUpLHvi2UhaX4HwmzT0BX",
                    "secret": "ejLSo7/JmSeBeBW5y33vxJC7QoK/o7yJyYyl9eHyXONJn45Wt/Q639xboW399BJiWf2eiefFuEqQ0qOZ8Pi/mQ=="
                }
            },
            {
                "id": "35215",
                "title": "OKCOIN",
                "source": "assets/imgs/okcoin.png",
                "connected": True,
                "keys": {
                    "key": "2b8248a6-3dfb-4f40-b44f-cfa32f18e195",
                    "secret": "66072F864FC529751ED9A0BA9049067E",
                    "passphrase": "#hash537/OK"
                }
            },
        ]

        grid = self.ids.gl_connected
        exc = self.ids.gl_exchanges
        grid.clear_widgets()
        exc.clear_widgets()

        for e in exchanges:
            ex = ConnectedExchange()
            ex.title = e['title']
            ex.source = e['source']
            ex.connected = e['connected']
            ex.keys = e['keys']

            grid.add_widget(ex)

            ev = ExchangeTile()
            ev.title = e['title']
            ev.source = e['source']
            ev.connected = e['connected']
            ev.keys = e['keys']

            exc.add_widget(ev)

    @mainthread
    def on_coins(self, inst, mkts):
        return
        grid = self.ids.gl_currencies
        popular = self.ids.gl_popular
        popular.clear_widgets()
        grid.clear_widgets()

        for v in mkts:
            a = ListTile()
            a.text = str(v['symbol']).upper()
            a.source = v['image']
            a.price = v['current_price']
            a.price_change = v['market_cap_change_percentage_24h']
            a.data = v
            grid.add_widget(a)

        for v in mkts:
            if str(v['symbol']) in self.popular:
                a = Asset()
                a.text = str(v['symbol']).upper()
                a.source = v['image']
                a.price = round(v['current_price'], 2)
                a.price_change = v['market_cap_change_percentage_24h']
                a.data = v
                a.height = Window.height*.2
                popular.add_widget(a)

class BaseExchange(BoxLayout):
    title = StringProperty("")
    source = StringProperty("")
    connected = BooleanProperty(False)
    keys = ObjectProperty(allownone=True)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

class ConnectedExchange(BaseExchange):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

class ExchangeTile(BaseExchange):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)