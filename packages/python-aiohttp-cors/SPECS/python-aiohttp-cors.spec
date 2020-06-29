%global srcname aiohttp-cors
%global common_desc aiohttp_cors library implements Cross Origin Resource Sharing (CORS) support \
for aiohttp asyncio-powered asynchronous HTTP server.

Name:           python-%{srcname}
Version:        0.7.0
Release:        10%{?dist}
Summary:        CORS (Cross Origin Resource Sharing) support for aiohttp

License:        ASL 2.0
URL:            https://github.com/aio-libs/aiohttp-cors
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Fix test failure of test_add_options_route
Patch1:         %{url}/commit/eb4f5a4bb28f8260d4edc32969e838d9abace051.patch

# Fix test failure of test_static_resource
Patch2:         %{url}/pull/278/commits/e64b95848f3253157d831f4934841fceeaf9b2e3.patch

BuildArch:      noarch

%description
%{common_desc}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires: python3-devel
BuildRequires: python3-setuptools

# For tes suite
BuildRequires: python3-pytest
BuildRequires: python3-pytest-aiohttp
BuildRequires: python3-aiohttp >= 1.1

# Browser tests not possible yet
# BuildRequires: python3-selenium
#
# ifarch on noarch?
# BuildRequires: chromium
# BuildRequires: chromedriver
# Chrome failed to start: exited abnormally
#     (unknown error: DevToolsActivePort file doesn't exist)
#
# BuildRequires: firefox
# BuildRequires: geckodriver -- not available

%description -n python3-%{srcname}
%{common_desc}


%prep
%autosetup -n %{srcname}-%{version} -p1

# remove non-essential pytest plugins
sed -i '/pytest-cov/d' setup.py
sed -i '/pytest-pylint/d' setup.py

# Don't treat warnings as errors, that's what upstream testing is for
# In 0.7.0, nothing else is in this config
rm pytest.ini

# Don't add --cov options to pytest
# In 0.7.0, nothing else is in this config
rm setup.cfg
# tox.ini has this repeated, but we don't need it
rm tox.ini

%build
%py3_build

%install
%py3_install

%check
%{python3} -m pytest -v --ignore tests/integration/test_real_browser.py

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst CHANGES.rst
%{python3_sitelib}/aiohttp_cors
%{python3_sitelib}/aiohttp_cors-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-8
- Run the tests

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-2
- Rebuilt for Python 3.7

* Sun Apr 22 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0 (rhbz #1554157)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 30 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0 (rhbz #1528479)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 0.5.3-1
- Update to 0.5.3

* Fri Feb 10 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 0.5.0-1
- Initial spec.
