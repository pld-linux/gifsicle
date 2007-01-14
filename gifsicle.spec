Summary:	Powerful program for manipulating GIF images and animations
Summary(pl):	Potê¿ny program do obróbki obrazków i animacji GIF
Name:		gifsicle
Version:	1.46
Release:	1
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://www.lcdf.org/gifsicle/%{name}-%{version}.tar.gz
# Source0-md5:	e23ba8f4e2549e544bbe714e3f0c6e26
Patch0:		%{name}-link.patch
URL:		http://www.lcdf.org/gifsicle/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	xorg-lib-libX11-devel
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

%description -l pl
gifsicle obrabia pliki obrazów GIF z linii poleceñ. Obs³uguje ³±czenie
kilku GIF-ów w animacjê GIF, rozbijanie animacji na klatki sk³adowe,
zmianê poszczególnych klatek w animacji, w³±czanie i wy³±czanie
interlace'u, dodawanie przezroczysto¶ci, dodawanie opó¼nieñ,
dyspozycji i pêtli do animacji, dodawanie i usuwanie komentarzy,
optymalizacjê animacji pod k±tem rozmiaru oraz zmieny palety kolorów
w obrazach.

Pakiet gifsicle zawiera dwa dodatkowe programy: gifview (lekk±
przegl±darkê GIF-ów dla X, potrafi±c± pokazywaæ animacje jako pokazy
slajdów lub w czasie rzeczywistym) oraz gifdiff (porównuj±cy dwa GIF-y
pod k±tem identycznego wygl±du).

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
%doc ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gifdiff
%attr(755,root,root) %{_bindir}/gifsicle
%attr(755,root,root) %{_bindir}/gifview
%{_mandir}/man1/gifdiff.1*
%{_mandir}/man1/gifsicle.1*
%{_mandir}/man1/gifview.1*
