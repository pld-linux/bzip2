# 
# Conditional build:
%bcond_with	progress	# with progressbar patch
%bcond_without	doc		# don't build tex documentation
#
Summary:	Extremely powerful file compression utility
Summary(es.UTF-8):   Un compresor de archivos con un nuevo algoritmo
Summary(fr.UTF-8):   Utilitaire de compression de fichier extrêmement puissant
Summary(pl.UTF-8):   Kompresor plików bzip2
Summary(pt_BR.UTF-8):   Compactador de arquivo extremamente poderoso
Summary(uk.UTF-8):   Компресор файлів на базі алгоритму блочного сортування
Summary(ru.UTF-8):   Компрессор файлов на основе алгоритма блочной сортировки
Name:		bzip2
Version:	1.0.4
Release:	1
Epoch:		0
License:	BSD-like
Group:		Applications/Archiving
Source0:	http://www.bzip.org/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fc310b254f6ba5fbb5da018f04533688
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	5ffc3dbdd40080a8c22c3b4c3143cdd7
Patch0:		%{name}-libtoolizeautoconf.patch
Patch1:		%{name}-bzgrep.patch
# Modified from http://www.vanheusden.com/Linux/bzip2-1.0.2.diff.gz
Patch2:		%{name}-progress-counter-1.0.2.patch
URL:		http://www.bzip.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.213
%{?with_doc:BuildRequires:	tetex}
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	-fomit-frame-pointer

%description
Bzip2 compresses files using the Burrows-Wheeler block-sorting text
compression algorithm, and Huffman coding. Compression is generally
considerably better than that achieved by more conventional
LZ77/LZ78-based compressors, and approaches the performance of the PPM
family of statistical compressors. The command-line options are
deliberately very similar to those of GNU Gzip, but they are not
identical.

%description -l es.UTF-8
Bzip2 es un programa de compresión/descompresión. Típicamente el
archivo compactado queda entre 20 la 30 por ciento menor de que se
fuera compactado con gzip. Observa que bzip2 no entiende los archivos
del bzip original, ni los archivos del gzip.

%description -l fr.UTF-8
Bzip2 compresse des fichiers en utilisant l'algorithme de compression
en tri de blocks de texte Burrows-Wheeler, et le codage Huffman. La
compression est considérablement meilleure que celle effectuée par les
plus conventionels compresseurs basés sur LZ77/LZ78, et approche la
performance de la famille PPM de compresseurs statistiques.

%description -l pl.UTF-8
Kompresor bzip2 używa algorytmu Burrows-Wheelera do kompresji danych i
metody Huffmana do ich kodowania. Kompresja pliku czy archiwum tar
jest z reguły lepsza niż w przypadku stosowania klasycznych
kompresorów LZ77/LZ78. Opcje linii poleceń są bardzo podobne do
poleceń GNU Gzip ale nie są identyczne.

%description -l pt_BR.UTF-8
Bzip2 é um programa de compressão/descompressão. Tipicamente o arquivo
compactado fica 20 a 30 por cento menor do que se fosse compactado com
o gzip.

Note que o bzip2 não entende os arquivos do bzip original, nem os
arquivos do gzip.

%description -l ru.UTF-8
bzip2 компрессирует файлы используя компрессирующий текстовый алгоритм
блочной сортировки Burrows-Wheeler и кодирование Huffman'а.
Достигаемая компрессия обычно существенно лучше достигаемой более
привычными компрессорами на основе LZ77/LZ78 и приближается к той,
которую обеспечивает семейство статистических компрессоров PPM.

%description -l uk.UTF-8
bzip2 компресує файли використовуючи текстовий алгоритм блочного
сортування Burrows-Wheeler та кодування Huffman'а. Компресія, яка
досягається bzip2, як правило краща за ту, що забезпечують
розповсюджені компресори на базі LZ77/LZ78 і наближається до тої, що
її забезпечує сімейство статистичних компресорів PPM.

