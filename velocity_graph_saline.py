import os
import pandas as pd
import matplotlib.pyplot as plt

#ideal time in sec
ideal_time = 1000
all_info_df = pd.DataFrame(columns=['Saline Time'])

def saline_graph():
    fps = 30
    csv_file = "Saline C1 Raw Velocity Data.csv"
    raw_csv_df = pd.read_csv(csv_file, skiprows=1, usecols=range(5),names=['Time', 'M1', 'M2', 'M3', 'M4'])
    # print(raw_csv_df.loc[:,'M1':'M4'])

    # #instantanouse velocity
    # plt.plot(raw_csv_df['Time'], raw_csv_df.loc[:,'M1':'M4'])
    # plt.xlabel('time')
    # plt.ylabel('velocity (pixels/second)')
    # plt.title("inst saline velocity")
    # plt.show()

    # #average velocity
    raw_csv_df['Avg inst velocity'] = raw_csv_df.loc[:, ['M1', 'M2', 'M3', 'M4']].mean(axis=1)
    # plt.plot(raw_csv_df['Time'], raw_csv_df['Avg inst velocity'])
    # plt.xlabel('time')
    # plt.ylabel('velocity (pixels/second)')
    # plt.title("avg inst saline velocity")
    # plt.show()

    #saline vel rolling avg 30s
    no_seconds = 30
    rolling_avg_dur = fps*no_seconds
    saline_rolling_vel_avg = raw_csv_df['Avg inst velocity'].rolling(rolling_avg_dur).mean()
    # plt.plot(raw_csv_df['Time'], saline_rolling_vel_avg)
    # plt.xlabel('time')
    # plt.ylabel('velocity (pixels/second)')
    # plt.title("avg inst saline velocity ["+str(no_seconds)+" second rolling avg]")
    # plt.show()

    all_info_df['Saline Rolling'] = saline_rolling_vel_avg
    all_info_df['Saline Time'] = raw_csv_df
    # print(all_info_df)

    all_info_df['Saline Dist'] = all_info_df['Saline Time'] * all_info_df['Saline Rolling']
    all_info_df['Saline_cumsum'] = all_info_df['Saline Dist'].cumsum()

def u50_graph():
    fps = 60
    csv_file_u50 = "5mgkg U50 C1 Raw Velocity Data.csv"
    raw_csv_df_u50 = pd.read_csv(csv_file_u50, skiprows=1, usecols=range(5), names=['Time', 'M1', 'M2', 'M3', 'M4'])
    # print(raw_csv_df_u50.loc[:,'M1':'M4'])

    #instantanouse velocity
    # plt.plot(raw_csv_df_u50['Time'], raw_csv_df_u50.loc[:,'M1':'M4'])
    # plt.xlabel('time')
    # plt.ylabel('velocity (pixels/second)')
    # plt.title("inst u50 velocity")
    # # plt.show()

    #average velocity
    raw_csv_df_u50['Avg inst velocity'] = raw_csv_df_u50.loc[:, ['M1', 'M2', 'M3', 'M4']].mean(axis=1)
    # plt.plot(raw_csv_df_u50['Time'], raw_csv_df_u50['Avg inst velocity'])
    # plt.xlabel('time')
    # plt.ylabel('velocity (pixels/second)')
    # plt.title("avg inst saline velocity")
    # # plt.show()

    #u50 vel rolling avg 30s
    no_seconds = 30
    rolling_avg_dur = fps*no_seconds
    u50_rolling_vel_avg = raw_csv_df_u50['Avg inst velocity'].rolling(rolling_avg_dur).mean()
    plt.plot(raw_csv_df_u50['Time'], u50_rolling_vel_avg)
    plt.xlabel('time')
    plt.ylabel('velocity (pixels/second)')
    plt.title("avg inst u50 velocity ["+str(no_seconds)+" second rolling avg]")
    # plt.show()

    all_info_df['U50 Rolling'] = u50_rolling_vel_avg
    all_info_df['U50 Velocity Time'] = raw_csv_df_u50['Time']

    all_info_df['U50 Dist'] = all_info_df['U50 Velocity Time'] * all_info_df['U50 Rolling']*10
    all_info_df['U50_cumsum'] = all_info_df['U50 Dist'].cumsum()
    print(all_info_df['U50_cumsum'])

def pre_treat_nalt_graph():
    nalt_fps = 60
    csv_file_nalt = "pre_treat_Naltr_3mgkg_u50_5mgkg.csv"
    raw_csv_df_nalt = pd.read_csv(csv_file_nalt, skiprows=1, usecols=range(4), names=['Time','M2', 'M3', 'M4'])
    # raw_csv_df_nalt['Time'] = raw_csv_df_nalt['Time']/2
    #inst velocity
    # plt.plot(raw_csv_df_nalt['Time'], raw_csv_df_nalt.loc[:,'M2':'M4'])
    # plt.xlabel('time')
    # plt.ylabel('velocity (pixels/second)')
    # plt.title("inst pre-treat velocity")
    # plt.show()

    #average velocity
    raw_csv_df_nalt['Avg inst velocity'] = raw_csv_df_nalt.loc[:, ['M2', 'M3', 'M4']].mean(axis=1)
    # plt.plot(raw_csv_df_nalt['Time'], raw_csv_df_nalt['Avg inst velocity'])
    # plt.xlabel('time')
    # plt.ylabel('velocity (pixels/second)')
    # plt.title("avg inst saline velocity")
    # plt.show()

    #pre treat vel rolling avg 30s
    no_seconds = 30
    rolling_avg_dur = nalt_fps*no_seconds
    nalt_rolling_vel_avg = raw_csv_df_nalt['Avg inst velocity'].rolling(rolling_avg_dur).mean()
    # plt.plot(raw_csv_df_nalt['Time'][:(1800*nalt_fps)], nalt_rolling_vel_avg[:(1800*nalt_fps)])
    # plt.plot(raw_csv_df_nalt['Time'], nalt_rolling_vel_avg)
    # plt.xlabel('time')
    # plt.ylabel('velocity (pixels/second)')
    # plt.title("avg nalt velocity ["+str(no_seconds)+" second rolling avg]")
    # plt.show()
    all_info_df['Nalt Rolling'] = nalt_rolling_vel_avg
    all_info_df['Nalt Time'] = raw_csv_df_nalt['Time']


    all_info_df['Nalt Dist'] = all_info_df['Nalt Time'] * raw_csv_df_nalt['Avg inst velocity']
    all_info_df['nalt_cumsum'] = all_info_df['Nalt Dist'].cumsum()
    print(all_info_df['nalt_cumsum'])
