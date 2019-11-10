import shutil, os, re

# Create a Regex that matches files with the American date format

date_pattern = re.compile(r"""^(.*?) # all text before the date
       ((0|1)?\d)-                     # one or two digits for the month
       ((0|1|2|3)?\d)-                 # one or two digits for the day
       ((19|20)\d\d)                   # four digits for the year
       (.*?)$                          # all text after the date)
        """, re.VERBOSE)

for amerFilename in os.listdir('.'):
    mo = date_pattern.search(amerFilename)
    if mo == None:
       continue
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)


    datePattern = re.compile(r"""^(1) # all text before the date
    (2 (3) )-                     # one or two digits for the month
    (4 (5) )-                     # one or two digits for the day
    (6 (7) )                      # four digits for the year
    (8)$                          # all text after the date
    """, re.VERBOSE)

    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    #shutil.move(amerFilename, euroFilename)