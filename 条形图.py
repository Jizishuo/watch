from pyecharts import Bar, configure
configure(output_image=True)
bar = Bar("各城市人口", "虚构的", background_color="white",
          title_text_size = 25, subtitle_text_size = 15)

attr = ['惠州','东莞','广州','深圳','佛山','江门','珠海']
v1 = [23,45,68,58,32,28,36]
v2 = [12,22,34,29,16,14,18]

'''bar.add("举例数字1", attr, v1, is_label_show=True, mark_point= ["min", "max"],
        mark_line_symbolsize= "diamond", xaxis_rotate= 30, xaxis_label_textsize= 15,
        yaxis_label_textsize=15)

bar.add("举例数字2", attr, v2, is_label_show=True, mark_point= ["min", "max"],
        mark_line_symbolsize= "diamond", xaxis_rotate= 30, xaxis_label_textsize= 15,
        yaxis_label_textsize=15)'''


#is_stack 实现数据堆叠:
bar.add('举例数字1',attr,v1,is_stack = True)
bar.add('举例数字2',attr,v2,is_stack = True)

#is_convert实现横向条形图:
bar.add('举例数字1',attr,v1,is_label_show = True,label_pos = 'inside',xaxis_label_textsize = 15,yaxis_label_textsize = 15)
bar.add('举例数字2',attr,v2,is_label_show = True,is_convert = True,label_pos = 'inside',xaxis_label_textsize = 15,yaxis_label_textsize = 15)


#bar.render(path="F:\\python项目\\pyecharts使用示例\\11.jpeg")
bar.render()
