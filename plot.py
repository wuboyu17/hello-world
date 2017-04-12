import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt

# plot l'ACP
#changes2
path = 'C:\\Users\\michel\\Desktop\\Spectrecourrier\\CSV\\Jam_clustering\\Analyse_glissante\\' + session_date + '\\caracteristique.csv'
caracteristique = pd.read_csv(filepath_or_buffer=path, sep=';', encoding='latin-1')
caracteristique_reduit = caracteristique[caracteristique['Nb_Pli'] >= 100]
LHE = caracteristique_reduit[['L_Moy', 'H_Moy', 'E_Moy']]
acp = PCA(n_components=2)
LHE_acp = acp.fit_transform(LHE)
xLHE = np.array(LHE_acp[:, 0])
yLHE = np.array(LHE_acp[:, 1])
xLHE = xLHE.astype(int)
yLHE = yLHE.astype(int)

CS = np.array(caracteristique_reduit['CS']).astype(int)
liste_param = []
liste_name = ['Nb_Pli', 'Nb_Jam_MFJ', 'Nb_PM', 'Proportion_Pli_Contigu', 'Proportion_Jam_MFJ', 'Proximite_Jam_MFJ',
              'Contigu_Jam_MFJ', 'Nb_Noisy', 'Nb_Staple', 'Nb_Plastique', 'FrontFringe_Moy', 'RearFringe_Moy', 'Nb_Rejet_OCR',
              'Nb_Inward', 'Nb_Outward', 'Nb_Delivery', 'Nb_Box']
for ele in liste_name:
    liste_param.append(list(caracteristique_reduit[ele]))
data = []


def combine(list1, list2):
    list3 = []
    for i in range(len(list1)):
        list3.append('CS ' + str(list1[i]) + ': ' + str(list2[i]))
    return list3
for i in range(len(liste_param)):
    trace = go.Scatter(
        y=xLHE,
        x=yLHE,
        mode='markers',
        name=liste_name[i],
        marker=dict(
            color=liste_param[i],
            symbol='circle',
            size=16,
        ),
        text=combine(CS, liste_param[i])
    )
    data.append(trace)

layout = go.Layout(
    title="Projeter selon l'aspect physique",
    xaxis=dict(
        showgrid=False,
        showline=True,
        linecolor='rgb(102, 102, 102)',
        titlefont=dict(
            color='rgb(204, 204, 204)'
        ),
        tickfont=dict(
            color='rgb(102, 102, 102)',
        ),
        autotick=False,
        dtick=10,
        ticks='outside',
        tickcolor='rgb(102, 102, 102)',
    ),
    margin=dict(
        l=140,
        r=40,
        b=50,
        t=80
    ),
    legend=dict(
        font=dict(
            size=10,
        ),
        yanchor='middle',
        xanchor='right',
    ),

    paper_bgcolor='rgb(254, 247, 234)',
    plot_bgcolor='rgb(254, 247, 234)',
    hovermode='closest',
)
fig = go.Figure(data=data, layout=layout)
plot(fig, filename='C:\\Users\\michel\\Desktop\\Spectrecourrier\\CSV\\Jam_clustering\\Analyse_glissante\\'
                   + session_date + '\\Projeter selon l aspect physique.html')



# plot images
nb_img = len(caracteristique_reduit['Pli_Pilote_Img'])
for i in range(nb_img):
    plt.subplot(np.ceil(np.sqrt(nb_img)), np.ceil(np.sqrt(nb_img)), i+1)
    J18 = caracteristique_reduit.iloc[i]['Pli_Pilote_Img']
    CS = int(caracteristique_reduit.iloc[i]['CS'])
    im = plt.imread('M:\\Donnees\\BigData\\MSM\\MSM_data\\Acqui_S47_2016_Cx_MSM3\\' + session_date + '\\LIS\\color_high_' + J18 + '.tif')
    implot = plt.imshow(im, interpolation='nearest')
    plt.title(CS)
    plt.axis('off')
    plt.savefig('C:\\Users\\michel\\Desktop\\Spectrecourrier\\CSV\\Jam_clustering\\Analyse_glissante\\'
                   + session_date + '\\CS_images.pdf', dpi=600)





