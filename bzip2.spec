# 
# Conditional build:
# --without tetex - build without html documentation(don't request tetex)
#
Summary:	Extremely powerful file compression utility
Summary(fr):	Utilitaire de compression de fichier extrêmement puissant
Summary(pl):	Kompresor plików bzip2
Name:		bzip2
Version:	1.0.1
Release:	6
License:	GPL
Group:		Applications/Archiving
Group(de):	Applikationen/Archivierung
Group(fr):	Applications/Archivage
Group(pl):	Aplikacje/Archiwizacja
Source0:	ftp://sourceware.cygnus.com/pub/bzip2/v100/%{name}-%{version}.tar.gz
Patch0:		%{name}-libtoolizeautoconf.patch
%{!?_without_tetex:BuildRequires:        tetex}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
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
Group(de):	Entwicklung/Libraries
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
Group(de):	Entwicklung/Libraries
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
aclocal
libtoolize --copy --force
automake -a -c
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

# Substitute %{_bindir} in bzless.
mv -f $RPM_BUILD_ROOT%{_bindir}/bzless{,.tmp}
sed -e "s@%%{_bindir}@%{_bindir}@g" \
	$RPM_BUILD_ROOT%{_bindir}/bzless.tmp > \
	$RPM_BUILD_ROOT%{_bindir}/bzless
rm -f $RPM_BUILD_ROOT%{_bindir}/bzless.tmp

%{!?_without_tetex: ( cd doc ; texi2html bzip2.texi )}

gzip -9nf README* NEWS Y2K_INFO

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz Y2K_INFO.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_bindir}/*
%lang(en) %{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%files devel
%defattr(644,root,root,755)
%{!?_without_tetex: %doc doc/*.html}
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
