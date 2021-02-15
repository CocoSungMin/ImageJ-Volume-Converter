import os,sys , getopt
import fileinput

def main(argv):
   SourcePath = ""
   OutputPath = ""
   ImageType = ""
   SourcePath_ch =""
   OutputPath_ch = ""
   codePath_ch = ""

   codePath = os.getcwd()
   try:
      opts , etc_args = getopt.getopt(argv[1:], "h:i:o:t:" ,["help","SourcePath=","OutputPath=","ImageType="] )

   except:
      print(argv[0],'-i <SourcePath> -o <OutputPath> -t <ResultImageType>')
      sys.exit(2)

   for opt , arg in opts:
      if opt in ("-h","--help"):
         print(argv[0] , "-s <SourcePath> -o <OutputPath> -t <ImageType>")
         sys.exit()
      elif opt in ("-i","--SourcePath") :
         SourcePath = arg
      elif opt in ("-o", "--OutputPath"):
         OutputPath = arg
      elif opt in ("-t","--ImageType"):
         ImageType = arg
   if len(SourcePath) < 1:
      print(argv[0] , "-i option is mandatory")
      sys.exit(2)
   elif len(OutputPath) <1:
      print(argv[0], "-o option is mandatory")
      sys.exit(2)
   elif len(ImageType) <1 :
      print(argv[0], "-t option is mandatory")
      sys.exit(2)
   else:
      print("SoucePath : ", SourcePath)
      print("OutputPath :" , OutputPath)
      print("codePath :" , codePath)
      ImageType = ImageType.upper()
      print("ImageFormat :" , ImageType)

      vols = os.listdir(SourcePath)
      vols_outcome = []
      if ImageType == 'PNG' :
         for line in fileinput.input(codePath+'/NRRD_PNG_convertion.txt',inplace=True):
            if 'path = "";' in line :
               line = line.replace(line, 'path = "' + codePath + '/listOutcome.txt";\n')
               codePath_ch = 'path = "' + codePath + '/listOutcome.txt";'
            elif 'SourcePath = "";' in line:
               line = line.replace(line , 'SourcePath = "'+SourcePath+'/";\n')
               SourcePath_ch = 'SourcePath = "'+SourcePath+'/";'
            elif 'outputPath = "";' in line:
               line = line.replace(line, 'outputPath = "' + OutputPath + '/";\n')
               OutputPath_ch = 'outputPath = "' + OutputPath + '/";'
            else:
               pass
            sys.stdout.write(line)

      elif ImageType =='JPEG' :
         for line in fileinput.input(codePath+'/NRRD_JPEG_convertion.txt',inplace=True) :
            if 'path = "";' in line :
               line = line.replace(line, 'path = "' + codePath + '/listOutcome.txt";\n')
               codePath_ch = 'path = "' + codePath + '/listOutcome.txt";'
            elif 'SourcePath = "";' in line:
               line = line.replace(line , 'SourcePath = "'+SourcePath+'/";\n')
               SourcePath_ch = 'SourcePath = "' + SourcePath + '/";'
            elif 'outputPath = "";' in line:
               line = line.replace(line, 'outputPath = "' + OutputPath + '/";\n')
               OutputPath_ch = 'outputPath = "' + OutputPath + '/";'
            else:
               pass
            sys.stdout.write(line)

      print("SoucePath : ", SourcePath_ch)
      print("OutputPath :", OutputPath_ch)
      print("codePath :", codePath_ch)
      ImageType = ImageType.upper()
      print("ImageFormat :", ImageType)

      os.system("mkdir "+OutputPath)

      for i in vols:
         if i == '.DS_Store':
            pass
         elif i == 'PNG_convertion':
            pass
         elif i == 'JPEG_convertion' :
            pass
         else:
            vols_outcome.append(i)
      outFile = open("listOutcome.txt","w")
      for i in vols_outcome:
         outFile.write(i+"\n")
      outFile.close()

      Readfile = open("listOutcome.txt","r")
      os.chdir(OutputPath)

      #make result file directory same as original volume name
      for i in Readfile:
         if i== '.DS_Store' : pass
         else : os.system("mkdir "+i)

      Readfile.close()

      #change the directory to user's ImageJ fiji installed directory
      if ImageType == 'PNG':
         os.system('/Applications/Fiji.app/Contents/MacOS/ImageJ-macosx --headless -macro '+codePath+'/NRRD_PNG_convertion.txt')
      elif ImageType == 'JPEG':
         os.system('/Applications/Fiji.app/Contents/MacOS/ImageJ-macosx --headless -macro ' + codePath + '/NRRD_JPEG_convertion.txt')

      if ImageType == 'PNG':
         for line in fileinput.input(codePath+'/NRRD_PNG_convertion.txt', inplace=True):
            if codePath_ch in line:
               line = line.replace(line, 'path = "";\n')
            elif SourcePath_ch in line:
               line = line.replace(line, 'SourcePath = "";\n')
            elif OutputPath_ch in line:
               line = line.replace(line, 'outputPath = "";\n')
            else : pass

            sys.stdout.write(line)

      elif ImageType == 'JPEG':
         for line in fileinput.input(codePath+'/NRRD_JPEG_convertion.txt', inplace=True):
            if codePath_ch in line:
               line = line.replace(line, 'path = "";\n')
            elif SourcePath_ch in line:
               line = line.replace(line, 'SourcePath = "";\n')
            elif OutputPath_ch in line:
               line = line.replace(line, 'outputPath = "";\n')
            else: pass
            sys.stdout.write(line)

if __name__ =="__main__":
   main(sys.argv)