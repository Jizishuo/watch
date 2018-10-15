from pyecharts import Pie, configure

'''configure(output_image=True)
attr = ['惠州','东莞','广州','深圳','佛山','江门','珠海']
v1 = [12,22,34,29,16,14,18]

pie = Pie('饼图', background_color="white", title_text_size=25)
pie.add('',attr,v1,is_label_show = True)


#设置radius参数实现圆环图:radius = [x,y]，x是内半径，y是外半径
pie =Pie('圆环图',background_color = 'white',title_pos = 'center')
pie.add('',attr,v1,is_label_show = True,radius=[30, 75],is_legend_show = False)

pie.render()'''


#设置rosetype参数实现南丁格尔图（玫瑰图）：
#rosetype有'radius'和'area'两种模式，其中：
#radius通过半径显示数据的大小，扇区圆心角展现数据的百分比；
#area通过半径显示数据的大小，各扇区圆心角相等。
#另外还可以通过设置center参数调整圆心位置（center = [x,y]，x为横坐标，y为纵坐标）
'''configure(output_image=True)
pie =Pie('玫瑰图',background_color = 'white')
attr = ['惠州','东莞','广州','深圳','佛山','江门','珠海']
v1 = [12,22,34,29,16,14,18]
pie.add('radius',attr,v1,center = [25,50],radius=[30, 75],rosetype='radius')
pie.add('area',attr,v1,center = [75,50],radius=[30, 75],rosetype='area')
pie.render()'''

configure(output_image=True)
pie =Pie('圆环中的玫瑰图',background_color = 'white')
attr = ['惠州','东莞','广州','深圳','佛山','江门','珠海']
v1 = [12,22,34,29,16,14,18]
pie.add( '',attr,v1,radius=[65, 75],center=[50, 50])
pie.add('',attr,v1,radius=[0, 60],center=[50, 50],rosetype='area')
pie.render()