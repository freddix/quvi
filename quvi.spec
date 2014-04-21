Summary:	Command line tool for parsing flash video download links
Name:		quvi
Version:	0.9.5
Release:	1
License:	LGPL v2
Group:		Applications
Source0:	http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
# Source0-md5:	baa1d7b25e9fd173e952e27d4aa4b933
URL:		http://quvi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	libquvi-devel >= 0.9.4
BuildRequires:	perl-tools-pod
BuildRequires:	pkg-config
Requires:	libquvi-scripts
Requires:	lua-socket
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
quvi is a command line tool for parsing video download links.

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/quvi
%{_mandir}/man1/quvi*.1*
%{_mandir}/man5/quvi*.5*

