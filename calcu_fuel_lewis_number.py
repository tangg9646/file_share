
import tkinter as tk
# from tkinter import messagebox  # import this to fix messagebox error
# import pickle

window = tk.Tk()
window.title('氢氨流量计算')
window.geometry('600x500')


tk.Label(window, text='当量比（fuel:air）').place(x=10, y= 10)
var_equivalent = tk.StringVar()
var_equivalent.set('1.0')
entry_equivalent = tk.Entry(window, textvariable=var_equivalent, width=12)
entry_equivalent.place(x=10+5, y=30+5)

tk.Label(window, text='燃料H2比例（%）').place(x=200, y= 10)
var_h2_percent = tk.StringVar()
var_h2_percent.set('20')
entry_h2_percent = tk.Entry(window, textvariable=var_h2_percent, width=12)
entry_h2_percent.place(x=200+5, y=30+5)

tk.Label(window, text='燃料Lewis数 (0.29~0.685)').place(x=200, y= 75)
var_lewis_number = tk.StringVar()
var_lewis_number.set('0.606')
entry_lewis_number = tk.Entry(window, textvariable=var_lewis_number, width=12)
entry_lewis_number.place(x=200+5, y=95+5)




position_flow_x = 10
position_flow_y = 180
position_flow_Label_to_Entry_y = 25
position_flow_Label_to_Entry_x = 5
position_flow_next_gas_derta = 60

tk.Label(window, text='空气流量（ml/min）').place(x=position_flow_x, y= position_flow_y)
var_air_flow = tk.StringVar()
var_air_flow.set('2000')
entry_air_flow = tk.Entry(window, textvariable=var_air_flow, width=12, background='#F1F1B8')
entry_air_flow.place(x=position_flow_x + position_flow_Label_to_Entry_x, \
                     y=position_flow_y+position_flow_Label_to_Entry_y)



tk.Label(window, text='NH3流量（ml/min）').place(x=position_flow_x, \
                                             y= position_flow_y+position_flow_next_gas_derta)
var_nh3_flow = tk.StringVar()
var_nh3_flow.set('305.45')
entry_nh3_flow = tk.Entry(window, textvariable=var_nh3_flow, width=12, background='#F1F1B8')
entry_nh3_flow.place(x=position_flow_x+position_flow_Label_to_Entry_x, \
                     y=position_flow_y+position_flow_next_gas_derta+position_flow_Label_to_Entry_y)



tk.Label(window, text='H2流量（ml/min）').place(x=position_flow_x, \
                                            y= position_flow_y + 2*position_flow_next_gas_derta)
var_h2_flow = tk.StringVar()
var_h2_flow.set('76.36')
entry_h2_flow = tk.Entry(window, textvariable=var_h2_flow, width=12, background='#F1F1B8')
entry_h2_flow.place(x=position_flow_x+position_flow_Label_to_Entry_x, \
                    y=position_flow_y + 2*position_flow_next_gas_derta+position_flow_Label_to_Entry_y)



tk.Label(window, text='总流量（ml/min）').place(x=200, y= 180)
var_all_flow = tk.StringVar()
var_all_flow.set('2381.82')
entry_all_flow = tk.Entry(window, textvariable=var_all_flow, width=12, background='#88FFFF')
entry_all_flow.place(x=200, y=180+25)

tk.Label(window, text='平均流速（cm/s）').place(x=200, y= 240)
var_flow_speed = tk.StringVar()
var_flow_speed.set('28.15')
entry_flow_speed = tk.Entry(window, textvariable=var_flow_speed, width=12, background='#88FFFF')
entry_flow_speed.place(x=200, y=240+25)


#计算方式选择
select_loc_x = 380
select_loc_y = 50
y_derta = 30

tk.Label(window, text='求解方式选择', font=('Times news', 15), bg='#CCCCCC', padx=10, pady=10).place(x=select_loc_x, y= select_loc_y-40)
var_selected = tk.StringVar()

r1 = tk.Radiobutton(window, text='给定 当量比、H2占比、Air流量',
                    variable=var_selected, value='1')
r1.place(x=select_loc_x, y=select_loc_y)

r2 = tk.Radiobutton(window, text='给定 当量比、H2占比、NH3流量',
                    variable=var_selected, value='2')
r2.place(x=select_loc_x, y=select_loc_y + y_derta)

r3 = tk.Radiobutton(window, text='给定 当量比、H2占比、H2流量',
                    variable=var_selected, value='3')
r3.place(x=select_loc_x, y=select_loc_y + y_derta*2)

r4 = tk.Radiobutton(window, text='给定 当量比、H2占比、总流量',
                    variable=var_selected, value='4')
r4.place(x=select_loc_x, y=select_loc_y + y_derta*3)

r5 = tk.Radiobutton(window, text='给定 当量比、H2占比、气体流速',
                    variable=var_selected, value='5')
r5.place(x=select_loc_x, y=select_loc_y + y_derta*4)

