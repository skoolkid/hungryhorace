#!/usr/bin/env python3
import sys
import os

SKOOLKIT_HOME = os.environ.get('SKOOLKIT_HOME')
if not SKOOLKIT_HOME:
    sys.stderr.write('SKOOLKIT_HOME is not set; aborting\n')
    sys.exit(1)
if not os.path.isdir(SKOOLKIT_HOME):
    sys.stderr.write('SKOOLKIT_HOME={}: directory not found\n'.format(SKOOLKIT_HOME))
    sys.exit(1)
sys.path.insert(0, '{}/tools'.format(SKOOLKIT_HOME))
from testwriter import write_tests

SKOOL = '../sources/hh.skool'

SNAPSHOT = '../build/hungry_horace.z80'

OUTPUT = """Using skool file: {skoolfile}
Using ref files: ../sources/hh.ref, ../sources/changelog.ref, ../sources/facts.ref, ../sources/pokes.ref
Parsing {skoolfile}
Creating directory {odir}/hungry_horace
Copying {SKOOLKIT_HOME}/skoolkit/resources/skoolkit.css to {odir}/hungry_horace/skoolkit.css
  Writing disassembly files in hungry_horace/asm
  Writing hungry_horace/maps/all.html
  Writing hungry_horace/maps/routines.html
  Writing hungry_horace/maps/data.html
  Writing hungry_horace/maps/messages.html
  Writing hungry_horace/maps/unused.html
  Writing hungry_horace/buffers/gbuffer.html
  Writing hungry_horace/reference/changelog.html
  Writing hungry_horace/reference/facts.html
  Writing hungry_horace/reference/pokes.html
  Writing hungry_horace/index.html"""

write_tests(SKOOL, SNAPSHOT, OUTPUT, clean=False)
