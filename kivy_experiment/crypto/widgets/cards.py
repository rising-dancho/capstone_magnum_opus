import json
from threading import Thread
from kivy.app import App
from kivy.lang import Builder

from views.assetview import AssetView
from kivy.uix.behaviors import ButtonBehavior

from kivy.properties import StringProperty,NumericProperty,ListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import LinePlot
from kivy.clock import Clock, mainthread
from kivy.metrics import dp, sp
from kivy.utils import rgba



from pycoingecko import CoinGeckoAPI


Builder.load_string("""

<Asset>:
    size_hint: [None, None]
    width: Window.size[0]*.38
    height: dp(240)
    orientation: "vertical"
    spacing: dp(8)
    padding: dp(6)
    canvas.before:
        Color:
            rgba: app.colors.secondary
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(8)]
    BoxLayout:
        size_hint_y: None
        height: dp(42)
        # canvas.before:
        #     Color:
        #         rgba: rgba("#8B314B")
        #     Rectangle:
        #         pos:self.pos
        #         size: self.size
        AnchorLayout:
            size_hint_x: None
            width: dp(42)
            BoxLayout:
                size_hint: [None,None]
                size: [dp(42), dp(42)]
                padding: dp(4)
                RelativeLayout:
                    AsyncImage:
                        id: proxy
                        source: root.source
                        opacity: 0
                    Widget:
                        canvas.before:
                            Color:
                                rgba: [1,1,1,1]
                            Ellipse:
                                size: self.size[0], self.size[1]
                                pos:  self.pos
                                texture: proxy.texture       
        BoxLayout:
            size_hint_x: .5
            Text:
                text: root.text   
                font_name: app.fonts.heading
                color: app.colors.white 

        BoxLayout:
            size_hint_x: .5
            Text:
                id: price_change
                size_hint_x: None
                width: dp(48)
                font_name: app.fonts.subheading
                halign: "left"
                font_size: sp(10)
                color: app.colors.success
    BoxLayout:
        Graph:
            id: graph
            xmax: len(root.chart_data)
            xmin: 0
            ymax: 7
            ymin: 0.1
            draw_border: False

    BoxLayout:
        size_hint_y: None
        height: dp(42)
        orientation: "vertical"
        Text:
            text: "$%s"%str(root.price)
            font_name: app.fonts.subheading
            color: app.colors.white 
        Text:
            text: "%s owned"%str(root.owned)
            font_name: app.fonts.body
            color: app.colors.tertiary_light


<Watchlist>:
    size_hint_y: None
    height: dp(54)
    padding: dp(8)
    canvas.before:
        Color:
            rgba: app.colors.secondary
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(8)]
        
    BoxLayout:
        size_hint_x: None
        width: self.height # width = height so to make it a perfect square
        padding: dp(4)
        RelativeLayout:
            AsyncImage:
                id: proxy
                source: root.source
                opacity: 0
            Widget:
                canvas.before:
                    Color:
                        rgba: [1,1,1,1]
                    Ellipse:
                        size: self.size[0], self.size[1]
                        pos:  self.pos
                        texture: proxy.texture       

    BoxLayout:
        size_hint_x: .45
        Text:
            text: root.text   
            font_name: app.fonts.subheading
            color: app.colors.white 

    BoxLayout:
        size_hint_x: .45
        Text:
            text: "$%s"%str(root.price)  
            font_name: app.fonts.subheading
            font_size: app.fonts.size.h5
            halign: "right"
            color: app.colors.white 
        Text:
            id: price_change
            size_hint_x: None
            width: dp(48)
            font_name: app.fonts.subheading
            font_size: app.fonts.size.h6
            halign: "right"
            color: app.colors.success   


""")

class Card(ButtonBehavior, BoxLayout):
    source = StringProperty("")
    text = StringProperty("")
    owned = StringProperty("1 BTC")
    price = NumericProperty(0.0)
    price_change = NumericProperty(0.0)

    chart_data = ListProperty([0,.1])
    
    daily_prices = ListProperty([0,.1])
    weekly_prices = ListProperty([0,.1])
    monthly_prices = ListProperty([0,.1])
    yearly_prices = ListProperty([0,.1])

    data = ObjectProperty()
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.cg = CoinGeckoAPI()    
        self.from_view = False
        self.bind(on_release=self.view_asset)

    def on_price_change(self, inst, value):
        new_price = f"+{value}"
        new_price = new_price.replace("+-", "-")[:5] 
        self.ids.price_change.text = new_price + "%"

        if new_price.startswith("-"):
            self.ids.price_change.color = App.get_running_app().colors.danger

    def view_asset(self, *args):
        """
            Required
            ============================
            currency = StringProperty("BTC")
            asset_value = NumericProperty(42342.62)
            source = StringProperty("")
            chart_data = ListProperty([0,1])
            daily_data = ListProperty([0,1])
            weekly_data = ListProperty([0,1])
            monthly_data = ListProperty([0,1])
            yearly_data = ListProperty([0,1])
        """
        if len(self.daily_prices) < 2:
            self.from_view = True
            self.get_data()
        else:
            self.open_view()

    @mainthread
    def open_view(self):
        av = AssetView()
        av.currency = str(self.text)
        av.asset_value = self.price
        av.source = self.source

        av.daily_data = self.daily_prices
        av.weekly_data = self.weekly_prices
        av.monthly_data = self.monthly_prices
        av.yearly_data = self.yearly_prices
        av.data = self.data

        av.open()
        # av.update_graph()
        Clock.schedule_once(lambda x: av.update_graph(), .5)

    def get_data(self):
        # print("DATA: ", data)
        coin_id = self.data['id']
        t1 = Thread(target=self.get_points, args=[coin_id] ,daemon=True)
        t1.start()

    def get_points(self, coin_id):
        daily = self.cg.get_coin_market_chart_by_id(coin_id, vs_currency="usd", days=1)

        points = [x[1] for x in daily['prices'][-60:]]
        self.chart_data = points
        self.daily_prices = [x[1] for x in daily['prices']]

        t1 = Thread(target=self.get_all_points, args=[coin_id], daemon=True)
        t1.start() 

    def get_all_points(self, coin_id):
        weekly = self.cg.get_coin_market_chart_by_id(coin_id, vs_currency="usd", days=7)
        monthly = self.cg.get_coin_market_chart_by_id(coin_id, vs_currency="usd", days=30)
        yearly = self.cg.get_coin_market_chart_by_id(coin_id, vs_currency="usd", days=365)
        
        self.weekly_prices = [x[1] for x in weekly['prices']]
        self.monthly_prices= [x[1] for x in monthly['prices']]
        self.yearly_prices = [x[1] for x in yearly['prices']]

        if self.from_view:
            self.open_view()
            self.from_view = False

          
class Asset(Card):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

        Clock.schedule_once(self.render, .2)
    
    def render(self, _):
        graph = self.ids.graph
        plot = LinePlot()
        plot.line_width = dp(1.2)
        plot.color = App.get_running_app().colors.tertiary_light

        graph.add_plot(plot)
    
    def on_data(self, *args):
        self.get_data()
    
    def on_chart_data(self, inst, prices):
        graph = self.ids.graph
        plots = graph.plots

        if len(plots) == 0:
            return

        points = []
        ymax = 0
        ymin = min(prices)

        for i, p in enumerate(prices): 
            pt = (i+1, p)
            points.append(pt)

            if p > ymax:
                ymax = p
        
        graph.ymax = ymax
        graph.ymin = ymin
        plots[0].points = points
    
class Watchlist(Card):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

   