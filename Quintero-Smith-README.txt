To run our program, use the makefile:

$ make INPUT=<inputfilename>

you can also use

$ make 1000
$ make 10000
$ make 100000

to run the script with 1000base.txt, 10000base.txt, and 100000base.txt as input files, respectively.

To cleanup output files, you can use
$ make clean


To run the script manually, make sure the python module psutils is installed and run the following command:
python Quintero-Smith-optimal-aligner.py [input file]
