%global pypi_name unicodecsv


%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-%{pypi_name}
Version:        0.14.1
Release:        21%{?dist}
Summary:        Drop-in replacement for Python 2.7's csv module which supports unicode strings
License:        BSD
URL:            https://github.com/jdunck/python-unicodecsv
Source0:        https://pypi.python.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0001:      0001-Remove-unittest2-dependency-for-Python-3.x.patch
BuildArch:      noarch

%global _description\
The unicodecsv is a drop-in replacement for Python 2.7's\
csv module which supports unicode strings without a hassle.\
It is NOT a drop-in replacement for Python 3's csv module,\
see https://github.com/jdunck/python-unicodecsv/issues/65

%description %_description

%package -n python3-%{pypi_name}
Summary:        Drop-in replacement for Python 2.7's csv module which supports unicode strings
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{pypi_name}
The unicodecsv is a drop-in replacement for Python 2.7's
csv module which supports unicode strings without a hassle.

It is NOT a drop-in replacement for Python 3's csv module,
see https://github.com/jdunck/python-unicodecsv/issues/65


%prep
%autosetup -p1 -n %{pypi_name}-%{upstream_version}

%build
%py3_build

%install
%py3_install

%check
python3 -m unittest

%files -n python3-%{pypi_name}
%doc README.rst
#TODO ask upstream to add LICENSE file
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-21
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Javier Peña <jpena@redhat.com> - 0.14.1-19
- Remove unittest2 dependency from python3, it is not needed

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-17
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 25 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-15
- Subpackage python2-unicodecsv has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-12
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.14.1-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.14.1-9
- Python 2 binary package renamed to python2-unicodecsv
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 07 2015 Alan Pevec <alan.pevec@redhat.com> - 0.14.1-2
- clarify csv module API compatibility

* Thu Sep 24 2015 Alan Pevec <alan.pevec@redhat.com> - 0.14.1-1
- Update to upstream 0.14.1

* Fri Jul 31 2015 Alan Pevec <apevec@redhat.com> - 0.13.0-1
- Initial package.
