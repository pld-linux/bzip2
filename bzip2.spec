Summary:	Extremely powerful file compression utility
Summary(es):	Un compresor de archivos con un nuevo algoritmo
Summary(fr):	Utilitaire de compression de fichier extr�mement puissant
Summary(pl):	Kompresor plik�w bzip2
Summary(pt_BR):	Compactador de arquivo extremamente poderoso
Summary(uk):	��������� ���̦� �� ��ڦ ��������� �������� ����������
Summary(ru):	���������� ������ �� ������ ��������� ������� ����������
Name:		bzip2
Version:	1.0.2
Release:	12
Epoch:		0
License:	BSD-like
Group:		Applications/Archiving
Source0:	ftp://sources.redhat.com/pub/bzip2/v102/%{name}-%{version}.tar.gz
# Source0-md5:	ee76864958d568677f03db8afad92beb
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	5ffc3dbdd40080a8c22c3b4c3143cdd7
Patch0:		%{name}-libtoolizeautoconf.patch
URL:		http://sources.redhat.com/bzip2/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	tetex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bzip2 compresses files using the Burrows-Wheeler block-sorting text
compression algorithm, and Huffman coding. Compression is generally
considerably better than that achieved by more conventional
LZ77/LZ78-based compressors, and approaches the performance of the PPM
family of statistical compressors. The command-line options are
deliberately very similar to those of GNU Gzip, but they are not
identical.

%description -l es
Bzip2 es un programa de compresi�n/descompresi�n. T�picamente el
archivo compactado queda entre 20 la 30 por ciento menor de que se
fuera compactado con gzip. Observa que bzip2 no entiende los archivos
del bzip original, ni los archivos del gzip.

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

%description -l pt_BR
Bzip2 � um programa de compress�o/descompress�o. Tipicamente o arquivo
compactado fica 20 a 30 por cento menor do que se fosse compactado com
o gzip.

Note que o bzip2 n�o entende os arquivos do bzip original, nem os
arquivos do gzip.

%description -l ru
bzip2 ������������� ����� ��������� ��������������� ��������� ��������
������� ���������� Burrows-Wheeler � ����������� Huffman'�.
����������� ���������� ������ ����������� ����� ����������� �����
���������� ������������� �� ������ LZ77/LZ78 � ������������ � ���,
������� ������������ ��������� �������������� ������������ PPM.

%description -l uk
bzip2 �������դ ����� �������������� ��������� �������� ��������
���������� Burrows-Wheeler �� ��������� Huffman'�. ������Ӧ�, ���
����������� bzip2, �� ������� ����� �� ��, �� ������������
�����������Φ ���������� �� ��ڦ LZ77/LZ78 � ������������ �� �ϧ, ��
�� ��������դ Ӧ������� ������������ ��������Ҧ� PPM.

%package devel
Summary:	libbz2 library header files
Summary(fr):	Fichiers d'en-t�te pour bzip2
Summary(pl):	Pliki nag��wkowe do libbz2
Summary(pt_BR):	Arquivos de inclus�o para o bzip2
Summary(uk):	������, ����Ȧ�Φ ��� ������������� � libbz2
Summary(ru):	������, ����������� ��� ���������������� � libbz2
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	libbzip2-devel

%description devel
Libbz2 library header files.

%description devel -l pl
Pliki nag��wkowe do libbz2.

%description devel -l pt_BR
Este pacote inclui arquivos de inclus�o necess�rio para o
desenvolvimento de programas que usam o bzip2.

%description devel -l ru
���� ����� �������� ���������� � ������, ����������� ��� ����������
��������, ���������� ������������ ����������/������������ bz2.

%description devel -l uk
��� ����� ͦ����� ¦�̦����� �� ������, ����Ȧ�Φ ��� ��������
�������, �˦ ��������� Ц��������� ������Ӧ�/��������Ӧ� bz2.

%package libs
Summary:	libbz2 library
Summary(fr):	Librairie libbz2
Summary(pl):	Biblioteka libbz2
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
%ifarch amd64 ia64 ppc64 sparc64
Provides:	libbz2.so.1.0()(64bit)
%else
Provides:	libbz2.so.1.0
%endif
Obsoletes:	libbzip2
Conflicts:	%{name} < 0:1.0.2-12

%description libs
libbz2 library.

%description libs -l fr
Librairie libbz2.

%description libs -l pl
Biblioteka libbz2.

%package static
Summary:	Static libbz2 library
Summary(fr):	Librairie statique libbz2
Summary(pl):	Biblioteka statyczna libbz2
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com a bzip2
Summary(ru):	����������� ���������� bzip2
Summary(uk):	������Φ ¦�̦����� bzip2
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%define		specflags_ia32	-fomit-frame-pointer

%description static
Static libbz2 library.

%description libs -l fr
Librairie statique d'en-t�te pour bzip2.

%description static -l pl
Biblioteka statyczna libbz2.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com a bzip2.

%description static -l uk
�� ������� ����� ڦ ���������� ¦�̦�������.

%description static -l ru
��� ��������� ����� �� ������������ ������������.

%prep
%setup -q
%patch -p1

%build
%{__aclocal}
%{__libtoolize}
%{__automake}
%{__autoconf}
%configure
%{__make}
cd doc
/usr/bin/texi2html bzip2.texi
cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Substitute %{_bindir} in bzless.
mv -f $RPM_BUILD_ROOT%{_bindir}/bzless{,.tmp}
sed -e "s@%%{_bindir}@%{_bindir}@g" \
	$RPM_BUILD_ROOT%{_bindir}/bzless.tmp > \
	$RPM_BUILD_ROOT%{_bindir}/bzless
rm -f $RPM_BUILD_ROOT%{_bindir}/bzless.tmp

# standard soname was libbz2.so.1.0, libtoolizeautoconf patch broke it,
# but ABI has not changed - provide symlink for binary compatibility
ln -sf libbz2.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}/libbz2.so.1.0

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post libs	-p /sbin/ldconfig
%postun libs	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README* NEWS Y2K_INFO doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(ko) %{_mandir}/ko/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/lib*.so.1.0

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
