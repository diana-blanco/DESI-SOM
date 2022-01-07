# Overlapping Fields
### <em> Overview of the overlap between C3 fields (VVDS, COSMOS, EGS) and DES, HSC, and KiDS. </em> 

# The Catalogs

- vvds_c3r2_phot_2021nov17.fits — VVDS-2h photometry
- cosmos_c3r2_phot_2021nov17.fits — COSMOS photometry
- positions_mcal-y1a1-combined-riz-unblind-v4-matched.fits — DES positions (truncated from shear catalog)
- target_wide_s17a_9812.fits — HSC photoz with lensing cuts
- target_wide_s17a_9813.fits — HSC photoz with lensing cuts
- COSMOSadaptdepth_ugriZYJHKs_rot_photoz.cat — KiDS + CFHT-z (z.MP9801, the first-generation one) + UltraVISTA YJHK photometry

 

# HSC

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

**Visual Inspection:** 

No overlap. (Note: HSC-wide catalog has lensing cuts) 

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

**Visual Inspection:** 

Overlap. 

## EGS x HSC (wide)

**EGS**

No C3R2 catalog is yet available. Using bounds of field. 

- center (RA, Dec): (214.75, 52.68333)
- length x width: 1 deg$^2$

**Results:** 

EGS x HSC 9812 **do not have** any matches. 

EGS x HSC 9813 **do not have** any matches. 

**Visual Inspection:** 

No overlap.

# DES

## VVDS x DES

**VVDS**

- vvds_c3r2_phot_2021nov17.fits

**DES**

- positions_mcal-y1a1-combined-riz-unblind-v4-matched.fits

**Results:** 

VVDS x DES **have** 57,693 matches. 

**Visual Inspection:** 

Overlap.

## COSMOS x DES

**COSMOS**

- cosmos_c3r2_phot_2021nov17.fits

**DES**

- positions_mcal-y1a1-combined-riz-unblind-v4-matched.fits

**Results:** 

COSMOS x DES **do not** have any matches. (?) 

 **Visual Inspection:** 
No overlap.
(Observed overlap is between COSMOS and DES Science Verification lensing shear catalog... (i.e., Jarvis et al 2015).) 

## EGS x DES

**EGS**

No C3R2 catalog is yet available. Using bounds of field. 

- center (RA, Dec): (214.75, 52.68333)
- length x width: 1 deg$^2$

**DES**

- positions_mcal-y1a1-combined-riz-unblind-v4-matched.fits

**Results:** 

EGS x DES **do not have** any matches.

**Visual Inspection:** 

No overlap. 

# KiDS

## VVDS x KiDS

**VVDS**

- vvds_c3r2_phot_2021nov17.fits

**KiDS**

- COSMOSadaptdepth_ugriZYJHKs_rot_photoz.cat

**Results:** 

VVDS x KiDS **do not have** any matches. 

**Visual Inspection:** 

No overlap. 

## COSMOS x KiDS

**COSMOS**

- cosmos_c3r2_phot_2021nov17.fits

**KiDS**

- COSMOSadaptdepth_ugriZYJHKs_rot_photoz.cat

**Results:**

COSMOS x KiDS **have** 87,683 matches. 

**Visual Inspection:** 

Overlap.

## EGS x KiDS

No C3R2 catalog is yet available. Using bounds of field. 

- center (RA, Dec): (214.75, 52.68333)
- length x width: 1 deg$^2$

**KiDS**

- COSMOSadaptdepth_ugriZYJHKs_rot_photoz.cat

**Results:** 

EGS x KiDS **do not have** any matches. 

**Visual Inspection:** 

No overlap.
