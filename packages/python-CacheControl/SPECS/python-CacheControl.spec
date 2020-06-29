%global pypi_name CacheControl
%global pypi_name_lower cachecontrol

%{?python_enable_dependency_generator}

%global common_description %{expand:
CacheControl is a port of the caching algorithms in httplib2 for use with
requests session object. It was written because httplib2's better support
for caching is often mitigated by its lack of thread safety. The same is
true of requests in terms of caching.}

Name:           python-%{pypi_name}
Summary:        httplib2 caching for requests
Version:        0.12.6
Release:        4%{?dist}
License:        MIT

URL:            https://github.com/ionrock/cachecontrol
Source0:        %{url}/archive/v%{version}/%{pypi_name_lower}-%{version}.tar.gz

# use mock from python standard library
Patch0:         00-use-stdlib-mock.patch

BuildArch:      noarch

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        httplib2 caching for requests

%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# test dependencies
BuildRequires:  python3-cherrypy
BuildRequires:  python3-pytest
BuildRequires:  python3-lockfile
BuildRequires:  python3-msgpack >= 0.5.2
BuildRequires:  python3-redis
BuildRequires:  python3-requests

# optional dependencies
Recommends:     python3dist(lockfile) >= 0.9
Recommends:     python3dist(redis) >= 2.10.5

%description -n python3-%{pypi_name} %{common_description}


%prep
%autosetup -n %{pypi_name_lower}-%{version} -p1


%build
%py3_build


%install
%py3_install


%check
# skip a test requiring internet access
%{__python3} -m pytest -v tests -k "not test_file_cache_recognizes_consumed_file_handle"


%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE.txt

%{_bindir}/doesitcache

%{python3_sitelib}/%{pypi_name_lower}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/


%changelog
* Fri Jun 05 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.6-4
- Rebuilt with cherrypy tests

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.6-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 22 2019 Fabio Valentini <decathorpe@gmail.com> - 0.12.6-1
- Update to version 0.12.6.

* Fri Dec 13 2019 Fabio Valentini <decathorpe@gmail.com> - 0.12.5-7
- Recommend optional dependencies.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.5-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 20 2019 Fabio Valentini <decathorpe@gmail.com> - 0.12.5-5
- Port to pytest >=4.0.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.5-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 16 2018 Miro Hrončok <mhroncok@redhat.com> - 0.12.5-1
- Update to 0.12.5
- Remove python2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.12.3-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.12.3-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Sep 13 2017 Iryna Shcherbina <ishcherb@redhat.com> - 0.10.0-2
- Fix Python 2 dependency from python3-CacheControl (rhbz#1490893)

* Wed Aug 23 2017 Tomas Krizek <tkrizek@redhat.com> - 0.12.3-1
- Update to 0.12.3

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.11.5-8
- Python 2 binary package renamed to python2-cachecontrol
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.11.5-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.5-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Jun 19 2015 Slavek Kabrda <bkabrda@redhat.com> - 0.11.5-1
- Update to 0.11.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 04 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.10.1-1
- Initial package.

