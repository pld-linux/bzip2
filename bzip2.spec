Summary:   Extremely powerful file compression utility
Name:      bzip2
Version:   0.1pl2
Release:   3
Copyright: GPL
Group:     Utilities/Archiving
Source:    http://www.digistar.com/bzip2/%{name}-%{version}.tar.gz
BuildRoot: /tmp/%{name}-%{version}-root

%description
Bzip2  compresses  files  using the Burrows-Wheeler block-sorting text
compression algorithm, and Huffman coding. Compression is generally
considerably better than that achieved by more conventional LZ77/LZ78-based
compressors, and approaches the performance of the PPM family of statistical
compressors.

The command-line options are deliberately very similar to those of GNU Gzip,
but they are not identical.

%prep
%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1}
install -s bzip2 bzip2recover $RPM_BUILD_ROOT/usr/bin

ln -sf bzip2 $RPM_BUILD_ROOT/usr/bin/bunzip2

install bzip2.1 $RPM_BUILD_ROOT/usr/man/man1
echo ".so bzip2.1" > $RPM_BUILD_ROOT/usr/man/man1/bunzip2.1

cat > $RPM_BUILD_ROOT/usr/bin/bzless <<EOF
#!/bin/sh
/usr/bin/bunzip2 -c "\$@" | /usr/bin/less
EOF

%files
%attr(644, root, root, 755) %doc  README ALGORITHMS
%attr(755, root root) /usr/bin/*
%attr(644, root  man) /usr/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Aug 13 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.1pl2-3]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- bunzip2(1) man page is now maked as nroff include to bzip(1) instead
  making sym link to bzip2.1 (this allow compress man pages in future),
- added %attr and %defattr macros in %files (allow build package from
  non-root account).
