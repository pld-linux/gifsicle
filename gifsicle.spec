Summary:	Powerful program for manipulating GIF images and animations
Summary(pl.UTF-8):	Potężny program do obróbki obrazków i animacji GIF
Name:		gifsicle
Version:	1.84
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://www.lcdf.org/gifsicle/%{name}-%{version}.tar.gz
# Source0-md5:	21cb0d75db42e664bee77b77e8f40f50
Patch0:		%{name}-link.patch
URL:		http://www.lcdf.org/gifsicle/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	rpm >= 4.4.9-56
%if "%{pld_release}" == "ac"
BuildRequires:	XFree86-devel
%else
BuildRequires:	xorg-lib-libX11-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gifsicle manipulates GIF image files on the command line. It supports
merging several GIFs into a GIF animation; exploding an animation into
its component frames; changing individual frames in an animation;
turning interlacing on and off; adding transparency; adding delays,
disposals, and looping to animations; adding or removing comments;
optimizing animations for space; and changing images' colormaps, among
other things.

The gifsicle package contains two other programs: gifview, a
lightweight GIF viewer for X, can show animations as slideshows or in
real time, and gifdiff compares two GIFs for identical visual
appearance.

%description -l pl.UTF-8
gifsicle obrabia pliki obrazów GIF z linii poleceń. Obsługuje łączenie
kilku GIF-ów w animację GIF, rozbijanie animacji na klatki składowe,
zmianę poszczególnych klatek w animacji, włączanie i wyłączanie
interlace'u, dodawanie przezroczystości, dodawanie opóźnień,
dyspozycji i pętli do animacji, dodawanie i usuwanie komentarzy,
optymalizację animacji pod kątem rozmiaru oraz zmieny palety kolorów w
obrazach.

Pakiet gifsicle zawiera dwa dodatkowe programy: gifview (lekką
przeglądarkę GIF-ów dla X, potrafiącą pokazywać animacje jako pokazy
slajdów lub w czasie rzeczywistym) oraz gifdiff (porównujący dwa GIF-y
pod kątem identycznego wyglądu).

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/gifdiff
%attr(755,root,root) %{_bindir}/gifsicle
%attr(755,root,root) %{_bindir}/gifview
%{_mandir}/man1/gifdiff.1*
%{_mandir}/man1/gifsicle.1*
%{_mandir}/man1/gifview.1*