%package libs
Summary:	libbz2 library
Summary(fr.UTF-8):   Librairie libbz2
Summary(pl.UTF-8):   Biblioteka libbz2
Group:		Libraries
%ifarch %{x8664} ia64 ppc64 s390x sparc64
Provides:	libbz2.so.1.0()(64bit)
%else
Provides:	libbz2.so.1.0
%endif
Obsoletes:	libbzip2
Conflicts:	bzip2 < 0:1.0.2-12

%description libs
libbz2 library.

%description libs -l fr.UTF-8
Librairie libbz2.

%description libs -l pl.UTF-8
Biblioteka libbz2.

%package devel
Summary:	libbz2 library header files
Summary(fr.UTF-8):   Fichiers d'en-tête pour bzip2
Summary(pl.UTF-8):   Pliki nagłówkowe do libbz2
Summary(pt_BR.UTF-8):   Arquivos de inclusão para o bzip2
Summary(uk.UTF-8):   Хедери, необхідні для програмування з libbz2
Summary(ru.UTF-8):   Хедеры, необходимые для программирования с libbz2
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	libbzip2-devel

%description devel
Libbz2 library header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe do libbz2.

%description devel -l pt_BR.UTF-8
Este pacote inclui arquivos de inclusão necessário para o
desenvolvimento de programas que usam o bzip2.

%description devel -l ru.UTF-8
Этот пакет содержит библиотеку и хедеры, необходимые для разработки
программ, включающих подпрограммы компрессии/декомпрессии bz2.

%description devel -l uk.UTF-8
Цей пакет містить бібліотеку та хедери, необхідні для розробки
програм, які включають підпрограми компресії/декомпресії bz2.

%package static
Summary:	Static libbz2 library
Summary(fr.UTF-8):   Librairie statique libbz2
Summary(pl.UTF-8):   Biblioteka statyczna libbz2
Summary(pt_BR.UTF-8):   Bibliotecas estáticas para desenvolvimento com a bzip2
Summary(ru.UTF-8):   Статические библиотеки bzip2
Summary(uk.UTF-8):   Статичні бібліотеки bzip2
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libbz2 library.

%description static -l fr.UTF-8
Librairie statique d'en-tête pour bzip2.

%description static -l pl.UTF-8
Biblioteka statyczna libbz2.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com a bzip2.

%description static -l uk.UTF-8
Це окремий пакет зі статичними бібліотеками.

%description static -l ru.UTF-8
Это отдельный пакет со статическими библиотеками.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%{?with_progress:%patch2 -p1}

%build
%{__aclocal}
%{__libtoolize}
%{__automake}
%{__autoconf}
%configure \
	CFLAGS="%{rpmcflags} -D_FILE_OFFSET_BITS=64"
%{__make}

%if %{with doc}
cd doc
/usr/bin/texi2html bzip2.texi
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_lib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Substitute %{_bindir} in bzless.
mv -f $RPM_BUILD_ROOT%{_bindir}/bzless{,.tmp}
sed -e "s@%%{_bindir}@%{_bindir}@g" \
	$RPM_BUILD_ROOT%{_bindir}/bzless.tmp > \
	$RPM_BUILD_ROOT%{_bindir}/bzless
rm -f $RPM_BUILD_ROOT%{_bindir}/bzless.tmp

mv -f $RPM_BUILD_ROOT%{_libdir}/libbz2.so.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/libbz2.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/libbz2.so

# standard soname was libbz2.so.1.0, libtoolizeautoconf patch broke it,
# but ABI has not changed - provide symlink for binary compatibility
ln -sf libbz2.so.1.0.0 $RPM_BUILD_ROOT/%{_lib}/libbz2.so.1.0

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README* %{?with_doc:doc/*.html}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(ko) %{_mandir}/ko/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/lib*.so.*.*.*
%attr(755,root,root) /%{_lib}/lib*.so.1.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
