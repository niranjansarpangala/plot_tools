#Shree Durga Devi Namah
import os
home =os.getenv("HOME")
import sys
sys.path.append(home)
import matplotlib
def mat_behaviour(show):
    if show==0:
        #matplotlib.use('Agg') #for png
        matplotlib.use('PS') #for vector graphics
mat_behaviour(0)
import matplotlib.pyplot as plt
from plot_tools.plot_tool_class import quick_plot_tools
import numpy as np
def bar_plotter(data1,*args, **kwargs):
    from matplotlib import rcParams
    rcParams.update({'figure.autolayout': True})
    ylim = kwargs.get('ylim', None)
    #xv=kwargs.get('xv', None)
    yv=kwargs.get('yv', None)
    yerr=kwargs.get('yerr', None)
    ylabel=kwargs.get('ylabel', None)
    xlabel=kwargs.get('xlabel', None)
    colum=kwargs.get('colum', None)
    ymult=kwargs.get('ymult', 1.0)
    ind=kwargs.get('ind', None)
    [llsiz,lfsiz]=[20,20]
    data2=data1
    data2[yv]=data2[yv]*ymult
    if yerr is not None:
        data2[yerr]=data2[yerr]*ymult
    data1=data2.pivot(index=ind, columns=colum)
    if yerr is not None:
        ax1=data1[yv].plot.bar(rot=0,yerr=data1[yerr])
    else:
        ax1=data1[yv].plot.bar(rot=0)
    ax1.set_ylim(ylim)
    ax1.set_xlabel(xlabel,fontname='serif',fontsize=lfsiz)
    ax1.set_ylabel(ylabel,fontname='serif',fontsize=lfsiz)
    ax1.tick_params(axis='both',which='both', labelsize=llsiz)
    ax1.tick_params(axis='both',which='major',length=12,width=1.5 )
    #ax1.legend(fontsize=lfsiz-7)
    handles_p,labels_p=ax1.get_legend_handles_labels()
    for num in range(len(labels_p)):
        labels_p[num]=colum+" = " +labels_p[num]
    ax1.legend(handles=handles_p,labels=labels_p,fontsize=12)
    fig=ax1.get_figure()
    return fig

def bar_plot_one_variable(data1,*args, **kwargs):
    from matplotlib import rcParams
    rcParams.update({'figure.autolayout': True})
    ylim = kwargs.get('ylim', None)
    #xv=kwargs.get('xv', None)
    yv=kwargs.get('yv', None)
    yerr=kwargs.get('yerr', None)
    ylabel=kwargs.get('ylabel', None)
    xlabel=kwargs.get('xlabel', None)
    ymult=kwargs.get('ymult', 1.0)
    ind=kwargs.get('ind', None)
    [llsiz,lfsiz]=[20,20]
    data2=data1
    data2[yv]=data2[yv]*ymult
    if yerr is not None:
        data2[yerr]=data2[yerr]*ymult
    data1=data2
    #fig,ax1=plt.subplots()
    no_items=5
    width = 1.0/(no_items + 2)
    
    if yerr is not None:
        ax1=data1.plot.bar(y=yv,rot=0,yerr=data1[yerr])
        #ax1.bar(list(data1[ind]),data1[yv],yerr=data1[yerr],width=width)
    else:
        ax1=data1[yv].plot.bar(x=ind,rot=0)
    ax1.set_ylim(ylim)
    ax1.set_xlabel(xlabel,fontname='serif',fontsize=lfsiz)
    ax1.set_ylabel(ylabel,fontname='serif',fontsize=lfsiz)
    ax1.tick_params(axis='both',which='both', labelsize=llsiz)
    ax1.tick_params(axis='both',which='major',length=12,width=1.5 )
    #ax1.legend(fontsize=lfsiz-7)
    #handles_p,labels_p=ax1.get_legend_handles_labels()
    #for num in range(len(labels_p)):
    #    labels_p[num]=colum+" = " +labels_p[num]
    #ax1.legend(handles=handles_p,labels=labels_p,fontsize=12)
    fig=ax1.get_figure()
    return fig

def plot_distribution(df,LIST,show,**kwargs):
    '''
    plots distribution of column values of the given dataframe df
    '''
    kwa = {'cumulative': True}
    cumulative=kwargs.get('cumulative',0) #kwarg cumulative is to be set to 1 to get cumulative plot
    sns_on=kwargs.get('sns_on',0) # sns_on=1 to get the seaborn plot, only PDF here -I wasn't able plot seabron cumulative 
    fig, ax=plt.subplots()
    range_v=kwargs.get('range_v',0)
    xlabel=kwargs.get('xlabel',None)
    var=kwargs.get('var',None)
    qp=quick_plot_tools()
    #sets the range of values for numpy histogram - will be used only if sns_on=0
    for ele in LIST.keys():
        arr=np.array(df[ele])
        arr=arr[~np.isnan(arr)] #removes nan values from the array
        fig_arr=[fig,ax] 
        bin_size=20
        lab=var[0]+"="+str(LIST[ele][0])+r' $\mu m^2$ '+var[1]+"="+str(LIST[ele][1])
        if sns_on==0:
            fig,ax=qp.add_hist(fig_arr,arr,range_v,bin_size,cumulative=cumulative,label=lab)
        elif sns_on==1:
            #ax=sns.distplot(arr,hist_kws=kwa, kde_kws=kwa,label="D= "+str(LIST[ele][0])+r' $\mu m^2$'+" P="+str(LIST[ele][1]))
            ax=sns.distplot(arr,hist=True,norm_hist=True,label=lab)
    [lfsiz,llsiz]=[15,15]
    ax.set_xlabel(xlabel,fontname='serif',fontsize=lfsiz)
    if cumulative==0:
        ax.set_ylabel(r'Probability',fontname='serif',fontsize=lfsiz)
    elif cumulative==1:
        if sns_on==1:
            print("Are you sure? sns_on=1") #warning
        ax.set_ylabel("CDF",fontname='serif',fontsize=lfsiz)
    ax.tick_params(axis='both',which='both', labelsize=llsiz)
    ax.tick_params(axis='both',which='major',length=12,width=1.5 )
    ax.legend()
    return fig
    #filename_path=path+filename
    #qp.savefig(1,fig,filename_path)
    
