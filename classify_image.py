from pathlib import Path
import pandas as pd
import os
import datetime
import shutil


def get_csv_file_path():
    """
    取得csv文件的绝对路径+文件全称
    """
    filename = ""
    basepath = Path('C:/H2-NH3_Experiment/image_process/CSV')
    for entry in basepath.iterdir():
        if entry.is_file():
            filename = entry.name
    csv_file = 'C:/H2-NH3_Experiment/image_process/CSV/' + filename

    return csv_file


def get_csv_df():
    """
    获取csv文件，读取为Dataframe文件
    """
    csv_df = pd.read_csv(get_csv_file_path(), encoding='gbk')

    return csv_df


def convert_strtime_to_datetime(csv_df):
    """
    将DF中首列中的 time 转化为 datetime格式，保存在列表中
    """
    time_list = []
    for time in csv_df.iloc[:, 0]:
        csv_datetime = datetime.datetime.strptime(time, "%Y-%m-%d---%H-%M-%S")
        time_list.append(csv_datetime)

    return time_list


def get_files_name():
    """
    获取指定目录下所有文件的名称
    """
    files_name = []

    basepath = Path("C:/H2-NH3_Experiment/image_process/Raw_images/")
    files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
    for item in files_in_basepath:
        files_name.append(item.name)

    return files_name


def get_file_timestape(file_path):
    """
    获得指定的单个文件的时间戳
    """
    file_path = Path(file_path)
    info = file_path.stat()

    return info.st_mtime


def timestamp2datetime(timestamp, convert_to_local=True, utc=8, is_remove_ms=True):
    """
    转换 UNIX 时间戳为 datetime对象
    :param timestamp: 时间戳
    :param convert_to_local: 是否转为本地时间
    :param utc: 时区信息，中国为utc+8
    :param is_remove_ms: 是否去除毫秒
    :return: datetime 对象
    """
    if is_remove_ms:
        timestamp = int(timestamp)
    dt = datetime.datetime.utcfromtimestamp(timestamp)
    if convert_to_local:
        dt = dt + datetime.timedelta(hours=utc)

    return dt


def get_df_index(file_date_time, time_list):
    """根据datetime，查询出当前这个文件应该属于什么参数下的实验"""
    row_index = 0
    for time in time_list:
        if file_date_time < time:
            return row_index - 1
        else:
            row_index += 1

        if row_index == len(time_list):
            return len(time_list) - 1



def mkdir(path):
    """
    在指定位置创建文件夹，用于放置 .csv文件
    :param path:
    :return:
    """
    folder = os.path.exists(path)
    if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
        print("已成功创建文件夹")
    else:
        print("本身已经存在该文件夹")

def creat_file_dir(row_index, csv_df, dst_basepath):
    """
    根据row_index 和 csv文件，确定应该新建的文件夹的名字
    """
    # basepath = "C:/H2-NH3_Experiment/image_process/Classified/"
    # foldername = csv_df.loc[row_index, "总流量"] + "-" + csv_df.loc[row_index, "H2占比"] + "-" + csv_df.loc[row_index, "当量比"] + "/"
    foldername = str(csv_df.loc[row_index, "总流量"]) + "-" + \
                 str(csv_df.loc[row_index, "H2占比"]) + "-" + str(csv_df.loc[row_index, "当量比"]) + "/"
    # path = basepath + foldername
    path = dst_basepath + foldername

    mkdir(path)

    return path

def source_to_destination(src, dst):
    """
    将当前文件，移动至创建的文件夹内
    """
    if src == None:
        return None
    else:
        shutil.copy2(src, dst)


def process_image():
    """
    处理图片，分类至指定名字文件夹
    :return:
    """

    mkdir("C:/H2-NH3_Experiment/image_process/Raw_images/")
    mkdir("C:/H2-NH3_Experiment/image_process/Classified/")
    mkdir("C:/H2-NH3_Experiment/image_process/CSV/")

    src_basepath = "C:/H2-NH3_Experiment/image_process/Raw_images/"
    dst_basepath = "C:/H2-NH3_Experiment/image_process/Classified/"

    csv_df = get_csv_df()
    time_list = convert_strtime_to_datetime(csv_df)
    files_name = get_files_name()

    for file_name in files_name:
        # 获得单张图片文件的绝对路径
        file_src_path = src_basepath + file_name
        print("文件的绝对路径：" + file_src_path)

        # 获得单张文件的datetime类型时间属性
        file_timestape = get_file_timestape(file_src_path)
        file_datetime = timestamp2datetime(file_timestape)
        print("文件修改时间：" + str(file_datetime))

        # 确定该文件应该属于哪一行下的参数
        row_index = get_df_index(file_datetime, time_list)
        print("文件属于的行索引：" + str(row_index))


        file_dst_path = creat_file_dir(row_index, csv_df, dst_basepath)
        print("file_src_path  ", file_src_path)
        print("file_dst_path  ", file_dst_path)

        source_to_destination(file_src_path, file_dst_path)
        print("完成一次for循环\n\n")

process_image()

