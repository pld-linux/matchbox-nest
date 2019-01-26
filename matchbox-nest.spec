Summary:	Graphical wrapper around Xnest
Summary(pl.UTF-8):	Graficzny wrapper na Xnest
Name:		matchbox-nest
Version:	0.3
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.yoctoproject.org/releases/matchbox/matchbox-nest/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	f8d469a8e1d3a054dff58a6c81497c39
Patch0:		%{name}-path.patch
URL:		https://www.yoctoproject.org/software-item/matchbox/
BuildRequires:	expat-devel >= 1.95
BuildRequires:	libmatchbox-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXtst-devel
Requires:	xorg-xserver-Xnest
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
matchbox-nest is a graphical wrapper around Xnest. You can make Xnest
look like a particular device's display and set up buttons on that
device.

%description -l pl.UTF-8
matchbox-nest to graficzny wrapper na Xnest. Można sprawić, by Xnest
wyglądał jak wyświetlacz określonego urządzenia i skonfigurować
przyciski na tym urządzeniu.

%prep
%setup -q
%patch0 -p1

%build
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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/matchbox-nest
%{_datadir}/matchbox-nest
