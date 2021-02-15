# ImageJ-Volume-Converter
---------------------

This python code uses ImageJ Fiji's Macro function to convert DICOM or NRRD files to JPEG , PNG format

we supposed you to use this Program when you need to train the deep learning model for medical data

----------------------

## Program pipe line
1. Python code autometically check the input volume directory and copy the same folder hierarchy to output directory
2. make txt format file list 
3. Call ImageJ Fiji headless version to terminal 
4. Reset to default setting

-------------------

## Code Usage
1. In terminal ,Go to the directory where the soucre code located
2. Type the given terminal command

DICOM Conversion
    
    python3 DicomConverter.py -i <InputVolumeDirectory> -o <OutputVolumeDirectory> -t <ConvertedImageType>
    

NRRD Conversion
    
    python3 DicomConverter.py -i <InputVolumeDirectory> -o <OutputVolumeDirectory> -t <ConvertedImageType>
    
3. Check the files in output volume directory

4. If you need to handle the Lookup table. Find the right .txt file and change values.
   
   SetMinandMax(a,b) // in ~_conversion.txt , a is min , b is max
   

------------------

Made by Sungmin LEE , Bachelor course Research Assistant , Gachon Uni.
