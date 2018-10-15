from pyecharts import Map

# attr, value要显示的数值
value = [20, 100,30, 600, 300, 56, 4, 7, 67, 22,12]
attr = ["天河区", "白云区", "越秀区","荔湾区","南沙区","增城区","花都区","从化区","番禺区","海珠区","黄埔区"]

data1 = {'天河区': 20, '白云区': 100, '越秀区': 55, '荔湾区': 800,
        '南沙区': 4, '增城区': 120, '花都区': 90, '从化区': 700,
        '番禺区': 120, '海珠区':350, '黄埔区': 600}
data2 = [('天河区', 20), ('白云区', 100), ('越秀区', 55), ('荔湾区', 800),
        ('南沙区', 4), ('增城区', 120), ('花都区', 90), ('从化区', 700),
        ('番禺区', 120), ('海珠区',350), ('黄埔区', 600)]

# 图框的基本特性
m = Map('广州地图啦啦啦啦',title_color="#fff", title_text_size=15, width=1200, height=600, background_color='#404a59')

# 添加数据到图框中
#attr, value = m.cast(data)
# m.add('', attr, value, maptype=u'广州', visual_range=[0, 100], is_visualmap=True, visual_text_color='#000')
m.add("", attr, value, maptype=u'广州', visual_range=[0, 200], visual_text_color="#fff",
      symbol_size=15, is_visualmap=True)
# show_config() 打印输出图表的所有配置项
# m.show_config()

# render() 生成 .html 文件
m.render()
