import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.ticker as ticker
# plt.style.use(['science', 'nature', 'notebook'])
class cls_plt_fig():
    def __init__(self, name):
        self.name = name
    def func_plt_fig(self, 
            fig_name='../generate/test.svg',

            x_label=None, # r"$\bf{Conv\ Layers}$",
            x_value=np.array([0,1,2]), 
            xticks_loc=(0, 0),
            xticks= ['Conv1', 'Conv2'],
            border_width = 1,
            
            y_label=[r"$\bf{Speedup}$", r"$\bf{Energy}$"], # 1D
            
            # 3D: [Y_axis][Curve/Vector][Point]
            y_value=[[np.array([2.55, 3.48]),np.array([2.55, 3.48])], [np.array([2.55, 3.48]), np.array([2.55, 3.48])]],
            y_fig_type=[["bar"], ["bar"]],# 2D
            y_legend= [["Speedup"], ["Energy"]], # 2D

            y_color=[[(0,0,0)],[(0,0,0)]], # 2D
            y_yticks_max= [10, None],
            y_yticks_min= [0, None],
            y_axis_color=[(0,0,0), (0,0,0)],

            # plot:
            y_linestyle='-',
            y_marker=[['s', 's'], ['*', '*'], ['o', 'o']],
            y_markersize=10,
            # y_markerfacecolor=[[None]],
            y_markeredgecolor="white",
            y_markeredgewidth=1,
            # bar:
            y_edgecolor = [[None, None],[None, None]],# [[(0,0,0)],[(0,0,0)]],
            y_facecolor = None,# [[(0,0,0)],[(0,0,0)]],
            y_hatch = [[None, None],[None, None]],
            ylim_min = None,

            # global setting
            len_yticks = [10, 5],
            # legend_size= 12,
            # label_size= 12,
            # xticks_fontsize= 12,
            font_size = 13,
            linewidth= 2,
            bar_width = 0.4,
            bar_gap_width = 0.4/4,

            grid_axis= None,
            plt_text= False,
            PercentFormatter = False,
            minor = None,
            labelrotation = None, # 45
            legend_loc= "best",
            legend_ncol=1,
            figsize = (7, 3.733)
            ): # dict
        y_dim = np.shape(y_value)

        if y_dim[0] >2: # multi Y axis using HostAxes method but can't change fontsize
            fig = plt.figure() #定义figure，（1）中的1是什么
            ax = HostAxes(fig, [0.2, 0.2, 0.6, 0.6])  #用[left, bottom, weight, height]的方式定义axes，0 <= l,b,w,h <= 1
        else:
            fig, ax = plt.subplots(figsize=figsize)
        plt.rcParams['hatch.color'] = "white"
        
        ax1 = None
        ax_array = [ax]

        if y_dim[0] > 1:


            if y_dim[0] >2:
                ax.axis['right'].set_visible(False)
                ax.axis['top'].set_visible(False)
                ax1 = ParasiteAxes(ax, sharex=ax)
                ax.parasites.append(ax1)
                ax1.axis['top'].set_visible(False)
                ax1.axis['right'].set_visible(True)
                ax1.axis['right'].major_ticklabels.set_visible(True)
                ax1.axis['right'].label.set_visible(True)
                ax_array.append(ax1)

                ax2 = ParasiteAxes(ax, sharex=ax)
                ax.parasites.append(ax2)
                ax2.axis['top'].set_visible(False)
                load_axisline = ax2.get_grid_helper().new_fixed_axis
                ax2.axis['right2'] = load_axisline(loc='right', axes=ax2, offset=(40,0))
                ax_array.append(ax2)

                fig.add_axes(ax)
            else:
                ax1 = ax.twinx()
                ax_array.append(ax1)

        (handles1, labels1) = ([], [])
        for idx_axis in range(y_dim[0]):
            for idx_vector in range(y_dim[1]):
                if  y_fig_type[idx_axis][idx_vector] == "plot":
                    ax_array[idx_axis].plot(
                            x_value, #+ 0.04/0.5*idx_axis*(x_value-0.7)
                            y_value[idx_axis][idx_vector], 
                            label=y_legend[idx_axis][idx_vector],
                            linewidth=linewidth, 
                            linestyle=y_linestyle[idx_axis][idx_vector], 
                            color=y_color[idx_axis][idx_vector],  
                            marker=y_marker[idx_axis][idx_vector], 
                            markersize=y_markersize if y_marker[idx_axis][idx_vector] !="*" else y_markersize+10, 
                            markeredgecolor = y_markeredgecolor, 
                            markeredgewidth = y_markeredgewidth,
                            zorder=10
                            )
                elif y_fig_type[idx_axis][idx_vector] == "bar":
                    bar_pair = 0
                    if y_fig_type[0][idx_vector] == "bar" and y_dim[0] > 1:
                        if y_fig_type[1][idx_vector] == "bar":
                            bar_pair += 1 # No. of left and right bar pair
                    ax_bar_center_bias =  (bar_width+bar_gap_width)*bar_pair/2

                    x_coordinate =  x_value \
                                +(bar_width +bar_gap_width)*(idx_vector-(y_dim[1]-1)/2) \
                                + (ax_bar_center_bias if idx_axis > 0 else (- ax_bar_center_bias))
                    ax_array[idx_axis].bar(
                            x_coordinate
                            ,y_value[idx_axis][idx_vector], 
                            label=y_legend[idx_axis][idx_vector],
                            linewidth=linewidth,
                            width=bar_width, 
#                             color= y_color[idx_axis][idx_vector]
                            facecolor= y_color[idx_axis][idx_vector], #y_facecolor[idx_axis][idx_vector],
                            edgecolor= y_edgecolor[idx_axis][idx_vector], 
                            hatch = y_hatch[idx_axis][idx_vector] 
                            # zorder=10
                            )
                    if plt_text:
                        for idx_point in range(len(x_coordinate)):
                            ax_array[idx_axis].text(x_coordinate[idx_point]
                            , y_value[idx_axis][idx_vector][idx_point] + (y_yticks_max[idx_axis] - y_yticks_min[idx_axis])*0.07,'%.1f' %y_value[idx_axis][idx_vector][idx_point],va='top', ha='center', fontsize=font_size-1)

            ##################################
            # serial setting

            # xylabel
            if x_label:
                ax.set_xlabel(x_label, fontsize=font_size+2)
            ax_array[idx_axis].set_ylabel(y_label[idx_axis], fontsize=font_size+2, 
            color=y_axis_color[idx_axis]
            )

            # yticks
            ax_array[idx_axis].tick_params(axis='y', which='major',width=1.5, length=6, labelsize = font_size, colors=y_axis_color[idx_axis], direction='out')


            if y_yticks_min and y_yticks_max[idx_axis] and len_yticks:
                ax_array[idx_axis].set_yticks(np.linspace(y_yticks_min[idx_axis], y_yticks_max[idx_axis], len_yticks[idx_axis]+1)) # occupy fully yaxis
                ax_array[idx_axis].set_ylim(y_yticks_min[idx_axis],y_yticks_max[idx_axis])
            # legend
            (handle1, label1)= ax_array[idx_axis].get_legend_handles_labels()
            handles1 += handle1
            labels1  += label1



        ##################################
        # Global setting

        # x ticks
        if ylim_min:
            ax.set_ylim(ylim_min, )  
