import numpy as np
from matplotlib import pyplot as plt
class cls_plt_fig():
    def __init__(self, name):
        self.name = name
    def func_plt_fig(self, fig_dict={   "x_name":"Conv Layers", 
            "x_value": np.arange(3), 
            "x_label" : r"$\bf{Conv}$"+' ' +r"$\bf{Layers}$",
            "y1_fig_type": "bar",
            "y1_name":"speedup",
            "y1_value":[1], 
            "y1_color":(0, 0, 0),
            "y1_linestyle":'x-',
            "y1_label":r"$\bf{Speedup}$",
            "y1_marker":'s',
            "y1_legend": r"$\bf{Speedup}$",
            "y1_yticks_max": 18,
            "y1_axis_color":(0,0,0),
            "y2_fig_type": "bar",
            "y2_name":"energy_efficiency",
            "y2_value":[1],
            "y2_color":(1, 0, 0),
            "y2_linestyle":'--',
            "y2_label":r"$\bf{Energy}$" + ' ' + r"$\bf{efficiency}$"+' ' + r"$\bf{(TOPS/W)}$",
            "y2_marker":'^',
            "y2_legend": r"$\bf{Energy}$" + ' ' + r"$\bf{efficiency}$",
            "legend_size": 12,
            "label_size": 12,
            "xticks_fontsize": 12,
            "y2_yticks_max": 12,
            "grid_axis": 'both',
            "linewidth": 2,
            "markersize": 8,
            "family":"Arial",
            # "label_size": 10,
            "bar_width": 0.4,
            "xticks": "layer",
            "plt_text": True,
            "legend_loc": (0.65, 0.8),
            "fig_name" :'../../generate/speedup&EE_layer.svg'
            }): # dict
        print('******** test import ')
        fig, ax = plt.subplots(figsize=fig_dict["figsize"] if "figsize" in fig_dict else (7, 4.6))
        color = fig_dict["y1_color"]
        print("color: {}".format(color))
        family = fig_dict["family"]
        label_size = fig_dict["label_size"]
        bar_gap_width = fig_dict["bar_gap_width"]/2 if "bar_gap_width" in fig_dict else 0
        if 'grid' in fig_dict:
            plt.grid(axis=fig_dict['grid'], zorder=0) #, 
        for idx_y in range(len(fig_dict["y1_name"])):
            print("idx_y: {}".format(idx_y))
            ax_bar_center_bias = 0 #-( (fig_dict['bar_width']+bar_gap_width)*len(fig_dict["y1_name"])/2 if fig_dict['y2_fig_type']== 'bar' else 0)
            if fig_dict['y1_fig_type'] == 'plot':
                ax.plot(fig_dict["x_value"] +10*idx_y, fig_dict["y1_value"][idx_y], fig_dict["y1_linestyle"], marker=fig_dict["y1_marker"][idx_y], color=color[idx_y],  linewidth=fig_dict["linewidth"], markersize=fig_dict["markersize"], label=fig_dict["y1_legend"][idx_y], zorder=10, markerfacecolor= fig_dict["y1_markerfacecolor"] if "y1_markerfacecolor" in fig_dict else None, markeredgecolor = fig_dict["y1_markeredgecolor"] if "y1_markeredgecolor" in fig_dict else None, markeredgewidth = fig_dict["y1_markeredgewidth"] if "y1_markeredgewidth" in fig_dict else None)
            elif fig_dict['y1_fig_type'] == 'bar':
                ax.bar(fig_dict["x_value"] \
                    +(fig_dict['bar_width'] +bar_gap_width)*(idx_y-(len(fig_dict["y1_name"])/2-1/2))
                    + ax_bar_center_bias \
                    ,fig_dict["y1_value"][idx_y], width=fig_dict['bar_width'], linewidth=fig_dict["linewidth"],label=fig_dict["y1_legend"][idx_y],facecolor= fig_dict["y1_facecolor"][idx_y] if "y1_facecolor" in fig_dict else color[idx_y],edgecolor= fig_dict["y1_edgecolor"][idx_y] if "y1_edgecolor" in fig_dict else None, hatch = fig_dict['y1_hatch'][idx_y] if 'y1_hatch' in fig_dict else None, zorder=10)
            else:
                print("Key Error 'fig_type'")
                os.exit()

        ax.set_xlabel(fig_dict["x_label"], size=label_size, family=family)
        ax.set_ylabel(fig_dict["y1_label"], size=label_size, color=(0,0,0) if 'y1_axis_color' not in fig_dict else fig_dict['y1_axis_color'], family=family)
        
        from matplotlib.pyplot import MultipleLocator
        inst = plt.gca()
        handles1, labels1 = ax.get_legend_handles_labels()
        len_yticks = len(ax.get_yticks()) if 'len_yticks' not in fig_dict else fig_dict['len_yticks']
        ax.set_yticks(np.linspace(0 if 'y1_yticks_min' not in fig_dict else fig_dict['y1_yticks_min'], fig_dict['y1_yticks_max'], len_yticks)) # occupy fully yaxis
        
        ax.set_ylim(0 if 'y1_yticks_min' not in fig_dict else fig_dict['y1_yticks_min'],)
        if fig_dict['y1_fig_type'] == 'bar':
            ax.set_xlim(fig_dict['x_value'][0]-fig_dict['bar_width']*2, fig_dict['x_value'][-1]+fig_dict['bar_width']*2)
        elif 'x_axis_max' in fig_dict and 'x_axis_min' in fig_dict:
            ax.set_xlim(fig_dict['x_axis_min'], fig_dict['x_axis_max'])
        if "y2_name" in fig_dict:
            ax1 = ax.twinx()
            color1 = fig_dict["y2_color"]
            for idx_y in range(len(fig_dict["y2_name"])):
                if fig_dict['y2_fig_type'] == 'plot':
                    ax1.plot(fig_dict["x_value"]+10*idx_y, fig_dict["y2_value"][idx_y], fig_dict["y2_linestyle"], marker=fig_dict["y2_marker"][idx_y], color=color1[idx_y],  linewidth=fig_dict["linewidth"], markersize=fig_dict["markersize"], label=fig_dict["y2_legend"][idx_y], zorder=10,markerfacecolor= fig_dict["y2_markerfacecolor"] if "y2_markerfacecolor" in fig_dict else None, markeredgecolor = fig_dict["y2_markeredgecolor"] if "y2_markeredgecolor" in fig_dict else None, markeredgewidth = fig_dict["y2_markeredgewidth"] if "y2_markeredgewidth" in fig_dict else None)
                elif fig_dict['y2_fig_type'] == 'bar':
                    ax1.bar((np.array(fig_dict["x_value"])\
                    + (fig_dict['bar_width'] +bar_gap_width)*(idx_y-(len(fig_dict["y2_name"])/2-1/2)) \
                    -ax_bar_center_bias\
                    ),fig_dict["y2_value"][idx_y],width=fig_dict['bar_width'], linewidth=fig_dict["linewidth"],label=fig_dict["y2_legend"][idx_y], facecolor= fig_dict["y2_facecolor"][idx_y] if "y2_facecolor" in fig_dict else color1[idx_y],edgecolor= fig_dict["y2_edgecolor"][idx_y] if "y2_edgecolor" in fig_dict else None, hatch = fig_dict['y2_hatch'][idx_y] if 'y2_hatch' in fig_dict else None, zorder=10)
                else:
                    print("Key Error 'fig_type'")
                    os.exit()  

            ax1.set_ylabel(fig_dict["y2_label"], size=label_size, color=(0,0,0) if 'y2_axis_color' not in fig_dict else fig_dict['y2_axis_color'], family=family)
            handles2, labels2 = ax1.get_legend_handles_labels()
            print(handles1, labels1)
            if 'y2_legend_off' in fig_dict:
                plt.legend(handles1, labels1, fontsize=fig_dict['legend_size'] if 'legend_size' in fig_dict else label_size,loc=fig_dict['legend_loc'],frameon=False,ncol=fig_dict["legend_ncol"] if "legend_ncol" in fig_dict else 1)
            else:
                plt.legend(handles1+handles2, labels1+labels2,fontsize=fig_dict['legend_size'] if 'legend_size' in fig_dict else label_size, loc=fig_dict['legend_loc'],frameon=False,ncol=fig_dict["legend_ncol"] if "legend_ncol" in fig_dict else 1)
            ax1.spines['right'].set_color(color1 if 'y2_axis_color' not in fig_dict else fig_dict['y2_axis_color'])
            ax1.tick_params(axis='y', colors=color1 if 'y2_axis_color' not in fig_dict else fig_dict['y2_axis_color'])

            ax1.set_yticks(np.linspace(0 if 'y2_yticks_min' not in fig_dict else fig_dict['y2_yticks_min'], fig_dict['y2_yticks_max'], len_yticks)) # same number of yticks with ax
            ax1.set_ylim(0 if 'y2_yticks_min' not in fig_dict else fig_dict['y2_yticks_min'], fig_dict['y2_yticks_max'])
            ax1.spines['top'].set_visible(False)
            ax1.spines['left'].set_visible(False)
            ax1.tick_params(axis = 'both', labelsize = fig_dict['xticks_fontsize'])
            
        else:
            plt.legend(handles1, labels1, fontsize=fig_dict['legend_size'] if 'legend_size' in fig_dict else label_size, loc=fig_dict['legend_loc'], frameon=False, ncol=fig_dict["legend_ncol"] if "legend_ncol" in fig_dict else 1)
            # plt.legend('boxoff')
            ax.spines['top'].set_linewidth(1)
            ax.spines['right'].set_linewidth(1)
        if 'xticks' in fig_dict: # redefine xticks
            plt.xticks(fig_dict['x_axis'] if "x_axis" in fig_dict else fig_dict['x_value'], fig_dict['xticks'])
            if 'rotation' in fig_dict and fig_dict['rotation'] != 0:
                fig.autofmt_xdate(rotation=fig_dict['rotation'])
            ax.tick_params(axis = 'both', labelsize = fig_dict['xticks_fontsize'])
            # ax.tick_params(axis = 'x', labelsize = fig_dict['xticks_fontsize'])
        if "plt_text" in fig_dict:
            for x in range(len(fig_dict['x_value'])):
                for idx_y in range(len(fig_dict["y1_name"])):
                    if fig_dict['y1_value'][idx_y][x] > 0:
                        ax.text(fig_dict['x_value'][x]\
                        +(fig_dict['bar_width'] +bar_gap_width)*(idx_y-(len(fig_dict["y1_name"])/2-1/2))\
                        +ax_bar_center_bias\
                        , fig_dict['y1_value'][idx_y][x]+0.05*ax.get_yticks()[-1],'%.1f' %fig_dict['y1_value'][idx_y][x],va='top', ha='center', fontsize=label_size)
                if 'y2_value' in fig_dict:
                    for idx_y in range(len(fig_dict["y1_name"])):
                        if fig_dict['y2_value'][idx_y][x]> 0:
                            ax1.text(fig_dict['x_value'][x]\
                            + (fig_dict['bar_width'] +bar_gap_width)*(idx_y-(len(fig_dict["y2_name"])/2-1/2)) \
                            -ax_bar_center_bias\
                            , fig_dict['y2_value'][idx_y][x]+0.05*ax1.get_yticks()[-1],'%.1f' %fig_dict['y2_value'][idx_y][x],va='top', ha='center', fontsize=label_size)
        ax.spines['left'].set_color((0,0,0) if 'y1_axis_color' not in fig_dict else fig_dict['y1_axis_color'])
        ax.spines['left'].set_linewidth(1)
        ax.spines['bottom'].set_linewidth(1)
        plt.tick_params(which='major',width=1.5, length=8)
        ax.tick_params(axis='y', colors=(0,0,0) if 'y1_axis_color' not in fig_dict else fig_dict['y1_axis_color'])
        
        plt.savefig(fig_dict['fig_name'], format='svg')
        plt.show()