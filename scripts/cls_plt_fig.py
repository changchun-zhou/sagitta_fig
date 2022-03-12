import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes
# plt.style.use(['science', 'nature', 'notebook'])
class cls_plt_fig():
    def __init__(self, name):
        self.name = name
    def func_plt_fig(self, 
            fig_name='../generate/test.svg',

            x_label=r"$\bf{Conv\ Layers}$",
            x_value=np.array([0,1,2]), 
            xticks= None,
            
            y_label=[r"$\bf{Speedup}$"], # 1D
            y_value=[[[1, 2, 3]]],# 3D
            y_fig_type=[["bar"]],# 2D
            y_legend= [["Speedup"]], # 2D

            y_color=[[None]], # 2D
            y_yticks_max= [10, None],
            y_yticks_min= [0, None],
            y_axis_color=[(0,0,0), (0,0,0)],

            # plot:
            y_linestyle='-',
            y_marker=[['s', 's'], ['o', 'o'], ['*', '*']],
            y_markersize=10,
            # y_markerfacecolor=[[None]],
            y_markeredgecolor="white",
            y_markeredgewidth=1,
            # bar:
            y_edgecolor = [[None]],
            # y1_facecolor = None
            y_hatch = [[None]],

            # global setting
            len_yticks = None,
            # legend_size= 12,
            # label_size= 12,
            # xticks_fontsize= 12,
            font_size = 12,
            linewidth= 2,
            bar_width = 0.1,
            bar_linewidth = 0.6,

            grid_axis= None,
            plt_text= False,
            legend_loc= "best",
            legend_ncol=1,
            figsize = (7, 4.6)
            ): # dict
        y_dim = np.shape(y_value)

        
        
        if y_dim[0] >2: # multi Y axis using HostAxes method but can't change fontsize
            fig = plt.figure() #定义figure，（1）中的1是什么
            ax = HostAxes(fig, [0, 0, 0.6, 0.6])  #用[left, bottom, weight, height]的方式定义axes，0 <= l,b,w,h <= 1
        else:
            fig, ax = plt.subplots(figsize=figsize)

        bar_gap_width = bar_width/4
        ax1 = None
        ax_array = [ax]
        if y_dim[0] > 1:
            ax.axis['right'].set_visible(False)
            ax.axis['top'].set_visible(False)

            if y_dim[0] >2:
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
                            x_value + 0.6*idx_vector, 
                            y_value[idx_axis][idx_vector], 
                            label=y_legend[idx_axis][idx_vector],
                            # linewidth=linewidth, 
                            linestyle=y_linestyle, 
                            color=y_color[idx_axis][idx_vector],  
                            marker=y_marker[idx_axis][idx_vector], 
                            markersize=y_markersize if y_marker[idx_axis][idx_vector] !="*" else y_markersize+8, 
                            markeredgecolor = y_markeredgecolor, 
                            markeredgewidth = y_markeredgewidth,
                            zorder=10
                            )
                elif y_fig_type[idx_axis][idx_vector] == "bar":
                    bar_pair = 0
                    if y_fig_type[0][idx_vector] == "bar" and y_dim[0] > 1:
                        if y_fig_type[1][idx_vector] == "bar":
                            bar_pair += 1 # No. of left and right bar pair
                    ax_bar_center_bias = 0# (bar_width+bar_gap_width)*bar_pair/2

                    ax_array[idx_axis].bar(
                            x_value 
                                +(bar_width +bar_gap_width)*(idx_vector-(y_dim[1]-1)/2)
                                + (ax_bar_center_bias if idx_axis > 0 else (- ax_bar_center_bias)) \
                            ,y_value[idx_axis][idx_vector], 
                            label=y_legend[idx_axis][idx_vector],
                            linewidth=bar_linewidth,
                            width=bar_width, 
                            facecolor= y_color[idx_axis][idx_vector],
                            edgecolor= y_edgecolor[idx_axis][idx_vector], 
                            # hatch = y_hatch[idx_axis][idx_vector], 
                            zorder=10)

            ##################################
            # serial setting

            # xylabel
            ax.set_xlabel(x_label, fontsize=font_size)
            ax_array[idx_axis].set_ylabel(y_label[idx_axis], fontsize=font_size, 
            color=y_axis_color[idx_axis]
            )

            # yticks
            ax_array[idx_axis].tick_params(axis='y', which='major',width=1.5, length=8, labelsize = font_size+2, colors=y_axis_color[idx_axis], direction='out')
            if y_yticks_min and y_yticks_max[idx_axis] and len_yticks:
                ax_array[idx_axis].set_yticks(np.linspace(y_yticks_min[idx_axis], y_yticks_max[idx_axis], len_yticks+1)) # occupy fully yaxis
                ax_array[idx_axis].set_ylim(y_yticks_min[idx_axis],y_yticks_max[idx_axis])

            # legend
            (handle1, label1)= ax_array[idx_axis].get_legend_handles_labels()
            handles1 += handle1
            labels1  += label1

            # spine
            ax_array[idx_axis].spines['left'].set_linewidth(1)
            ax_array[idx_axis].spines['right'].set_linewidth(1)
            ax_array[idx_axis].spines['top'].set_linewidth(1)
            ax_array[idx_axis].spines['bottom'].set_linewidth(1)

        ##################################
        # Global setting

        # x ticks
        # ax.set_xlim(x_value[0], x_value[-1])    
        # ax.set_xlim(x_value[0]-bar_width*2, x_value[-1]+bar_width*2)
        plt.xticks(xticks,xticks if xticks is not None else x_value)# ["0.7", "0.8", "0.9", "1.0", "1.1", "1.2", "0.7", "0.8", "0.9", "1.0", "1.1", "1.2"])
            # xticks if xticks is not None else x_value)
        ax.tick_params(axis='x', which='major',width=1.5, length=8, labelsize = font_size+2, colors=(0,0,0), direction='out')

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
        elif y_dim[0] ==2:
            ax_array[0].spines['left'].set_color(y_axis_color[0])
            ax_array[1].spines['right'].set_color(y_axis_color[1])


        # handles1 = [handles1[0]] + [handles1[2]] + [handles1[4]]
        # labels1 = [labels1[0]] + [labels1[2]] + [labels1[4]]
        plt.legend(handles1, labels1, fontsize=font_size, loc=legend_loc, ncol=legend_ncol, frameon=False)#, handletextpad=0.1,columnspacing=0.4 )
        plt.savefig(fig_name, format='svg')
        plt.show()
