import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 


def pca(img):

  '''
  Function: performs PCA analysis on raster files - satellite images

  Args: 
  img :: raster

  Output: PCA values for each band

  '''

  
  #calculus dos autovetores e autovalores
  matrix = img.reshape(img.shape[0]*img.shape[1], img.shape[2])

#calculating matrix covariance among bands
  cov = np.cov(matrix.T)

#calculating eigenvectors
  autoval,autovec = np.linalg.eig(cov)

  #sorting values


#Function that returns the indexes to sort an array
  ord = autoval.argsort()[::-1]
  autoval = autoval[ord]
  autovec = autovec[:,ord]

  #Computando as componentes  
  PC = np.matmul(matrix,autovec)

  PC_3D = PC.reshape(img.shape[0],img.shape[1],img.shape[2])
  return autovec, PC_3D

def autovec_tab(auto_v, bands):
  
  # formatting output of numeric values
  pd.options.display.float_format = '{:,.3f}'.format
  # Creating dataframe
  df = pd.DataFrame(auto_v.T, columns=bands)
  return df

def vis(array):

  '''
  Function: creates a 4 x 4 visualization for raster images

  Args:

  array :: raster transformed to an numpy array.

  '''
  #plotting PCs 
  fig,axes = plt.subplots(2,2,figsize=(15,13),
                          sharex='all',
                          sharey='all')
  

  fig.suptitle('Principal Components',
               fontsize=30)


  axes = axes.ravel()
  for i in range(array.shape[2]):
      axes[i].imshow(array[:,:,i],cmap='gray')
      axes[i].set_title('PC '+str(i+1),fontsize=25)
      axes[i].axis('off')
  return plt.show()

def expansion(img, percent_ini=2, percent_end=98):

  '''
  Function: sets tresholds for the bands visualization between 2 and 98%
  in order to improve the visualization

  Args:

  img: raster band
  percent_ini (default): 2
  percent_end (defult): 98

  Output: raster with expansion filter applied.

  '''
    s = np.zeros_like(img)
    x,y = 0,255  
    w = np.percentile(img, percent_ini)
    z = np.percentile(img, percent_end)        
    p = x + (img - w) * (y - x) / (z - w)    
    p[p<x] = x
    p[p>y] = y
    s = p
    return s
