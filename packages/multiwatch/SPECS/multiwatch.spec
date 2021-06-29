Name:           multiwatch
Version:        1.0.0
Release:        3%{?dist}
Summary:        Forks and watches multiple instances of a program in the same context
License:        MIT
URL:            https://redmine.lighttpd.net/projects/multiwatch/wiki
Source0:        https://download.lighttpd.net/multiwatch/releases-1.x/multiwatch-%{version}.tar.xz

# https://git.lighttpd.net/lighttpd/multiwatch/commit/bdd50b7910ebfd04f70e39cb688e3a4851505ac4.patch
Patch0:         multiwatch-1.0.0-fix_signal.patch

BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  libev-devel


%description
Multiwatch forks multiple instance of one application and keeps them running.
It is made to be used with spawn-fcgi, so all forks share the same fastcgi
socket (no web server restart needed if you increase/decrease the number of
forks), and it is easier than setting up multiple daemontool supervised
instances.


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%files
%license COPYING
%doc README
%{_bindir}/multiwatch
%{_mandir}/man1/multiwatch.1.*


%changelog
* Wed May 13 2020 Xavier Bachelot <xavier@bachelot.org> - 1.0.0-3
- Fix spelling in %%description

* Thu Apr 23 2020 Xavier Bachelot <xavier@bachelot.org> - 1.0.0-2
- Add upstream patch to fix --signal behaviour

* Thu Dec 05 2019 Xavier Bachelot <xavier@bachelot.org> - 1.0.0-1
- Initial package
