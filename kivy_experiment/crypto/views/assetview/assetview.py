from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.metrics import dp, sp 
from kivy.utils import rgba, QueryDict
from kivy.properties import ColorProperty, ObjectProperty, BooleanProperty, \
ListProperty, StringProperty, NumericProperty

from kivy.garden.graph import LinePlot
from kivy.clock import Clock

Builder.load_file('views/assetview/assetview.kv')
class AssetView (ModalView):
    currency = StringProperty("BTC")
    asset_value = NumericProperty(42342.62)
    source = StringProperty("")
    chart_data = ListProperty([0,1])
    daily_data = ListProperty([0,1])
    weekly_data = ListProperty([0,1])
    monthly_data = ListProperty([0,1])
    yearly_data = ListProperty([0,1])

    data = ObjectProperty(allownone=True)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.render, .2)
    
    def render(self, _):
        # graph = self.ids.asset_graph
        plot = LinePlot()
        plot.line_width = dp(1.2)
        plot.color = App.get_running_app().colors.tertiary_light
        
        self.ids.asset_graph.add_plot(plot)

    def on_data(self, inst, data):
        """
            Expected data:
            ==================================
            print(data.keys())

        """
        self.ids.market_cap.text = str(data['market_cap'])
        self.ids.low.text = str(data['low_24h'])
        self.ids.volume.text = str(data['total_volume'])
        self.ids.high.text = str(data['high_24h'])
        self.ids.circulating_supply.text = str(data['circulating_supply'])
        self.ids.total_supply.text = str(data['total_supply'])

        price_change = str(data['price_change_percentage_24h'])[:4] + "%"
        price_change = price_change.replace("+-", "-")
        self.ids.price_change.text = price_change


    def update_graph(self, data_type="day"):
        if data_type == "hour":
            target= [x for x in self.daily_data[-60:]]#get the hour chart 

        if data_type == "day":
            target= self.daily_data

        elif data_type =="week":
            target= self.weekly_data

        elif data_type =="month":
            target= self.monthly_data

        elif data_type =="year":
            target= self.yearly_data
        
        if len(target) > 4:
            self.chart_data = target

    def on_chart_data(self, inst, prices):
        graph = self.ids.asset_graph
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

