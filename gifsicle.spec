Summary:	Powerful program for manipulating GIF images and animations
Name:		gifsicle
Version:	1.45
Release:	1
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://www.lcdf.org/gifsicle/%{name}-%{version}.tar.gz
# Source0-md5:	08b0055ed616c9bcdf707057ea29dbfb
URL:		http://www.lcdf.org/gifsicle/
BuildRequires:	giflib-devel
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

%prep
%setup -q

%build
%configure \
	--enable-ungif
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/gifdiff
%attr(755,root,root) %{_bindir}/gifsicle
%attr(755,root,root) %{_bindir}/gifview
%{_mandir}/man1/gifdiff.1*
%{_mandir}/man1/gifsicle.1*
%{_mandir}/man1/gifview.1*
