Summary:	Extremely powerful file compression utility
Summary(pl):	Kompresor plików bzip2
Name:		bzip2
Version:	0.9.0c
Release:	2
Copyright:	GPL
Group:		Utilities/Archiving
Group(pl):	Narzêdzia/Archiwizacja
Source:		http://www.digistar.com/bzip2/%{name}-%{version}.tar.gz
Patch:		bzip2-shlib.patch
URL:		http://www.muraroa.demon.co.uk/
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

%package devel
Summary:	Libbz2 library header files
Summary(pl):	Pliki nag³ówkowe do libbz2
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Libbz2 library header files

%description -l pl devel
Pliki nag³ówkowe do libbz2.

%package static
Summary:	Static libbz2 library
Summary(pl):	Biblioteka statyczna libbz2
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libbz2 library.

%description -l pl static
Biblioteka statyczna libbz2.

%prep
%setup -q 
%patch -p1

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,lib,include,man/man1}

install -s {bzip2,bzip2recover} $RPM_BUILD_ROOT/usr/bin

ln -sf bzip2 $RPM_BUILD_ROOT/usr/bin/bunzip2
ln -sf bzip2 $RPM_BUILD_ROOT/usr/bin/bzcat

install bzip2.1 $RPM_BUILD_ROOT/usr/man/man1
install bzlib.h $RPM_BUILD_ROOT/usr/include

echo .so bzip2.1 > $RPM_BUILD_ROOT/usr/man/man1/bunzip2.1
echo .so bzip2.1 > $RPM_BUILD_ROOT/usr/man/man1/bzcat.1
echo .so bzip2.1 > $RPM_BUILD_ROOT/usr/man/man1/bzip2recover.1

cat > $RPM_BUILD_ROOT/usr/bin/bzless <<EOF
#!/bin/sh
/usr/bin/bunzip2 -c "\$@" | /usr/bin/less
EOF

install lib*so.*.* lib*.a $RPM_BUILD_ROOT/usr/lib
ln -sf libbz2.so.0.9.0 $RPM_BUILD_ROOT/usr/lib/libbz2.so
strip --strip-unneeded $RPM_BUILD_ROOT/usr/lib/lib*so.*.*

gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) /usr/lib/lib*.so.*.*
%attr(755,root,root) /usr/bin/*
%attr(644,root,root) /usr/man/man1/*

%files devel
%defattr(644,root,root,755)
%doc *.html
%attr(755,root,root) /usr/lib/lib*.so
/usr/include/*.h

%files static
%attr(644,root,root) /usr/lib/lib*.a

%changelog
* Sun Mar 14 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.9.0c-2]
- added build a shared libbz2.so,
- added devel and static subpackage,
- gzipping man pages instead bzipping2,
- removed man group from man pages.

* Fri Jan 15 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.9.0c-1d]
- added Group(pl),
- added static bzip2 library,
- added symlink bzcat,
- fixed man pages,
- compressed man pages with bzip2 (bzip2 must by instaled in system ;)

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
- build against glibc-2.1.
