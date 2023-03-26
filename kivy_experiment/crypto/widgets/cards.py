from kivy.app import App
from kivy.lang import Builder

from kivy.properties import StringProperty,NumericProperty,ListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import LinePlot
from kivy.clock import Clock
from kivy.metrics import dp, sp
from kivy.utils import rgba
import json


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
                size_hint_x: None
                width: dp(48)
                text: "+%s"%str(root.price_change)#[:4]
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
            size_hint_x: None
            width: dp(48)
            text: "+%s"%str(root.price_change)  
            font_name: app.fonts.subheading
            font_size: app.fonts.size.h6
            halign: "right"
            color: app.colors.success   


""")
class Asset(BoxLayout):
    source = StringProperty("")
    text = StringProperty("")
    owned = StringProperty("1 BTC")
    price = NumericProperty(0.0)
    price_change = NumericProperty(0.0)
    chart_data = ListProperty([0,.1])
    data = ObjectProperty()
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .2)
    
    def render(self, _):
        graph = self.ids.graph
        plot = LinePlot()
        plot.line_width = dp(1.2)
        plot.color = App.get_running_app().colors.tertiary_light

        graph.add_plot(plot)
    
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
    
    def on_data(self, inst, data):
        # print("DATA: ", data)
        coin_id = data['id']

    def get_points(self):
        with open("data.json", "r") as f:
            data = json.load(f)

            points = [x[1] for x in data['prices'][-60:]]
            self.chart_data = points

class Watchlist(BoxLayout):
    source = StringProperty("")
    text = StringProperty("")
    price = NumericProperty(0.0)
    price_change = NumericProperty(0.0)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)