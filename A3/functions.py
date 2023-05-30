## functions

def normalize(band):
    band_min, band_max = (band.min(), band.max())
    return ((band - band_min)/((band_max - band_min)))

def brighten(band, alpha = 0.13, beta = 0):
    alpha=0.13
    beta=0
    return np.clip(alpha*band+beta, 0,255)

def gammacorr(band, gamma = 2):
    gamma=2
    return np.power(band, 1/gamma)

def ndvi_calc(red, nir):
    ndvi = (nir - red) / (nir + red)
    return ndvi