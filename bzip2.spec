Summary:	Extremely powerful file compression utility
Summary(fr):	Utilitaire de compression de fichier extrêmement puissant
Summary(pl):	Kompresor plików bzip2
Name:		bzip2
Version:	1.0.0
Release:	2
License:	GPL
Group:		Utilities/Archiving
Group(fr):	Applications/Archivage
Group(pl):	Narzêdzia/Archiwizacja
Source0:	ftp://sourceware.cygnus.com/pub/bzip2/v100/%{name}-%{version}.tar.gz
Patch0:		bzip2-shlib.patch
URL:		http://sourceware.cygnus.com/bzip2/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bzip2 compresses files using the Burrows-Wheeler block-sorting text
compression algorithm, and Huffman coding. Compression is generally
considerably better than that achieved by more conventional
LZ77/LZ78-based compressors, and approaches the performance of the PPM
family of statistical compressors. The command-line options are
deliberately very similar to those of GNU Gzip, but they are not
identical.

%description -l fr
Bzip2 compresse des fichiers en utilisant l'algorithme de compression
en tri de blocks de texte Burrows-Wheeler, et le codage Huffman. La
compression est considérablement meilleure que celle effectuée par les
plus conventionels compresseurs basés sur LZ77/LZ78, et approche la
performance de la famille PPM de compresseurs statistiques.

%description -l pl
Kompresor bzip2 u¿ywa algorytmu Burrows-Wheelera do kompresji danych i
metody Huffmana do ich kodowania. Kompresja pliku czy archiwum tar
jest z regu³y lepsza ni¿ w przypadku stosowania klasycznych
kompresorów LZ77/LZ78. Opcje linii poleceñ s± bardzo podobne do
poleceñ GNU Gzip ale nie s± identyczne.

%package devel
Summary:	Libbz2 library header files
Summary(fr):	Librairie statique et fichiers d'en-tête pour bzip2
Summary(pl):	Pliki nag³ówkowe do libbz2
Group:		Development/Libraries
Group(fr):	Development/Librairies
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
Group(fr):	Development/Librairies
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
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir},%{_includedir},%{_mandir}/man1}

install -s {bzip2,bzip2recover} $RPM_BUILD_ROOT%{_bindir}

ln -sf bzip2 $RPM_BUILD_ROOT%{_bindir}/bunzip2
ln -sf bzip2 $RPM_BUILD_ROOT%{_bindir}/bzcat

install bzip2.1 $RPM_BUILD_ROOT%{_mandir}/man1
install bzlib.h $RPM_BUILD_ROOT%{_includedir}

echo .so bzip2.1 > $RPM_BUILD_ROOT%{_mandir}/man1/bunzip2.1
echo .so bzip2.1 > $RPM_BUILD_ROOT%{_mandir}/man1/bzcat.1
echo .so bzip2.1 > $RPM_BUILD_ROOT%{_mandir}/man1/bzip2recover.1

cat > $RPM_BUILD_ROOT%{_bindir}/bzless <<EOF
#!/bin/sh
%{_bindir}/bunzip2 -c "\$@" | /usr/bin/less
EOF

install lib*so.*.* lib*.a $RPM_BUILD_ROOT%{_libdir}
ln -sf libbz2.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}/libbz2.so

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*so.*.*

gzip -9nf README CHANGES Y2K_INFO $RPM_BUILD_ROOT%{_mandir}/man1/*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.gz README.gz Y2K_INFO.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc manual*html 
%doc *.html
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