###########################################

r6 = tk.Radiobutton(window, text='给定 当量比、lewis数、Air流量',
                    variable=var_selected, value='11')
r6.place(x=select_loc_x, y=select_loc_y + y_derta*6)

r7 = tk.Radiobutton(window, text='给定 当量比、lewis数、NH3流量',
                    variable=var_selected, value='22')
r7.place(x=select_loc_x, y=select_loc_y + y_derta*7)

r8 = tk.Radiobutton(window, text='给定 当量比、lewis数、H2流量',
                    variable=var_selected, value='33')
r8.place(x=select_loc_x, y=select_loc_y + y_derta*8)

r9 = tk.Radiobutton(window, text='给定 当量比、lewis数、总流量',
                    variable=var_selected, value='44')
r9.place(x=select_loc_x, y=select_loc_y + y_derta*9)

r10 = tk.Radiobutton(window, text='给定 当量比、lewis数、气体流速',
                    variable=var_selected, value='55')
r10.place(x=select_loc_x, y=select_loc_y + y_derta*10)






def get_input():
    if entry_equivalent.get() == '':
        equivalent = None
    else:
        equivalent = float(entry_equivalent.get())

    if entry_h2_percent.get() == '':
        h2_percent = None
    else:
        h2_percent = float(entry_h2_percent.get())

    if entry_lewis_number.get() == '':
        lewis_number = None
    else:
        lewis_number = float(entry_lewis_number.get())

    if entry_air_flow.get() == '':
        air_flow = None
    else:
        air_flow = float(entry_air_flow.get())

    if entry_nh3_flow.get() == '':
        nh3_flow = None
    else:
        nh3_flow = float(entry_nh3_flow.get())

    if entry_h2_flow.get() == '':
        h2_flow = None
    else:
        h2_flow = float(entry_h2_flow.get())

    if entry_all_flow.get() == '':
        all_flow = None
    else:
        all_flow = float(entry_all_flow.get())

    if entry_flow_speed.get() == '':
        flow_speed = None
    else:
        flow_speed = float(entry_flow_speed.get())

    return equivalent, h2_percent, lewis_number, air_flow, nh3_flow, h2_flow, all_flow, flow_speed


def display_result(equivalent, h2_percent, lewis_number, air_flow, nh3_flow, h2_flow, all_flow, flow_speed):
    equivalent = round(equivalent, 2)
    h2_percent = round(h2_percent, 2)
    lewis_number = round(lewis_number, 4)
    air_flow = round(air_flow, 2)
    nh3_flow = round(nh3_flow, 2)
    h2_flow = round(h2_flow, 2)
    all_flow = round(all_flow, 2)
    flow_speed = round(flow_speed, 2)

    var_equivalent.set(str(equivalent))
    var_h2_percent.set(str(h2_percent))
    var_lewis_number.set(str(lewis_number))
    var_air_flow.set(str(air_flow))
    var_nh3_flow.set(str(nh3_flow))
    var_h2_flow.set(str(h2_flow))
    var_all_flow.set(str(all_flow))
    var_flow_speed.set(str(flow_speed))

def cal_lewis_number(h2_percent):
    """
    输入参数：
    :param h2_percent: h2含量
    :return: 混合燃料的lewis数
    """
    nh3_percent = 100.0 - h2_percent
    h2_lewis = 0.29
    nh3_lewis = 0.685
    return h2_percent/100.0*h2_lewis + nh3_percent/100.0*nh3_lewis

def cal_h2_percent(lewis_number):
    """
    根据混合燃料的lewis数计算h2的百分含量
    :param lewis_number: 混合燃料的lewis数
    :return: h2的百分含量
    """
    h2_lewis = 0.29
    nh3_lewis = 0.685
    h2_percent = (100.0 * nh3_lewis - 100.0 * lewis_number) / (nh3_lewis - h2_lewis)

    return h2_percent

def cal_mix_ratio(h2_percent):
    """
    根据h2含量，计算nh3  h2混合比
    :param h2_percent:
    :return:
    """
    # 混合比定义为nh3含量比上h2含量
    nh3_percent = 100.0 - h2_percent
    mix_ratio = nh3_percent / h2_percent
    return mix_ratio

