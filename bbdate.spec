Summary:	bbdate - displays the current date
Summary(pl.UTF-8):	bbdate - wyświetlanie bieżącej daty
Name:		bbdate
Version:	0.2.4
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://bbtools.windsofstorm.net/sources/%{name}-%{version}.tar.gz
# Source0-md5:	c2813cb16a179f206303612585f3b00b
URL:		http://bbtools.windsofstorm.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool displays the date in an decorated window, simulating the
look of the Blackbox toolbar.

%description -l pl.UTF-8
To narzędzie wyświetla datę w dekorowanym oknie, symulującym wygląd
paska narzędziowego Blackboksa.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
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
%doc AUTHORS BUGS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/bbdate
%{_datadir}/bb*
