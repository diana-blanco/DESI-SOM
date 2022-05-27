"""
Self Organizing Maps (SOMs)

Herein lie the SOM codes used to: 
    * generate a new SOM using input data
    * re-create an existing SOM 
    
This file can also be imported as a module to utilize the following functions: 
    * generate_som
    * recreate_som
    
TODO: 
    Edit median z map to specify which z is used...
    Better place to generate win_map? 
    Plot som: might be better to generate the maps separately and then pass the maps? 
    Plot som: yep to the above. In the meantime, there is a plot recreate som
"""

import matplotlib.colors as colors
import matplotlib.pyplot as plt 


from minisom import MiniSom
from mpl_toolkits.axes_grid1 import make_axes_locatable

import numpy as np


def generate_som(n, m, norm_array, num_iteration = int(1e6), sigma = 1.5, learning_rate = 0.5): 
    """
    Generates a self-organizing map based on the input array.
    
    Parameters
    ----------
    n: (int)
        Dimension of SOM along n axis.
    m: (int) 
        Dimension of SOM along m axis.
    norm_array: (np.array)
        Normalized array containing input data.
    sigma: (float) 
        Spread of the neighborhood function.
    learning_rate: (float)
        Initial learning rate. 
        
    Returns
    -------
    som: (minisom.MiniSom)
        ...
    win_map: ()
        ...
        
    """
    
    # initiate som
    som = MiniSom(
        n, m, norm_array.shape[1], sigma = 1.5, learning_rate = 0.5, neighborhood_function = 'gaussian', random_seed = 0) 
    print('initialized som...') 
    
    # initiate SOM weights to span first two PCAs
    som.pca_weights_init(norm_array)
    
    print('training...')
    # train SOM
    som.train(norm_array, num_iteration = num_iteration, verbose = True)
    
    win_map = generate_win_map(norm_array, som)
    
    return som, win_map

def generate_win_map(norm_array, som): 
    """
    Generates a map containing the indices of all the galaxies in som cell. 
    
    Parameters
    ----------
    norm_array: (np.array)
        Normalized array containing input data.
    som: (minisom.MiniSom)
        Self-organizing map. 
        
    Returns
    -------
    win_map: ()
        ...
        
    """
    
    win_map = som.win_map(norm_array, return_indices = True) # returns a dictionary with all indices of the elements
    
    return win_map


def generate_med_z(catalog, som, win_map): 
    """
    Generates map containing median redshift in som cell. 
    
    Parameters
    ----------
    catalog: (astropy.Table) 
        Original catalog containing redshift information.
    som: (minisom.MiniSom)
        Self-organizing map. 
        
    Returns
    -------
    med_z_map: (np.array)
        Map containing the median redshift in each som cell. 
    """
    
    # empty "map" to hold median zs
    med_z_map = np.zeros(som.distance_map().shape)
    
    for iy, ix in np.ndindex(med_z_map.shape): 
        med_z_map[iy, ix] = np.median(catalog[win_map[(iy, ix)]]['z_spec'])
        
    return med_z_map

def recreate_med_z(catalog, som_shape, win_map): 
    """
    Recreates map containing median redshift in som cell. 
    
    Parameters
    ----------
    catalog: (astropy.Table) 
        Original catalog containing redshift information.
    som: (minisom.MiniSom)
        Self-organizing map. 
        
    Returns
    -------
    med_z_map: (np.array)
        Map containing the median redshift in each som cell. 
    """
    
    # empty "map" to hold median zs
    med_z_map = np.zeros(som_shape)
    
    for iy, ix in np.ndindex(med_z_map.shape): 
        med_z_map[iy, ix] = np.median(catalog[win_map[(iy, ix)]]['z_spec'])
        
    return med_z_map

def generate_occ(catalog, som, win_map): 
    """
    Generates map containing occupation in som cell. 
    
    Parameters
    ----------
    catalog: (astropy.Table) 
        Original catalog containing redshift information.
    som: (minisom.MiniSom) 
        Self-organizing map. 
    
    Returns
    -------
    occ_map: (np.array)
        Map containing the occupation in each som cell. 
    """
    
    # create empty "map" to hold occupation in each cell
    occ_map = np.zeros(som.distance_map().shape)

    for iy, ix in np.ndindex(occ_map.shape):  
        occ_map[iy, ix] = len(win_map[(iy,ix)])
    
    return occ_map