def calcu():
    cal_method = int(var_selected.get())
    equivalent, h2_percent, lewis_number, air_flow, nh3_flow, h2_flow, all_flow, flow_speed = get_input()

    mix_ratio = cal_mix_ratio(h2_percent)

    circular_area = 3.141592653 * (1.34 / 2)**2
    concentrate_o2 = 0.21


    if cal_method == 1 or cal_method == 11:
        # 给定当量比、h2含量、空气流量
        if cal_method == 1:
            h2_flow = (air_flow * concentrate_o2) / ((5*mix_ratio+2)/(4*equivalent))
            nh3_flow = mix_ratio * h2_flow
            all_flow = air_flow + h2_flow + nh3_flow
            flow_speed = all_flow /60.0 / circular_area
            lewis_number = cal_lewis_number(h2_percent)
        else:
            h2_percent = cal_h2_percent(lewis_number)
            mix_ratio = cal_mix_ratio(h2_percent)
            h2_flow = (air_flow * concentrate_o2) / ((5 * mix_ratio + 2) / (4 * equivalent))
            nh3_flow = mix_ratio * h2_flow
            all_flow = air_flow + h2_flow + nh3_flow
            flow_speed = all_flow / 60.0 / circular_area


    elif cal_method == 2 or cal_method == 22:
        # 给定当量比、h2占比、NH3流量大小
        if cal_method == 2:
            h2_flow = nh3_flow / mix_ratio
            air_flow = (((5*mix_ratio+2) / (4*equivalent*mix_ratio)) * nh3_flow) / concentrate_o2
            all_flow = air_flow + h2_flow + nh3_flow
            flow_speed = all_flow / 60.0 / circular_area
            lewis_number = cal_lewis_number(h2_percent)
        else:
            h2_percent = cal_h2_percent(lewis_number)
            mix_ratio = cal_mix_ratio(h2_percent)
            h2_flow = nh3_flow / mix_ratio
            air_flow = (((5 * mix_ratio + 2) / (4 * equivalent * mix_ratio)) * nh3_flow) / concentrate_o2
            all_flow = air_flow + h2_flow + nh3_flow
            flow_speed = all_flow / 60.0 / circular_area

    elif cal_method == 3 or cal_method == 33:
        # 给定当量比、h2占比、H2流量
        if cal_method == 3:
            nh3_flow = mix_ratio * h2_flow
            air_flow = h2_flow * ((5*mix_ratio+2)/(4*equivalent)) / concentrate_o2
            all_flow = air_flow + h2_flow + nh3_flow
            flow_speed = all_flow / 60.0 / circular_area
            lewis_number = cal_lewis_number(h2_percent)
        else:
            h2_percent = cal_h2_percent(lewis_number)
            mix_ratio = cal_mix_ratio(h2_percent)
            nh3_flow = mix_ratio * h2_flow
            air_flow = h2_flow * ((5 * mix_ratio + 2) / (4 * equivalent)) / concentrate_o2
            all_flow = air_flow + h2_flow + nh3_flow
            flow_speed = all_flow / 60.0 / circular_area


    elif cal_method == 4 or cal_method == 44:
        # 给定当量比、h2占比、总流量
        if cal_method == 4:
            h2_flow = all_flow / (1 + mix_ratio + (((5*mix_ratio+2)/(4*equivalent)) / concentrate_o2))
            nh3_flow = mix_ratio * h2_flow
            air_flow = ((5*mix_ratio+2)/(4*equivalent)) / concentrate_o2 * h2_flow
            flow_speed = all_flow / 60.0 / circular_area
            lewis_number = cal_lewis_number(h2_percent)
        else:
            h2_percent = cal_h2_percent(lewis_number)
            mix_ratio = cal_mix_ratio(h2_percent)
            h2_flow = all_flow / (1 + mix_ratio + (((5 * mix_ratio + 2) / (4 * equivalent)) / concentrate_o2))
            nh3_flow = mix_ratio * h2_flow
            air_flow = ((5 * mix_ratio + 2) / (4 * equivalent)) / concentrate_o2 * h2_flow
            flow_speed = all_flow / 60.0 / circular_area

    elif cal_method == 5 or cal_method == 55:
        # 给定当量比、h2占比、气体流速
        if cal_method == 5:
            all_flow = 60 * circular_area * flow_speed
            h2_flow = all_flow / (1 + mix_ratio + ((5 * mix_ratio + 2) / (4 * equivalent)) / concentrate_o2)
            nh3_flow = mix_ratio * h2_flow
            air_flow = ((5 * mix_ratio + 2) / (4 * equivalent)) / concentrate_o2 * h2_flow
            lewis_number = cal_lewis_number(h2_percent)
        else:
            h2_percent = cal_h2_percent(lewis_number)
            mix_ratio = cal_mix_ratio(h2_percent)
            all_flow = 60 * circular_area * flow_speed
            h2_flow = all_flow / (1 + mix_ratio + ((5 * mix_ratio + 2) / (4 * equivalent)) / concentrate_o2)
            nh3_flow = mix_ratio * h2_flow
            air_flow = ((5 * mix_ratio + 2) / (4 * equivalent)) / concentrate_o2 * h2_flow

    display_result(equivalent, h2_percent, lewis_number, air_flow, nh3_flow, h2_flow, all_flow, flow_speed)

    print(equivalent, h2_percent, lewis_number, air_flow, nh3_flow, h2_flow, all_flow, flow_speed)
    print(var_selected.get())



btn_calcu = tk.Button(window, text='计算', command=calcu, padx=5, pady=5, background='gray', font=('Times news',20))
btn_calcu.place(x=select_loc_x+30, y=420)




window.mainloop()