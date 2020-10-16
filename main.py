import velocity_graph_saline
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    velocity_graph_saline.saline_graph()
    velocity_graph_saline.u50_graph()
    velocity_graph_saline.pre_treat_nalt_graph()
    # velocity_graph_saline.show_All()



    # plt2.plot(velocity_graph_saline.all_info_df['Saline Time'][:2600*30].values, velocity_graph_saline.all_info_df['Saline Rolling'][:2600*30].values, label='saline')
    # plt2.plot(velocity_graph_saline.all_info_df['U50 Velocity Time'][:2600*60].values, velocity_graph_saline.all_info_df['U50 Rolling'][:2600*60].values, label='u50')
    # plt2.plot(velocity_graph_saline.all_info_df['Nalt Time'][:2600*30].values, velocity_graph_saline.all_info_df['Nalt Rolling'][:2600*30], label='nalt')
    # plt2.xlabel('time (seconds)')
    # plt2.ylabel('velocity (pixels/second)')
    # plt2.title("combined rolling velocity graphs")
    # plt2.legend()
    # # plt2.show()
    plt3.plot(velocity_graph_saline.all_info_df['Saline Time'][:2600*30], velocity_graph_saline.all_info_df['Saline_cumsum'][:2600*30], label='saline cummulative sum')
    plt3.plot(velocity_graph_saline.all_info_df['U50 Velocity Time'][:2600*60], velocity_graph_saline.all_info_df['U50_cumsum'][:2600*60], label='u50 cummmulative sum')
    plt3.plot(velocity_graph_saline.all_info_df['Nalt Time'][:2600*30], velocity_graph_saline.all_info_df['nalt_cumsum'][:2600*30], label='nalt cummulative sum')
    plt3.xlabel('time (seconds)')
    plt3.ylabel('distance travelled (pixels)')
    plt3.title("combined cummulative distance")
    plt3.legend()
    plt3.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