def recreate_occ(catalog, som_shape, win_map): 
    """
    Generates map containing occupation in som cell. 
    
    Parameters
    ----------
    catalog: (astropy.Table) 
        Original catalog containing redshift information.
    som: (minisom.MiniSom) 
        Self-organizing map. 
    
    Returns
    -------
    occ_map: (np.array)
        Map containing the occupation in each som cell. 
    """
    
    # create empty "map" to hold occupation in each cell
    occ_map = np.zeros(som_shape)

    for iy, ix in np.ndindex(occ_map.shape):  
        occ_map[iy, ix] = len(win_map[(iy,ix)])
    
    return occ_map

def generate_z_occ(catalog, som_shape, win_map, occ_z): 
    """
    Generates map containing occupation of specified z in som cell. 
    
    Parameters
    ----------
    catalog: (astropy.Table) 
        Original catalog containing redshift information.
    som: (minisom.MiniSom) 
        Self-organizing map. 
    
    Returns
    -------
    occ_map: (np.array)
        Map containing the occupation in each som cell. 
    """
    
    # create empty "map" to hold occupation in each cell
    occ_z_map = np.zeros(som_shape)

    for iy, ix in np.ndindex(occ_map.shape):  
        occ_z_map[iy, ix] = len(win_map[(iy,ix)])
    
    return occ_z_map

def generate_w_d(catalog, som, win_map): 
    """
    Generates map of deep weights for each cell... 
    
    Parameters 
    ----------
    catalog: (astropy.Table) 
        Original catalog containing redshift information.
    som: (minisom.MiniSom) 
        Self-organizing map.
    
    Returns 
    -------
    w_d_map: (np.array) 
        Map of deep weights. 
    """
    # create empty map to hold deep weights 
    w_d_map = np.zeros(som.distance_map().shape)

    for iy, ix in np.ndindex(w_d_map.shape): 
        # first, determine if N_z(c_k) == 0, if so, arbitrarily set weight as 'NaN'
        # (this means that none of the galaxies from the deep sample that fall into 
        # that color cell do NOT have a match in the redshift sample
    
        # store galaxies with zs from deep  sample (probably a better way to name this)
        gals_w_z_deep = win_map[(iy,ix)]
    
        # store galaxies with zs from redshift sample (probably a better way to name this)
        gals_w_z_redshift = catalog[win_map[(iy,ix)]][np.where(catalog[win_map[(iy,ix)]]['has_z_spec'] == True)]
    
        # count N_d and N_z 
        N_d = len(win_map[(iy,ix)]) 
        N_z = len(gals_w_z_redshift) 
    
        if N_z != 0: 
            w_d_map[iy, ix] = N_d / N_z 
    
        elif N_z == 0: 
            w_d_map[iy, ix] = None
            
    return w_d_map

def recreate_w_d(catalog, som_shape, win_map): 
    """
    Generates map of deep weights for each cell... 
    
    Parameters 
    ----------
    catalog: (astropy.Table) 
        Original catalog containing redshift information.
    som: (minisom.MiniSom) 
        Self-organizing map.
    
    Returns 
    -------
    w_d_map: (np.array) 
        Map of deep weights. 
    """
    # create empty map to hold deep weights 
    w_d_map = np.zeros(som_shape)

    for iy, ix in np.ndindex(w_d_map.shape): 
        # first, determine if N_z(c_k) == 0, if so, arbitrarily set weight as 'NaN'
        # (this means that none of the galaxies from the deep sample that fall into 
        # that color cell do NOT have a match in the redshift sample
    
        # store galaxies with zs from deep  sample (probably a better way to name this)
        gals_w_z_deep = win_map[(iy,ix)]
    
        # store galaxies with zs from redshift sample (probably a better way to name this)
        gals_w_z_redshift = catalog[win_map[(iy,ix)]][np.where(catalog[win_map[(iy,ix)]]['has_z_spec'] == True)]
    
        # count N_d and N_z 
        N_d = len(win_map[(iy,ix)]) 
        N_z = len(gals_w_z_redshift) 
    
        if N_z != 0: 
            w_d_map[iy, ix] = N_d / N_z 
    
        elif N_z == 0: 
            w_d_map[iy, ix] = None
            
    return w_d_map

