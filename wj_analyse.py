'''
〈温江区重污染站点AQI历史数据分析〉
@version [V1.0.0, 2022-03-25]
@author [杨丽鹏]
'''
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line
import os

# 日数据
date_ype = '日数据'
excel_name = 'wj_day.xlsx'
# 小时数据
# date_ype = '小时数据'
# excel_name = 'wj_hour.xlsx'
# 分钟数据
# date_ype = '分钟数据'
# excel_name = 'wj_minute.xlsx'

# 读取excel
def excel_to_list(excel_name):
    df = pd.read_excel(excel_name, usecols=[0,1,2],
                       names=None)  # 读取项目名称列,不要列名
    df_li = df.values.tolist()
    return df_li

# y轴处理
def y_deal(line, title , y_list):
    line.add_yaxis(series_name=title, y_axis=y_list,
                   # 是否为曲线
                   is_smooth=False,
                   # # 使用markpoint标记点属性，数据类型设置为max会将最大值生成标记点
                   markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='max')]),
                   # 平均值
                   markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_='average')]),
                   # 连接空数据
                   is_connect_nones=True
                   )
    return line

# 将列表转换为图形
def list_to_pycharts(df_li):
    station_list = []
    time_list = []
    aqi_list = []
    y_temp_dict = {}
    y_temp_list = []
    dif_dict = {}
    for i in df_li:
        station_list.append(str(i[0]))
        time_list.append(str(i[1]))
        aqi_list.append(i[2])
        y_temp_dict[str(i[0])+str(i[1])] = i[2]
    # 站点去重
    station_list = set(station_list)
    # 时间去重
    time_list = list(set(time_list))
    # 时间排序
    time_list.sort()
    # 设置时间为x轴
    line = Line().add_xaxis(xaxis_data=time_list)
    # 拼接pycharts模型y轴
    for i in station_list:
        # 拼接临时列表
        for j in time_list:
            y_temp_list.append(y_temp_dict.get(i+j))
        # 拼接y轴
        y_deal(line, i, y_temp_list)
        # 将临时列表保存，做差值运算
        dif_dict[i] = list(y_temp_list)
        # 清空临时y轴列表
        y_temp_list.clear()

    # 差值计算
    for i in list(dif_dict.keys()):
        x = i
        y = dif_dict[i]
        dif_dict.pop(i)
        for m in list(dif_dict.keys()):
            n = dif_dict[m]
            for k in range(0,len(y)):
                # 判断是否为数值
                if str(y[k]).isdigit() and str(n[k]).isdigit():
                    y_temp_list.append(abs(y[k]-n[k]))
                else:
                    y_temp_list.append('-')
            # 拼接y轴
            y_deal(line, x+"-"+m, y_temp_list)
            # 清空临时y轴列表
            y_temp_list.clear()

    # 设置样式
    line.set_global_opts(
        # 设置标题样式
        title_opts=opts.TitleOpts(
        # title="温江区重污染站点AQI历史数据分析"
        # 标题文本使用 \n 换行
        title = '温江区重污染站点AQI历史数据分析',
        subtitle = date_ype,

        # 标题左右位置：pos_left,pos_right，距离图表左侧/右侧距离
        # 值可以是像素值如20，也可以是相对值'20%'，或者'left'、'center'、'right'
        pos_left = '10%',

        # 标题上下位置：pos_top,pos_bottom，距离图表左侧/右侧距离
        # 值可以是像素值、相对值，或者'top'、'middle'、'bottom'
        pos_top = 10,

        # 主副标题间距，默认10
        item_gap = 10,

        # 主副标题文字样式，调用TextStyleOpts方法设置
        # 主要配置项：
        # color,font_style,font_weight,font_family,font_size等
        title_textstyle_opts = (opts.TextStyleOpts(color='black')),
        subtitle_textstyle_opts = (
            opts.TextStyleOpts(
                font_weight='bolder')),

        # 主副标题超链接：title_link/subtitle_link
        # title_link = 'http://www.baidu.com',

        # 跳转方式:title_target/subtitle_target,'blank'(默认)/'self'
        # title_target = 'blank'
        ),

        # 设置图例样式
        legend_opts=opts.LegendOpts(

            # 是否显示图例组件
            is_show=True,

            # 图例位置，配置方法与标题相同
            pos_left='50%',
            pos_top='10',

            # 图例布局朝向：'horizontal'(默认，横排), 'vertical'(竖排)
            orient='horizontal',

            # 对齐方式：`auto`, `left`, `right`
            align='auto',

            # 图例中每项的间隔，默认10
            item_gap=10,

            # 图例宽度和高度，默认为25和14
            item_width=50,
            item_height=20,

            # 项目选择模式，'single'(只能显示一个项目)，'multiple'(默认)，False(关闭选择)
            selected_mode='multiple',

            # 项目处于未选中状态时的颜色，默认'#ccc'
            # inactive_color='blue',

            # 字体样式，设置同标题设置
            # textstyle_opts=opts.TextStyleOpts(color='red', font_size=20),

            # 项目较多时，是否允许滚动翻页
            type_='scroll'
        ),
        datazoom_opts=opts.DataZoomOpts(range_start=0, range_end=80),
        toolbox_opts=opts.ToolboxOpts(
            pos_left='80%',
            pos_top='40',
            feature=opts.global_options.ToolBoxFeatureOpts(
                save_as_image={"show": True, "title": "下载为图片", "type": "png"})
                ),
        ).render()
    os.system("render.html")

if __name__ == '__main__':
    list_to_pycharts(excel_to_list(excel_name))

