%bcond_without check
%global pypi_name asynctest

%global desc The package asynctest is built on top of the standard unittest module and cuts\
down boilerplate code when testing libraries for asyncio.\
\
Currently, asynctest targets the “selector” model, hence, some features will not\
(yet?) work with Windows’ proactor.

Name: python-%{pypi_name}
Version: 0.13.0
Release: 5%{?dist}
Summary: Enhance the standard unittest package with asyncio libraries testing
License: ASL 2.0
URL: https://github.com/Martiusweb/asynctest/
Source0: %{pypi_source}
BuildArch: noarch

%description
%{desc}

%package -n python3-%{pypi_name}
Summary: %{summary}
BuildRequires: python3-devel
BuildRequires: python3-nose
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} nosetests-3 -v \
  -e make_inheritance_test \
  -e test_awaited_from_autospec_mock \
  -e test_create_autospec_on_coroutine_and_using_assert_methods \
  -e test_events_watched_outside_test_are_ignored \
  -e test_multiple_patches_on_coroutine \
  -e test_patch_coroutine_only_when_running \
  -e test_patch_coroutine_with_multiple_scopes \
  -e test_patch_generator_with_multiple_scopes_on_same_dict \

%endif

%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 03 2019 Dominik Mierzejewski <dominik@greysector.net> 0.13.0-3
- skip tests failing with python 3.8 (#1739895)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-2
- Rebuilt for Python 3.8

* Sun Aug 11 2019 Dominik Mierzejewski <dominik@greysector.net> 0.13.0-1
- update to 0.13.0
- drop obsolete patch

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Dominik Mierzejewski <dominik@greysector.net> 0.12.2-4
- reintroduce python_provide macro call
- put python3-setuptools into BR, even though it's redundant now
- shorten Summary: to fit in 80 characters

* Mon Jan 14 2019 Dominik Mierzejewski <dominik@greysector.net> 0.12.2-3
- remove trailing space from description
- rename pname to standard pypi_name and use pypi_source macro

* Fri Jan 11 2019 Dominik Mierzejewski <dominik@greysector.net> 0.12.2-2
- ignore test failing under mock
- remove extra newline from description

* Sat Jan 05 2019 Dominik Mierzejewski <dominik@greysector.net> 0.12.2-1
- initial build
