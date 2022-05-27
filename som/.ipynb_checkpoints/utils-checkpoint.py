"""
Utilities (utils)
    
This file can also be imported as a module to utilize the following functions: 
    * vertical_stack
    * generate_colors

"""

from astropy.table import Column, Table, vstack

import numpy as np



def stack_vertically(catalog_1, catalog_2, id_1, id_2): 
    """ 
    Stacks two catalogs vertically, retaining origin information. 
    
    Parameters 
    ----------
    catalog_1: (astropy.Table)
        The first catalog in the stack.
    catalog_2: (astropy.Table)
        The second catalog in the stack. 
    id_1: (str)
        The identifying information for the first catalog. (i.e., catalog name)
    id_2: (str)
        The identifying information for the second catalog. 
        
    Returns
    -------
    stacked_catalog: (astropy.Table) 
        Vertically stacked catalog containing identifier "catalog_name". 
        
    """
    
    # add a column to both catalog 1 and catalog 2 to store identifiers
    
    # initialize columns
    col_1 = Column(name = 'catalog_name', data = np.full(len(catalog_1), str(id_1))) 
    col_2 = Column(name = 'catalog_name', data = np.full(len(catalog_2), str(id_2)))
    
    # add columns to catalogs
    catalog_1.add_column(col_1)
    catalog_2.add_column(col_2)
    
    # vertically stack catalogs 
    stacked_catalog = vstack((catalog_1, catalog_2))
    
    return stacked_catalog

def generate_colors(catalog, bands, isMag = True): 
    """
    # TO DO: Change based on input catalog type...!
    Generates colors from provided list of bands. 
    
    Parameters
    ----------
    catalog: (astropy.Table) 
        Catalog containing either magnitudes or fluxes in specified bands.
    bands: (str) 
        String containing all of the bands to generate colors. 
    isMag: (bool)
        Will the colors be generated from magnitudes? default = True.
    
    Returns
    ----------
    catalog: (astropy.Table) 
        Catalog containing colors. 
    colors_array: (np.array)
        Array containing colors only. 
        
    """
    
    bands = list(bands) 
    n_bands = len(bands)
    
    if isMag == True: 
        
        # generate colors and append to original catalog
        for ii in range(n_bands - 1): 
            catalog[f'{str(bands[ii])}-{str(bands[ii+1])}'] = (catalog[f'{str(bands[ii])}'] - catalog[f'{str(bands[ii+1])}'])
    
        # generate np.array with colors only
        # list of str containing color names
        colors = [f'{str(bands[ii])}-{str(bands[ii+1])}' for ii in range(n_bands - 1)]
        # catalog containing colors
        catalog_colors = catalog[colors]
        
        length = len(catalog_colors)
        array_colors = np.array([catalog_colors[clr] for clr in colors]).reshape(length, n_bands - 1)
        
    return catalog, array_colors 

    
def normalize_data(array): 
    """
    Normalizes the input array.
    Ex: Normalizes colors to be input to SOM.
    
    Parameters
    ----------
    array: (np.array) 
        Array containing data to be normalized.
        
    Returns
    -------
    norm_array: (np.array) 
        Normalized array.
    """
    
    norm_array = np.array(
        (array - np.mean(array, axis = 0)) / 
        np.std(array, axis = 0))
    
    return norm_array
    