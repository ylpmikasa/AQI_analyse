# # //导入柱状图-Bar
# from pyecharts.charts import Bar
# # //设置行名
# columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# # //设置数据
# data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
# data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
# # //设置柱状图的主标题与副标题
# bar = Bar("柱状图", "一年的降水量与蒸发量")
# # //添加柱状图的数据及配置项
# bar.add("降水量", columns, data1, mark_line=["average"], mark_point=["max", "min"])
# bar.add("蒸发量", columns, data2, mark_line=["average"], mark_point=["max", "min"])
# # 生成本地文件（默认为.html文件）
# bar.render()
# -----------------------------------------------------------------------------------------
# from pyecharts.charts import Bar
# from pyecharts import options as opts
# import os
#
# bar = Bar()
# bar.add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
# bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
# bar.set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
# bar.render()
#
# os.system("render.html")
# ---------------------------------------------------------------------------------------------
import pyecharts.options as opts
from pyecharts.charts import Line
import os


x=['星期一','星期二','星期三','星期四','星期五','星期七','星期日']
y1=[100,200,300,None,100,400,300]
y2=[200,300,200,100,200,300,400]
line=(
    Line()
    .add_xaxis(xaxis_data=x)
    .add_yaxis(series_name="y1线",y_axis=y1, is_smooth=True,is_connect_nones=True)
    .add_yaxis(series_name="y2线",y_axis=y2, is_smooth=False)
    .set_global_opts(title_opts=opts.TitleOpts(title="Line-多折线重叠"))
)
line.render()
os.system("render.html")