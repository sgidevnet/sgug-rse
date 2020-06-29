# Created by pyp2rpm-2.0.0
%global pypi_name rcssmin

Name:           python-%{pypi_name}
Version:        1.0.6
Release:        20%{?dist}
Summary:        CSS Minifier

License:        ASL 2.0
URL:            http://opensource.perlig.de/rcssmin/
Source0:        https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc

%description
RCSSmin is a CSS minifier.

The minifier is based on the semantics of the YUI compressor, which itself
is based on the rule list by Isaac Schlueter.

This module is a re-implementation aiming for speed instead of maximum
compression, so it can be used at runtime (rather than during a preprocessing
step).

%package -n     python3-%{pypi_name}
Summary:        CSS Minifier
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools


%description -n python3-%{pypi_name}
RCSSmin is a CSS minifier.

The minifier is based on the semantics of the YUI compressor, which itself
is based on the rule list by Isaac Schlueter.

This module is a re-implementation aiming for speed instead of maximum
compression, so it can be used at runtime (rather than during a preprocessing
step).

%prep
%autosetup -n %{pypi_name}-%{version}

# strip bang path from rcssmin.py
sed -i '1d' rcssmin.py

%build
%py3_build
%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install

# remove upstream developer documentation
rm -r %{buildroot}/%{_docdir}/%{pypi_name}/

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE bench/LICENSE.cssmin
%{python3_sitearch}/%{pypi_name}.py
%{python3_sitearch}/_%{pypi_name}.cpython*
%{python3_sitearch}/__pycache__/%{pypi_name}.cpython*
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.6-20
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.6-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.6-17
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.6-14
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.6-12
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.6-11
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Matthias Runge <mrunge@redhat.com> - 1.0.6-10
- add gcc to buildrequires

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.6-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.6-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 31 2016 Matthias Runge <mrunge@redhat.com> - 1.0.6-2
- build python3 on only on Fedora

* Fri Feb 26 2016 Matthias Runge <mrunge@redhat.com> - 1.0.6-1
- Initial package. (rhbz#1312360)
