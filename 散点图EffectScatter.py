from pyecharts import EffectScatter, configure

es = EffectScatter("散点图举例", background_color="white",title_text_size = 25)
v1 = [12,22,34,29,16,14,18]
v2 = [23,45,68,58,32,28,36]
#带波浪的散点
es.add("", v1, v2, symbol="pin", effect_scale=5.5,xaxis_min = 10)
#正常 不带波浪的散点
es.add('', v1, v2,effect_scale = 0,xaxis_min = 10)
es.render()