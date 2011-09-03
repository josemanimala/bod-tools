import os
import re
path = '/home/jose/wiki_data/pages/'
listing = os.listdir(path)
def group_by_heading1( some_source ):
    buffer= []
    for line in some_source:
        if line.startswith( "===== Software Homepage =====" ):
            if buffer: yield buffer
            buffer= [ line ]
        else:
            buffer.append( line )
    yield buffer

def group_by_heading2( some_source ):
    buffer= []
    for line in some_source:
        if line.startswith( "===== Related / Similar Applications =====" ):
            if buffer: yield buffer
            buffer= [ line ]
        else:
            buffer.append( line )
    yield buffer

for infile in listing:
	if(os.path.isdir(path+infile)==False):
		with open( path+infile, "r" ) as source:
			fdata = open( path+infile, "r" )
			if re.search("===== Software Homepage =====", fdata.read()):
		    		for heading_and_lines in group_by_heading1( source ):
        				heading= heading_and_lines[0]
        				lines= heading_and_lines[1:]
				print lines
				source.seek(0)
				for heading_and_lines in group_by_heading2( source ):
        				heading= heading_and_lines[0]
        				lines= heading_and_lines[1:]
				print heading
				print lines
			
		
