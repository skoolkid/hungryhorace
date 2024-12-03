Hungry Horace disassembly
=========================

A disassembly of the [Spectrum](https://en.wikipedia.org/wiki/ZX_Spectrum)
version of
[Hungry Horace](https://en.wikipedia.org/wiki/Horace_series#Hungry_Horace),
created using [SkoolKit](https://skoolkit.ca).

Decide which number base you prefer and then click the corresponding link below
to browse the latest release:

* [Hungry Horace disassembly](https://skoolkid.github.io/hungryhorace/) (hexadecimal)
* [Hungry Horace disassembly](https://skoolkid.github.io/hungryhorace/dec/) (decimal)

To build the current development version of the disassembly, first obtain the
development version of [SkoolKit](https://github.com/skoolkid/skoolkit). Then:

    $ skool2html.py sources/hh.skool

To build an assembly language source file that can be fed to an assembler:

    $ skool2asm.py sources/hh.skool > hh.asm
