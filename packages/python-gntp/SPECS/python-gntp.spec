%global srcname gntp

Name:           python-%{srcname}
Version:        1.0.3
Release:        13%{?dist}
Summary:        Growl Notification Transport Protocol for Python
License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/kfdm/%{srcname}/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools


%description
This is a Python library for working with the Growl Notification Transport
Protocol.

It should work as a drop-in replacement for the older Python bindings.


%package -n python3-%{srcname}
Summary:  %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
# %%{_bindir}/%%{srcname} was moved from there:
Obsoletes: python2-%{srcname} < 1.0.3-12

%description -n python3-%{srcname}
This is a Python3 library for working with the Growl Notification Transport
Protocol.

It should work as a drop-in replacement for the older Python bindings.


%prep
%setup -q -n %{srcname}-%{version}

# Remove executable bit, shabang line from library source:
chmod -x %{srcname}/cli.py
sed -i '/#!\/usr\/bin\/env python/,/^$/d' gntp/cli.py

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build


%install
%py3_install

# Now /usr/bin/gntp is Python 3, so we move it away
mv %{buildroot}%{_bindir}/%{srcname} %{buildroot}%{_bindir}/%{srcname}-%{python3_version}

# The guidelines also specify we must provide symlinks with a '-X' suffix.
ln -s ./%{srcname}-%{python3_version} %{buildroot}%{_bindir}/%{srcname}-3

# Finally, we provide /usr/bin/gntp as a link to /usr/bin/gntp-3
ln -s ./%{srcname}-3 %{buildroot}%{_bindir}/%{srcname}


%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{_bindir}/%{srcname}
%{_bindir}/%{srcname}-3
%{_bindir}/%{srcname}-%{python3_version}


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-11
- Subpackage python2-gntp has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-2
- Rebuild for Python 3.6

* Mon Aug 08 2016 Dominika Krejci <dkrejci@redhat.com> - 1.0.3-1
- Update to 1.0.3
- Add Python 3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 15 2013 Conrad Meyer <cemeyer@uw.edu> - 1.0.1-3
- Remove bundled egg (as per rh #917328 review)

* Sat Jun 15 2013 Conrad Meyer <cemeyer@uw.edu> - 1.0.1-2
- Add dependency on python-setuptools to avoid buggy python-distutils fallback

* Mon Apr 29 2013 Conrad Meyer <cemeyer@uw.edu> - 1.0.1-1
- Bump to latest upstream

* Mon Apr 29 2013 Conrad Meyer <cemeyer@uw.edu> - 0.9-2
- New-world spec cleanups (python_sitelib is already defined, don't need to
  nuke buildroot during install)
- BR python2-devel, not python-devel

* Sat Mar 2 2013 Conrad Meyer <cemeyer@uw.edu> - 0.9-1
- Initial package
