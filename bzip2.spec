Summary:	Extremely powerful file compression utility
Summary(fr):	Utilitaire de compression de fichier extr�mement puissant
Summary(pl):	Kompresor plik�w bzip2
Name:		bzip2
Version:	1.0.2
Release:	1
License:	BSD-like
Group:		Applications/Archiving
Group(de):	Applikationen/Archivierung
Group(fr):	Applications/Archivage
Group(pl):	Aplikacje/Archiwizacja
Source0:	ftp://sourceware.cygnus.com/pub/bzip2/v102/%{name}-%{version}.tar.gz
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-libtoolizeautoconf.patch
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
compression est consid�rablement meilleure que celle effectu�e par les
plus conventionels compresseurs bas�s sur LZ77/LZ78, et approche la
performance de la famille PPM de compresseurs statistiques.

%description -l pl
Kompresor bzip2 u�ywa algorytmu Burrows-Wheelera do kompresji danych i
metody Huffmana do ich kodowania. Kompresja pliku czy archiwum tar
jest z regu�y lepsza ni� w przypadku stosowania klasycznych
kompresor�w LZ77/LZ78. Opcje linii polece� s� bardzo podobne do
polece� GNU Gzip ale nie s� identyczne.

%package devel
Summary:	Libbz2 library header files
Summary(fr):	Librairie statique et fichiers d'en-t�te pour bzip2
Summary(pl):	Pliki nag��wkowe do libbz2
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name} = %{version}

%description devel
Libbz2 library header files.

%description -l pl devel
Pliki nag��wkowe do libbz2.

%package static
Summary:	Static libbz2 library
Summary(pl):	Biblioteka statyczna libbz2
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
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

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

gzip -9nf README* NEWS Y2K_INFO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.gz Y2K_INFO.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_bindir}/*
%lang(en) %{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(ko) %{_mandir}/ko/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