def generate_i_mag_map(catalog, som_shape, win_map): 
    """
    Generates map of median i-band mag for each cell... 
    
    Parameters 
    ----------
    catalog: (astropy.Table) 
        Original catalog containing redshift information.
    som: (minisom.MiniSom) 
        Self-organizing map.
    
    Returns 
    -------
    w_d_map: (np.array) 
        Map of deep weights. 
    """
    # create empty "map" to hold occupation in each cell
    i_mag_map = np.zeros(som_shape)

    for iy, ix in np.ndindex(i_mag_map.shape):  
        i_mag_map[iy, ix] = np.median(catalog[win_map[(iy, ix)]]['I_1'])# change
    
    return i_mag_map

def plot_som(catalog, som, win_map, plot_dist_map = False, plot_med_z_map = False, plot_occ_map = False, plot_w_d_map = False):  
    """
    Plots specified maps.
    
    Parameters
    ----------
    catalog: (astropy.Table)
        Catalog, clearly. 
    som: ()
        Self-organizing map.
    win_map: ()
        ...
    plot_dist_map: (bool) 
        Plot the euclidean distance map? 
    plot_med_z_map: (bool) 
        Plot the median redshift map? 
    plot_occ_map: (bool) 
        Plot the occupation map? 
    plot_w_d_map: (bool)
        Plot the deep weights map? 
    Returns
    -------
    """
    
    n_plots = sum([plot_dist_map, plot_med_z_map, plot_occ_map, plot_w_d_map])
    
    n_cols = 2 # arbitrary
    
    n_rows = n_plots // n_cols
    n_rows += n_plots % n_cols
    
    pos_plots = range(1, n_plots + 1) 
    
    # main figure
    fig = plt.figure(figsize = (20,20))
    
    plots = []
    labels = []
    
    if plot_dist_map == True: 
        print('generating distance map...') 
        plots.append(som.distance_map()) #function that generates dist map 
        labels.append('Euclidean Distance') 
        
    if plot_med_z_map == True: 
        print('generating median z map...')
        plots.append(generate_med_z(catalog, som, win_map)) # function that generates median z map
        labels.append('Median z') # edit to specify which z is used... 
    
    if plot_occ_map == True:
        print('generating occupation map...')
        plots.append(generate_occ(catalog, som, win_map))
        labels.append('Occupation') 
    
    if plot_w_d_map == True: 
        print('generating deep weights map...')
        plots.append(generate_w_d(catalog, som, win_map))
        labels.append('$w_d$')       
    
    # plot figure
    for ii in range(n_plots): 
        ax = fig.add_subplot(n_rows, n_cols, pos_plots[ii]) 
        
        divider = make_axes_locatable(ax)
        
        cax = divider.append_axes('right', size='5%', pad=0.05)
        
        if labels[ii] == 'Occupation': 
            im = ax.pcolor(plots[ii], cmap = 'viridis', norm = colors.LogNorm())
        else:
            im = ax.pcolor(plots[ii], cmap = 'viridis')
        
        fig.colorbar(im, cax = cax, orientation = 'vertical') 
        
        ax.title.set_text(labels[ii])

###################################

#def recreate_som(): 

def plot_recreate_som(catalog, win_map, som_shape, plot_dist_map = False, plot_med_z_map = False, plot_occ_map = False, plot_w_d_map = False):  
    """
    Plots specified maps.
    
    Parameters
    ----------
    catalog: (astropy.Table)
        Catalog, clearly. 
    som_shape: (tuple)
        Shape of the SOM.
    win_map: ()
        ...
    plot_dist_map: (bool) 
        Plot the euclidean distance map? 
    plot_med_z_map: (bool) 
        Plot the median redshift map? 
    plot_occ_map: (bool) 
        Plot the occupation map? 
    plot_w_d_map: (bool)
        Plot the deep weights map? 
    Returns
    -------
    """
    
    n_plots = sum([plot_med_z_map, plot_occ_map, plot_w_d_map])
    
    n_cols = 2 # arbitrary
    
    n_rows = n_plots // n_cols
    n_rows += n_plots % n_cols
    
    pos_plots = range(1, n_plots + 1) 
    
    # main figure
    fig = plt.figure(figsize = (10,20))
    
    plots = []
    labels = []
    
    #if plot_dist_map == True: 
    #    print('generating distance map...') 
    #    plots.append(som.distance_map()) #function that generates dist map 
    #    labels.append('Euclidean Distance') 
        
    if plot_med_z_map == True: 
        print('generating median z map...')
        plots.append(recreate_med_z(catalog, som_shape, win_map)) # function that generates median z map
        labels.append('Median z') # edit to specify which z is used... 
    
    if plot_occ_map == True:
        print('generating occupation map...')
        plots.append(recreate_occ(catalog, som_shape, win_map))
        labels.append('Occupation') 
    
    if plot_w_d_map == True: 
        print('generating deep weights map...')
        plots.append(recreate_w_d(catalog, som_shape, win_map))
        labels.append('$w_d$')       
    
    # plot figure
    for ii in range(n_plots): 
        ax = fig.add_subplot(n_rows, n_cols, pos_plots[ii]) 
        
        divider = make_axes_locatable(ax)
        
        cax = divider.append_axes('right', size='5%', pad=0.05)
        
        if labels[ii] == 'Occupation': 
            im = ax.pcolor(plots[ii].T, cmap = 'viridis', norm = colors.LogNorm())
        elif labels[ii] == '$w_d$':
            im = ax.pcolor(plots[ii].T, cmap = 'viridis', norm = colors.LogNorm())
        else:
            im = ax.pcolor(plots[ii].T, cmap = 'viridis')
        
        fig.colorbar(im, cax = cax, orientation = 'vertical') 
        
        ax.axis('equal')

        ax.title.set_text(labels[ii])
    
    plt.tight_layout()
        
