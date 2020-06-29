%global srcname sievelib
%global _description\
Client-side Sieve and Managesieve library written in Python.\
* Sieve : An Email Filtering Language (RFC 5228).\
* ManageSieve : A Protocol for Remotely Managing Sieve Scripts (RFC 5804).

Name:           python-%{srcname}
Version:        1.1.1
Release:        11%{?dist}
Summary:        Client-side SIEVE library
License:        MIT
URL:            https://github.com/tonioo/sievelib
Source:         https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz

# Fix issue with relying on pip's internal API
# Resolved upstream: https://github.com/tonioo/sievelib/pull/73
Patch0:         list-requirements-in-setup.py.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-nose
BuildRequires:  python3-six
BuildRequires:  python3-future
BuildRequires:  python3-pip

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Client-side Sieve and Managesieve library written in Python.
* Sieve : An Email Filtering Language (RFC 5228)
* ManageSieve : A Protocol for Remotely Managing Sieve Scripts (RFC 5804)

%prep
%autosetup -n %{srcname}-%{version} -p1
# remove bundled egg-info
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
# Remove shebang from libraries
for lib in %{buildroot}%{python2_sitelib}/%{srcname}/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
%py3_install
# Remove shebang from libraries
for lib in %{buildroot}%{python3_sitelib}/%{srcname}/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%check
nosetests-%{python3_version}

%files -n python3-%{srcname}
%doc README.rst
%license COPYING
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info

%changelog
* Tue Jun 16 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.1.1-11
- Fix build with pip >= 20.1 (#1838484)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.1-4
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-2
- Rebuilt for Python 3.7

* Tue Mar 13 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-1
- Version 1.1.1
- Github's tarball doesn't build, use Pypi instead.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 21 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.0.0-1
- Version 1.0.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 01 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.9.2-8
- Python3 changes

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.9.2-3
- Use python_provide macro

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 21 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.9.2-1
- New version 0.9.2

* Mon Jun 29 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-5.20150629gite34fb54
- Add python3 subpackage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 09 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-3
- Use license macro

* Wed Dec 03 2014 Juan Orti <jorti@fedoraproject.org> - 0.8-2
- Remove python shebang from libraries
- Change URL to GitHub
- Include license file

* Tue Dec 02 2014 Juan Orti <jorti@fedoraproject.org> - 0.8-1
- Spec file cleanup

* Sat May 24 2014 Didier Fabert <didier.fabert@gmail.com> 0.0.4-1
- Initial RPM release
