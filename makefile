SCRIPT=Quintero-Smith.py
REQUIRES=psutil_installed
INPUT=input.txt #default input file, can be overriden with INPUT=<filename> as command argument
THOU=1000base.txt
TENTHOU=10000base.txt
HUNDREDTHOU=100000base.txt

default: $(REQUIRES)
	python $(SCRIPT) $(INPUT)

1000: $(REQUIRES)
	python $(SCRIPT) $(THOU)

10000: $(REQUIRES)
	python $(SCRIPT) $(TENTHOU)

100000: $(REQUIRES)
	python $(SCRIPT) $(HUNDREDTHOU)

psutil_installed:
	pip install psutil

clean:
	rm -f *.o?
