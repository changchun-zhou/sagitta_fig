import numpy as np
from matplotlib import pyplot as plt

# plt.style.use(['science', 'nature', 'notebook'])
class cls_plt_fig():
    def __init__(self, name):
        self.name = name
    def func_plt_fig(self, 
            fig_name='../generate/test.svg',

            x_label=r"$\bf{Conv}$"+' ' +r"$\bf{Layers}$",
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
            y_linestyle=[[None]],
            y_marker=[['s', 's'], ['o', 'o']],
            y_markersize=None,
            # y1_markerfacecolor=
            y_markeredgecolor=[[None]],
            y_markeredgewidth=[[None]],
            # bar:
            y_edgecolor = [[None]],
            # y1_facecolor = None
            y_hatch = [[None]],

            # y2_label=r"$\bf{Energy}$" + ' ' + r"$\bf{efficiency}$"+' ' + r"$\bf{(TOPS/W)}$",
            # y2_value=[1],
            # y2_fig_type= "bar",
            # y2_legend= r"$\bf{Energy}$" + ' ' + r"$\bf{efficiency}$",

            # y2_color=(1, 0, 0),
            # y2_yticks_max= None,
            # y2_yticks_min= None,
            # y2_axis_color=(0,0,0),

            # # plot:
            # y2_linestyle='x-',
            # y2_marker='s',
            # # y2_markerfacecolor=
            # y2_markeredgecolor=None,
            # y2_markeredgewidth=None,
            # # bar:
            # y2_edgecolor = None,
            # # y2_facecolor = None
            # y2_hatch = None,

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
            legend_ncol=None,
            figsize = (7, 4.6)
            ): # dict
        fig, ax = plt.subplots(figsize=figsize)
        y_dim = np.shape(y_value)
        bar_gap_width = bar_width/4
        ax1 = None
        if y_dim[0] > 1:
            ax1 = ax.twinx()
        ax_array = [ax, ax1]
        (handles1, labels1) = ([], [])
        for idx_axis in range(y_dim[0]):
            for idx_vector in range(y_dim[1]):
                if  y_fig_type[idx_axis][idx_vector] == "plot":
                    ax_array[idx_axis].plot(
                            x_value + + 0.6*idx_vector, 
                            y_value[idx_axis][idx_vector], 
                            label=y_legend[idx_axis][idx_vector],
                            # linewidth=linewidth, 
                            # linestyle=y_linestyle[idx_axis][idx_vector], 
                            color=y_color[idx_axis][idx_vector],  
                            marker=y_marker[idx_axis][idx_vector], 
                            # markersize=y_markersize, 
                            # markeredgecolor = y_markeredgecolor[idx_axis][idx_vector], 
                            # markeredgewidth = y_markeredgewidth[idx_axis][idx_vector],
                            zorder=10
                            )
                elif y_fig_type[idx_axis][idx_vector] == "bar":
                    bar_pair = 0
                    if y_fig_type[0][idx_vector] == "bar" and y_dim[0] > 1:
                        if y_fig_type[1][idx_vector] == "bar":
                            bar_pair += 1 # No. of left and right bar pair
                    ax_bar_center_bias = 0#(bar_width+bar_gap_width)*bar_pair/2
                    # print(ax_bar_center_bias)
                    # print(x_value)
                    # print(x_value 
                    #             +(bar_width +bar_gap_width)*(idx_vector-(y_dim[1]-1)/2)
                    #             + (ax_bar_center_bias if idx_axis > 0 else (- ax_bar_center_bias)))
                    # print(y_value[idx_axis][idx_vector])
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
            # Global setting

            # xylabel
            ax.set_xlabel(x_label, size=font_size)
            ax_array[idx_axis].set_ylabel(y_label[idx_axis], size=font_size, 
            color=y_axis_color[idx_axis]
            )

            # ticks
            ax_array[idx_axis].tick_params(axis='y', which='major',width=1.5, length=8, labelsize = font_size+2, colors=y_axis_color[idx_axis])
            if y_yticks_min and y_yticks_max[idx_axis] and len_yticks:
                ax_array[idx_axis].set_yticks(np.linspace(y_yticks_min[idx_axis], y_yticks_max[idx_axis], len_yticks+1)) # occupy fully yaxis
                ax_array[idx_axis].set_ylim(y_yticks_min[idx_axis],y_yticks_max[idx_axis])

            # ax.set_xlim(x_value[0]-bar_width*2, x_value[-1]+bar_width*2)
            plt.xticks(xticks, xticks if xticks is not None else x_value)
            ax_array[0].tick_params(axis='x', which='major',width=1.5, length=8, labelsize = font_size+2, colors=(0,0,0))

            # legend
            (handle1, label1)= ax_array[idx_axis].get_legend_handles_labels()
            handles1 += handle1
            labels1  += label1
            # handles2, labels2 = ax1.get_legend_handles_labels()

            # grid 
            plt.grid(axis=grid_axis, zorder=0) #,
            if y_dim[0] >1 :
                ax_array[0].spines['left'].set_color(y_axis_color[0])
                ax_array[1].spines['right'].set_color(y_axis_color[1])

            ax_array[idx_axis].spines['left'].set_linewidth(1)
            ax_array[idx_axis].spines['bottom'].set_linewidth(1)
            ax_array[idx_axis].spines['top'].set_linewidth(1)
            ax_array[idx_axis].spines['bottom'].set_linewidth(1)

            
            

        plt.legend(handles1, labels1, frameon=False)

        plt.savefig(fig_name, format='svg')
        plt.show()


        # for idx_y in range(len(fig_dict["y1_name"])):
        #     print("idx_y: {}".format(idx_y))
        #     ax_bar_center_bias = 0 #-( (fig_dict['bar_width']+bar_gap_width)*len(fig_dict["y1_name"])/2 if fig_dict['y2_fig_type']== 'bar' else 0)
        #     if fig_dict['y1_fig_type'] == 'plot':
        #         ax.plot(fig_dict["x_value"] +10*idx_y, fig_dict["y1_value"][idx_y], fig_dict["y1_linestyle"], marker=fig_dict["y1_marker"][idx_y], color=color[idx_y],  linewidth=fig_dict["linewidth"], markersize=fig_dict["markersize"], label=fig_dict["y1_legend"][idx_y], zorder=10, markerfacecolor= fig_dict["y1_markerfacecolor"] if "y1_markerfacecolor" in fig_dict else None, markeredgecolor = fig_dict["y1_markeredgecolor"] if "y1_markeredgecolor" in fig_dict else None, markeredgewidth = fig_dict["y1_markeredgewidth"] if "y1_markeredgewidth" in fig_dict else None)
        #     elif fig_dict['y1_fig_type'] == 'bar':
        #         ax.bar(fig_dict["x_value"] \
        #             +(fig_dict['bar_width'] +bar_gap_width)*(idx_y-(len(fig_dict["y1_name"])/2-1/2))
        #             + ax_bar_center_bias \
        #             ,fig_dict["y1_value"][idx_y], width=fig_dict['bar_width'], linewidth=fig_dict["linewidth"],label=fig_dict["y1_legend"][idx_y],facecolor= fig_dict["y1_facecolor"][idx_y] if "y1_facecolor" in fig_dict else color[idx_y],edgecolor= fig_dict["y1_edgecolor"][idx_y] if "y1_edgecolor" in fig_dict else None, hatch = fig_dict['y1_hatch'][idx_y] if 'y1_hatch' in fig_dict else None, zorder=10)
        #     else:
        #         print("Key Error 'fig_type'")
        #         os.exit()

        # ax.set_xlabel(fig_dict["x_label"], size=label_size, family=family)
        # ax.set_ylabel(fig_dict["y1_label"], size=label_size, color=(0,0,0) if 'y1_axis_color' not in fig_dict else fig_dict['y1_axis_color'], family=family)
        
        # from matplotlib.pyplot import MultipleLocator
        # inst = plt.gca()
        # handles1, labels1 = ax.get_legend_handles_labels()
        # len_yticks = len(ax.get_yticks()) if 'len_yticks' not in fig_dict else fig_dict['len_yticks']
        # ax.set_yticks(np.linspace(0 if 'y1_yticks_min' not in fig_dict else fig_dict['y1_yticks_min'], fig_dict['y1_yticks_max'], len_yticks)) # occupy fully yaxis
        
        # ax.set_ylim(0 if 'y1_yticks_min' not in fig_dict else fig_dict['y1_yticks_min'],)
        # if fig_dict['y1_fig_type'] == 'bar':
        #     ax.set_xlim(fig_dict['x_value'][0]-fig_dict['bar_width']*2, fig_dict['x_value'][-1]+fig_dict['bar_width']*2)
        # elif 'x_axis_max' in fig_dict and 'x_axis_min' in fig_dict:
        #     ax.set_xlim(fig_dict['x_axis_min'], fig_dict['x_axis_max'])
        # if "y2_name" in fig_dict:
        #     ax1 = ax.twinx()
        #     color1 = fig_dict["y2_color"]
        #     for idx_y in range(len(fig_dict["y2_name"])):
        #         if fig_dict['y2_fig_type'] == 'plot':
        #             ax1.plot(fig_dict["x_value"]+10*idx_y, fig_dict["y2_value"][idx_y], fig_dict["y2_linestyle"], marker=fig_dict["y2_marker"][idx_y], color=color1[idx_y],  linewidth=fig_dict["linewidth"], markersize=fig_dict["markersize"], label=fig_dict["y2_legend"][idx_y], zorder=10,markerfacecolor= fig_dict["y2_markerfacecolor"] if "y2_markerfacecolor" in fig_dict else None, markeredgecolor = fig_dict["y2_markeredgecolor"] if "y2_markeredgecolor" in fig_dict else None, markeredgewidth = fig_dict["y2_markeredgewidth"] if "y2_markeredgewidth" in fig_dict else None)
        #         elif fig_dict['y2_fig_type'] == 'bar':
        #             ax1.bar((np.array(fig_dict["x_value"])\
        #             + (fig_dict['bar_width'] +bar_gap_width)*(idx_y-(len(fig_dict["y2_name"])/2-1/2)) \
        #             -ax_bar_center_bias\
        #             ),fig_dict["y2_value"][idx_y],width=fig_dict['bar_width'], linewidth=fig_dict["linewidth"],label=fig_dict["y2_legend"][idx_y], facecolor= fig_dict["y2_facecolor"][idx_y] if "y2_facecolor" in fig_dict else color1[idx_y],edgecolor= fig_dict["y2_edgecolor"][idx_y] if "y2_edgecolor" in fig_dict else None, hatch = fig_dict['y2_hatch'][idx_y] if 'y2_hatch' in fig_dict else None, zorder=10)
        #         else:
        #             print("Key Error 'fig_type'")
        #             os.exit()  

        #     ax1.set_ylabel(fig_dict["y2_label"], size=label_size, color=(0,0,0) if 'y2_axis_color' not in fig_dict else fig_dict['y2_axis_color'], family=family)
        #     handles2, labels2 = ax1.get_legend_handles_labels()
        #     print(handles1, labels1)
        #     if 'y2_legend_off' in fig_dict:
        #         plt.legend(handles1, labels1, fontsize=fig_dict['legend_size'] if 'legend_size' in fig_dict else label_size,loc=fig_dict['legend_loc'],frameon=False,ncol=fig_dict["legend_ncol"] if "legend_ncol" in fig_dict else 1)
        #     else:
        #         plt.legend(handles1+handles2, labels1+labels2,fontsize=fig_dict['legend_size'] if 'legend_size' in fig_dict else label_size, loc=fig_dict['legend_loc'],frameon=False,ncol=fig_dict["legend_ncol"] if "legend_ncol" in fig_dict else 1)
        #     ax1.spines['right'].set_color(color1 if 'y2_axis_color' not in fig_dict else fig_dict['y2_axis_color'])
        #     ax1.tick_params(axis='y', colors=color1 if 'y2_axis_color' not in fig_dict else fig_dict['y2_axis_color'])

        #     ax1.set_yticks(np.linspace(0 if 'y2_yticks_min' not in fig_dict else fig_dict['y2_yticks_min'], fig_dict['y2_yticks_max'], len_yticks)) # same number of yticks with ax
        #     ax1.set_ylim(0 if 'y2_yticks_min' not in fig_dict else fig_dict['y2_yticks_min'], fig_dict['y2_yticks_max'])
        #     ax1.spines['top'].set_visible(False)
        #     ax1.spines['left'].set_visible(False)
        #     ax1.tick_params(axis = 'both', labelsize = fig_dict['xticks_fontsize'])
            
        # else:
        #     plt.legend(handles1, labels1, fontsize=fig_dict['legend_size'] if 'legend_size' in fig_dict else label_size, loc=fig_dict['legend_loc'], frameon=False, ncol=fig_dict["legend_ncol"] if "legend_ncol" in fig_dict else 1)
        #     # plt.legend('boxoff')
        #     ax.spines['top'].set_linewidth(1)
        #     ax.spines['right'].set_linewidth(1)
        # if 'xticks' in fig_dict: # redefine xticks
        #     plt.xticks(fig_dict['x_axis'] if "x_axis" in fig_dict else fig_dict['x_value'], fig_dict['xticks'])
        #     if 'rotation' in fig_dict and fig_dict['rotation'] != 0:
        #         fig.autofmt_xdate(rotation=fig_dict['rotation'])
        #     ax.tick_params(axis = 'both', labelsize = fig_dict['xticks_fontsize'])
        #     # ax.tick_params(axis = 'x', labelsize = fig_dict['xticks_fontsize'])
        # if "plt_text" in fig_dict:
        #     for x in range(len(fig_dict['x_value'])):
        #         for idx_y in range(len(fig_dict["y1_name"])):
        #             if fig_dict['y1_value'][idx_y][x] > 0:
        #                 ax.text(fig_dict['x_value'][x]\
        #                 +(fig_dict['bar_width'] +bar_gap_width)*(idx_y-(len(fig_dict["y1_name"])/2-1/2))\
        #                 +ax_bar_center_bias\
        #                 , fig_dict['y1_value'][idx_y][x]+0.05*ax.get_yticks()[-1],'%.1f' %fig_dict['y1_value'][idx_y][x],va='top', ha='center', fontsize=label_size)
        #         if 'y2_value' in fig_dict:
        #             for idx_y in range(len(fig_dict["y1_name"])):
        #                 if fig_dict['y2_value'][idx_y][x]> 0:
        #                     ax1.text(fig_dict['x_value'][x]\
        #                     + (fig_dict['bar_width'] +bar_gap_width)*(idx_y-(len(fig_dict["y2_name"])/2-1/2)) \
        #                     -ax_bar_center_bias\
        #                     , fig_dict['y2_value'][idx_y][x]+0.05*ax1.get_yticks()[-1],'%.1f' %fig_dict['y2_value'][idx_y][x],va='top', ha='center', fontsize=label_size)
        # ax.spines['left'].set_color((0,0,0) if 'y1_axis_color' not in fig_dict else fig_dict['y1_axis_color'])
        # ax.spines['left'].set_linewidth(1)
        # ax.spines['bottom'].set_linewidth(1)
        # plt.tick_params(which='major',width=1.5, length=8)
        # ax.tick_params(axis='y', colors=(0,0,0) if 'y1_axis_color' not in fig_dict else fig_dict['y1_axis_color'])
        
        # plt.savefig(fig_dict['fig_name'], format='svg')
        # plt.show()