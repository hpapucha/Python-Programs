
def frame_score(the_frame, bonus1, bonus2):
    if the_frame[0] == 10:
        return bonus1 + bonus2 + 10
    elif the_frame[0] + the_frame[1] == 10:
        return bonus1 + 10
    elif the_frame[0] != 10 and the_frame[0] + the_frame[1] !=10:
        return the_frame[0] + the_frame[1]
    
# Define method to read a ragged array
def read_ragged_array(the_filename):
  
    # Initialize ragged array
    ragged_array = [ ]

    # Open input file and read first line
    f = open(the_filename, "r")
    line = f.readline( )
  
    # Keep processing lines until end of file is reached.
    while line:
        fields = line.split(" ")
        row = [ ]
      
        # Append each field item to the row array
        for field in fields:
            row.append(int(field.strip( )))
      
        # When finished constructing row, append
        # to ragged_array.
        ragged_array.append(row)

        # Read next line
        line = f.readline( )
