# Overlapping Fields
## Overview of the overlap between C3 fields (VVDS, COSMOS, EGS) and DES, HSC, and KiDS. 

## HSC 
## VVDS x HSC (wide)

**VVDS**

- vvds_c3r2_phot_2021nov17.fits

**HSC**

- pdf-s17a_wide-9812.cat.fits
- pdf-s17a_wide-9813.cat.fits

The above two catalogs have no positional information. Thusly, I will use the following files for the positions: 

- target_wide_s17a_9812.fits
- target_wide_s17a_9813.fits

**Results:** 

VVDS x HSC 9812 **do not** **have** any matches. The smallest on-sky distance between any two sources is ~112.46$\degree$. 

VVDS x HSC 9813 **do not have** any matches. The smallest on-sky distance between any two sources is ~112.56$\degree$.

## COSMOS x HSC (wide)

**COSMOS**

- cosmos_c3r2_phot_2021nov17.fits

**HSC** 

- pdf-s17a_wide-9812.cat.fits
- pdf-s17a_wide-9813.cat.fits

The above two catalogs have no positional information. Thusly, I will use the following files for the positions: 

- target_wide_s17a_9812.fits
- target_wide_s17a_9813.fits

**Results:** 

COSMOS x HSC 9812 **have** 17,816 matches. 

COSMOS x HSC 9813 **have** 252,447 matches. 

## EGS x HSC (wide)

**EGS**

No C3R2 catalog is yet available. Using bounds of field. 

- center (RA, Dec): (214.75, 52.68333)
- length x width: 1 deg$^2$

**Results:** 

EGS x HSC 9812 **do not have** any matches. 

EGS x HSC 9813 **do not have** any matches. 

# ### DES

## VVDS x DES

**VVDS**

- vvds_c3r2_phot_2021nov17.fits

**DES**

- positions_mcal-y1a1-combined-riz-unblind-v4-matched.fits

**Results:** 

VVDS x DES **have** 57,693 matches. 

## COSMOS x DES

**COSMOS**

- cosmos_c3r2_phot_2021nov17.fits

**DES**

- positions_mcal-y1a1-combined-riz-unblind-v4-matched.fits

**Results:** 

COSMOS x DES **have** 177,223 matches. 

Double check this result! 

 

## EGS x DES

**EGS**

No C3R2 catalog is yet available. Using bounds of field. 

- center (RA, Dec): (214.75, 52.68333)
- length x width: 1 deg$^2$

**DES**

- positions_mcal-y1a1-combined-riz-unblind-v4-matched.fits

**Results:** 

Still running? 

By inspection, there is no overlap. 

# Creating the Footprint Plot...

**Which fields do we need?** 

HSC, DES, KiDS

And also C3R2: 

VVDS, COSMOS, EGS
