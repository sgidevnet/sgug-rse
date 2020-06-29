%{?python_enable_dependency_generator}

%global pypi_name geoip2
%global srcname GeoIP2-python
%global desc This package provides an API for the GeoIP2 web services.
%global test_data MaxMind-DB
%global test_data_rls f6ed981c23b0eb33d7c07568e2177236252afda6

Name:           python-%{pypi_name}
Version:        3.0.0
Release:        2%{?dist}
Summary:        MaxMind GeoIP2 API

License:        ASL 2.0
URL:            https://www.maxmind.com/
Source0:        https://github.com/maxmind/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Source1:        https://github.com/maxmind/%{test_data}/archive/%{test_data_rls}/%{test_data}-%{test_data_rls}.tar.gz

BuildArch:      noarch

%description
%{desc}

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-requests
BuildRequires:  python3-maxminddb
BuildRequires:  python3-requests-mock
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}

%package doc
Summary:        Documentation for %{name}
BuildRequires:  %{_bindir}/sphinx-build

%description doc
This package provides the documentation for %{pypi_name}.

%prep
%autosetup -n %{srcname}-%{version} -a 1
rmdir tests/data
mv -f %{test_data}-%{test_data_rls} tests/data

%build
%py3_build
sphinx-build -b html docs html
rm -rf html/.{buildinfo,doctrees}

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info/

%files doc
%doc html/
%license LICENSE

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-2
- Rebuilt for Python 3.9

* Wed Feb 05 2020 Lumír Balhar <lbalhar@redhat.com> - 3.0.0-1
- New upstream version 3.0.0 (#1785833)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.9.0-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.9.0-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.9.0-5
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 23 2018 Carl George <carl@george.computer> - 2.9.0-3
- EPEL compatibility

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.9.0-2
- Rebuilt for Python 3.7

* Mon May 28 2018 Lumir Balhar <lbalhar@redhat.com> - 2.9.0-1
- Update to 2.9.0

* Thu Apr 12 2018 Lumir Balhar <lbalhar@redhat.com> - 2.8.0-1
- Update to 2.8.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.7.0-1
- Update to 2.7.0

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.6.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Nov 01 2017 Lumir Balhar <lbalhar@redhat.com> - 2.6.0-1
- New upstream version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Lumir Balhar <lbalhar@redhat.com> - 2.5.0-1
- Update to 2.5.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.4.2-2
- Rebuild for Python 3.6

* Tue Dec 13 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.4.2-1
- Update to 2.4.2

* Tue Nov 22 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 15 2016 Lumir Balhar <lbalhar@redhat.com> - 2.4.0-1
- Initial package.