#         border_width = 1  
        ax.set_xlim(x_value[0]-border_width, x_value[-1]+border_width)
        # ax.set_xlim(x_value[0]-bar_width*2, 22)
        # plt.xticks(xticks, ["0.7", "0.8", "0.9", "1.0", "1.1", "1.2"]) #, "0.7", "0.8", "0.9", "1.0", "1.1", "1.2"
        print(x_value, xticks)
        # plt.xticks(np.append(xticks, 10), np.append(xticks, '10'), fontsize=font_size)# if xticks is not None else x_value)
        # plt.xticks(xticks_loc, xticks, fontsize=font_size)# if xticks is not None else x_value)
        plt.xticks(x_value, xticks, fontsize=font_size)# if xticks is not None else x_value)
        
        # fig.autofmt_xdate(rotation=45)
        # plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
        ax.tick_params(axis='x', which='major',width=1.5, length=6, labelsize = font_size, colors=(0,0,0), direction='out')

        plt.grid(axis=grid_axis, zorder=0) #,

        if y_dim[0] >2 :
            ax_array[0].axis['left'].line.set_color(y_axis_color[0])
            ax_array[0].axis['left'].major_ticks.set_color(y_axis_color[0])
            ax_array[0].axis['left'].major_ticklabels.set_color(y_axis_color[0])
            ax_array[1].axis['right'].line.set_color(y_axis_color[1])
            ax_array[1].axis['right'].major_ticks.set_color(y_axis_color[1])
            ax_array[1].axis['right'].major_ticklabels.set_color(y_axis_color[1])
            ax_array[2].axis['right2'].line.set_color(y_axis_color[2])
            ax_array[2].axis['right2'].major_ticks.set_color(y_axis_color[2])
            ax_array[2].axis['right2'].major_ticklabels.set_color(y_axis_color[2])
        else:
            ax_array[0].spines['left'].set_color(y_axis_color[0])
            ax_array[0].spines['right'].set_visible(False)
            if y_dim[0] ==2:
                ax_array[1].spines['right'].set_color(y_axis_color[1])
                ax_array[1].spines['top'].set_visible(False)
                ax_array[1].spines['left'].set_visible(False)
        for idx_axis in range(y_dim[0]):
            ax_array[idx_axis].spines['left'].set_linewidth(1)
            ax_array[idx_axis].spines['right'].set_linewidth(1)
            ax_array[idx_axis].spines['top'].set_linewidth(1)
            ax_array[idx_axis].spines['bottom'].set_linewidth(1)
            ax_array[idx_axis].spines['bottom'].set_visible(True) # avoid spine overlapping


        ax_array[0].spines['top'].set_visible(False)
        if y_legend:
#             handles1 = [handles1[0]] + [handles1[2]]
#             labels1 = [labels1[0]] + [labels1[2]]
            plt.legend(handles1, labels1, fontsize=font_size, loc=legend_loc, ncol=legend_ncol, 
                       frameon=False, handletextpad=0.2,columnspacing=0.4 ) # handletextpad=0.4,columnspacing=0.8 ) # #, 
        plt.rcParams['hatch.color'] = "white"
        if PercentFormatter == True:
            ax_array[0].yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
            ax_array[1].yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
        if labelrotation:
            ax.tick_params(axis='x', labelrotation = labelrotation)
s
        if minor:
            ax.minorticks_on()
            ax.xaxis.set_tick_params(which='minor', bottom=False)
            ax_array[0].tick_params(axis='y', which='minor',width=1.5, length=3, labelsize = font_size, direction='out')
            yminorLocator = ticker.MultipleLocator(0.5)
            ax.yaxis.set_minor_locator(yminorLocator)
#         plt.rcParams['font.family']='Arial'
        plt.savefig(fig_name, format='svg')
        plt.show()
