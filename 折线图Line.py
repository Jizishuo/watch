from pyecharts import Line,configure

configure(output_image=True)
line = Line("折线图", background_color="white", title_text_size=25)
attr = ['惠州','东莞','广州','深圳','佛山','江门','珠海']
v1 = [23,45,68,58,32,28,36]
v2 = [12,22,34,29,16,14,18]

line.add('举例数字1', attr, v1, mark_line=['average'], is_label_show=True)
#is_smooth:是否平滑处理，可以看到举例数字2在设了is_smooth = True之后，线条变为平滑曲线。
line.add('举例数字2',attr,v2,is_label_show = True,is_smooth=True)


#is_fill实现面积图:
#area_opacity：填充面积的透明度；area_color：填充面积的颜色；symbol = None:去掉线上的点。
line.add('举例数字1',attr,v1,is_fill = True,area_opacity=0.4)
line.add('举例数字2',attr,v2,is_fill = True,is_smooth=True,area_opacity=0.4)


line.render()