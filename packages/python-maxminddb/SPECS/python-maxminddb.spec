%global pypi_name maxminddb
%global desc \
This is a Python module for reading MaxMind DB files.  The module includes both\
a pure Python reader and an optional C extension. MaxMind DB is a binary file\
format that stores data indexed by IP address subnets (IPv4 or IPv6).

Name:           python-%{pypi_name}
Version:        1.5.4
Release:        2%{?dist}
Summary:        Reader for the MaxMind DB format

License:        ASL 2.0
URL:            https://www.maxmind.com/
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  libmaxminddb-devel

%description %{desc}

%package doc
Summary:        Documentation for %{pypi_name}

%description doc
This package provides the documentation for %{pypi_name}.

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-mock
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{desc}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files doc
%doc docs/*

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.4-2
- Rebuilt for Python 3.9

* Thu May 07 2020 Lumír Balhar <lbalhar@redhat.com> - 1.5.4-1
- Update to 1.5.4 (#1831900)

* Tue May 05 2020 Lumír Balhar <lbalhar@redhat.com> - 1.5.3-1
- Update to 1.5.3 (#1831244)

* Tue Jan 28 2020 Lumír Balhar <lbalhar@redhat.com> - 1.5.2-1
- New upstream version 1.5.2 (#1785719)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Oct 02 2019 Lumír Balhar <lbalhar@redhat.com> - 1.5.1-1
- New upstream version 1.5.1 (bz#1756523)

* Wed Oct 02 2019 Lumír Balhar <lbalhar@redhat.com> - 1.5.0-1
- New upstream version 1.5.0 (bz#1756523)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.1-3
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Carl George <carl@george.computer> - 1.4.1-1
- Latest upstream

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-3
- Rebuilt for Python 3.7

* Tue Jun 12 2018 Carl George <carl@george.computer> - 1.4.0-2
- EPEL compatibility

* Mon May 28 2018 Lumir Balhar <lbalhar@redhat.com> - 1.4.0-1
- New upstream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.0-4
- Fix ambiguous Python 2 dependency declarations
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0 (#1431895)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Lumir Balhar <lbalhar@redhat.com> - 1.2.3-1
- New upstream version.

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-2
- Rebuild for Python 3.6

* Tue Nov 22 2016 Lumir Balhar <lbalhar@redhat.com> - 1.2.2-1
- New upstream version.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 15 2016 Lumir Balhar <lbalhar@redhat.com> - 1.2.1-1
- Initial package.
