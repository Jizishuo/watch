from pyecharts import Map

# attr, value要显示的数值
value = [20, 100]
attr = ['余杭区', '萧山区']

# 图框的基本特性
m = Map('杭州地图示例图', width=600, height=400)

# 添加数据到图框中
m.add('', attr, value, maptype=u'杭州', visual_range=[0, 100], is_visualmap=True, visual_text_color='#000')

# show_config() 打印输出图表的所有配置项
m.show_config()

# render() 生成 .html 文件
m.render()