def plot_single(catalog, win_map, som_shape, occ_z = None, plot_i_mag_map = False, plot_dist_map = False, plot_med_z_map = False, plot_occ_map = False, plot_occ_z_map = False, plot_w_d_map = False, save = False):  
    """
    Plots specified maps.
    
    Parameters
    ----------
    catalog: (astropy.Table)
        Catalog, clearly. 
    som_shape: (tuple)
        Shape of the SOM.
    win_map: ()
        ...
    map_type = (str)
        What type of map is it? 
    #plot_dist_map: (bool) 
    #    Plot the euclidean distance map? 
    #plot_med_z_map: (bool) 
    #    Plot the median redshift map? 
    #plot_occ_map: (bool) 
    #    Plot the occupation map? 
    #plot_w_d_map: (bool)
    #    Plot the deep weights map? 
    Returns
    -------
    """
    
    n_plots = 1
    #sum([plot_med_z_map, plot_occ_map, plot_w_d_map])
    
    n_cols = 2 # arbitrary
    
    n_rows = n_plots // n_cols
    n_rows += n_plots % n_cols
    
    pos_plots = range(1, n_plots + 1) 
    
    # main figure
    fig = plt.figure(figsize = (7,10))
    
    plots = []
    labels = []
    
    #if plot_dist_map == True: 
    #    print('generating distance map...') 
    #    plots.append(som.distance_map()) #function that generates dist map 
    #    labels.append('Euclidean Distance') 
    
    if plot_i_mag_map == True: 
        print('generating median i-mag map...') 
        plots.append(generate_i_mag_map(catalog, som_shape, win_map))
        labels.append('Median i-band mag') 
        
    if plot_med_z_map == True: 
        print('generating median z map...')
        plots.append(recreate_med_z(catalog, som_shape, win_map)) # function that generates median z map
        labels.append('Median z') # edit to specify which z is used... 
    
    if plot_occ_map == True:
        print('generating occupation map...')
        plots.append(recreate_occ(catalog, som_shape, win_map))
        labels.append('Occupation') 
    
    if plot_occ_z_map == True: 
        print('generating specified z occupation map...') 
        plots.append(generate_z_occ(catalog, som_shape, win_map, occ_z))
        labels.append('Occupation') 
    
    if plot_w_d_map == True: 
        print('generating deep weights map...')
        plots.append(recreate_w_d(catalog, som_shape, win_map))
        labels.append('$w_d$')       
    
    # plot figure
    for ii in range(n_plots): 
        ax = fig.add_subplot(n_rows, n_cols, pos_plots[ii]) 
        
        divider = make_axes_locatable(ax)
        
        cax = divider.append_axes('right', size='5%', pad=0.05)
        
        if labels[ii] == 'Occupation': 
            im = ax.pcolor(plots[ii].T, cmap = 'viridis', norm = colors.LogNorm())
        
        elif labels[ii] == 'Median i-band mag': 
            im = ax.pcolor(plots[ii].T, cmap = 'viridis', norm = colors.LogNorm())
        
        else:
            im = ax.pcolor(plots[ii].T, cmap = 'viridis')
        
        fig.colorbar(im, cax = cax, orientation = 'vertical') 
        
        ax.axis('equal')
        
        ax.title.set_text(labels[ii])
        
    plt.tight_layout()
    
    if save == True: 
        plt.savefig(f'{labels[ii]}.png', dpi = 300)
