Summary:	Extremely powerful file compression utility
Summary(pl):	Kompresor plików bzip2
Name:		bzip2
Version:	0.9.0c
Release:	2
Copyright:	GPL
Group:		Utilities/Archiving
Group(pl):	Narzêdzia/Archiwizacja
URL:		http://www.digistar.com/bzip2
Source:		%{name}-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Bzip2  compresses  files  using the Burrows-Wheeler block-sorting text
compression algorithm, and Huffman coding. Compression is generally
considerably better than that achieved by more conventional LZ77/LZ78-based
compressors, and approaches the performance of the PPM family of statistical
compressors.

The command-line options are deliberately very similar to those of GNU Gzip,
but they are not identical.

%description -l pl
Kompresor bzip2 u¿ywa algorytmu Burrows-Wheelera do kompresji danych i metody 
Huffmana do ich kodowania. Kompresja pliku czy archiwum tar jest z regu³y 
lepsza ni¿ w przypadku stosowania klasycznych kompresorów LZ77/LZ78. 
Opcje linii poleceñ s± bardzo podobne do poleceñ GNU Gzip ale nie s± 
identyczne.

%prep
%setup -q 

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/{bin,lib,man/man1}

install -s {bzip2,bzip2recover} $RPM_BUILD_ROOT/usr/bin
install *.a $RPM_BUILD_ROOT/usr/lib

ln -sf bzip2 $RPM_BUILD_ROOT/usr/bin/bunzip2
ln -sf bzip2 $RPM_BUILD_ROOT/usr/bin/bzcat

install bzip2.1 $RPM_BUILD_ROOT/usr/man/man1

echo .so bzip2.1 > $RPM_BUILD_ROOT/usr/man/man1/bunzip2.1
echo .so bzip2.1 > $RPM_BUILD_ROOT/usr/man/man1/bzcat.1
echo .so bzip2.1 > $RPM_BUILD_ROOT/usr/man/man1/bzip2recover.1

cat > $RPM_BUILD_ROOT/usr/bin/bzless <<EOF
#!/bin/sh
/usr/bin/bunzip2 -c "\$@" | /usr/bin/less
EOF

bzip2 -9  README
gzip -9fn $RPM_BUILD_ROOT/usr/man/man1/*

%files
%defattr(644,root,root,755)
%doc README.bz2 *.html

%attr(755,root,root) /usr/bin/*
%attr(644,root, man) /usr/man/man1/*

/usr/lib/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Jan 15 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.9.0c-1d]
- added Group(pl),
- added static bzip2 library,
- added symlink bzcat,
- fixed man pages,
- compressed %doc with bzip2 (bzip2 must be instaled in system ;) 

* Mon Oct 05 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.9.0-1d]
- updated to 0.9.0b. 

* Thu Sep 24 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.1pl2-2d]
- translation modified for pl,
- install -d instead mkdir -p,
- added %defattr support,
- fixed files permissions,
- minor modifications of the spec file.

* Mon Jul 20 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.1pl2-2]
- build against GNU libc-2.1.
