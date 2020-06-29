
%global srcname statsd

Name:       python-%{srcname}
Version:    3.2.1
Release:    18%{?dist}
Summary:    A Python statsd client

License:    MIT
URL:        https://github.com/jsocol/pystatsd
Source0:    https://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
# Apply https://github.com/jsocol/pystatsd/pull/88
Patch0:     0001-Fix-sphinx-extension-conflict.patch

BuildArch:  noarch

BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-nose

%description
A python client for the statsd daemon.

%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A python client for the statsd daemon.

%package doc
Summary: Documentation of the Python client for the statsd daemon
BuildRequires:  python3-sphinx

%description doc
Documentation of the Python client for the statsd daemon.

%prep
%autosetup -n %{srcname}-%{version} -p1
# Remove bundled egg-info
rm -rf %{srcname}.egg-info
# Let RPM handle the dependencies
rm -f requirements.txt

%build
%py3_build

## generate html docs
sphinx-build docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc AUTHORS README.rst
%{python3_sitelib}/*

%files doc
%license LICENSE
%doc html

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-18
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-13
- Subpackage python2-statsd has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.2.1-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Tristan de Cacqueray <tdecacqu@redhat.com> - 3.2.1-5
- Fix sphinx-build error

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-4
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Paul Belanger <pabelanger@redhat.com> - 3.2.1-2
- Ensure python3-statsd only exists when with_python3 defined
- Add python3 testing dependencies
- Run tests under python3

* Fri Dec 18 2015 Paul Belanger <pabelanger@redhat.com> - 3.2.1-1
- New upstream version - 3.2.1
- Add support for both python2 and python3.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Tristan de Cacqueray <tdecacqu@redhat.com> - 2.1.2-2.fc21
- Fixed fedora-review warnings

* Thu Apr 23 2015 Tristan de Cacqueray <tdecacqu@redhat.com> - 2.1.2-1.fc21
- Initial packaging
